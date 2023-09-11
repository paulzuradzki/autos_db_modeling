import os
from typing import Dict
from urllib.parse import urlparse

import pandas as pd
import psycopg2
from psycopg2.extras import execute_values
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from . import db_utils

# get_df_ex2_file_a_customers,
# get_df_ex2_file_a_transactions,
from .model_01_dealer import DISCOUNT_TYPE_CHOICES
from .orm_mapped_classes import Vehicle, VehicleModel
from .preload_extract_transform import (
    get_df_file_a,
    get_df_file_b,
    get_df_file_c,
)


def start_loading_sequence():
    db_utils.delete_from_tables()
    # dim_vehicle_model must be loaded first
    load_dim_vehicle_model()
    load_dim_vehicle()
    load_fact_inventory()
    load_dim_customer()
    load_discount_type_dim()
    load_fact_customer_relations()
    load_fact_sale_transactions()


def load_dim_vehicle_model() -> None:
    df_file_a = get_df_file_a()

    file_a_data = df_file_a.drop(columns=["id", "vin"]).to_dict(orient="records")
    engine = create_engine(os.environ.get("DATABASE_URL", ""))

    with Session(engine) as session:
        vehicle_models = [VehicleModel(**info) for info in file_a_data]
        session.bulk_save_objects(vehicle_models)
        session.commit()


def load_dim_vehicle() -> None:
    df_file_a = get_df_file_a()
    engine = create_engine(os.environ.get("DATABASE_URL", ""))
    dim_vehicle_model = pd.read_sql(
        "select * from autos_etl.dim_vehicle_model;", con=engine
    )

    join_keys = [
        "year",
        "make",
        "model",
        "trim",
        "wheel_drive_type",
        "color",
        "door_type",
        "drive_train_type",
    ]

    merged_df = df_file_a.merge(
        dim_vehicle_model.astype(str),
        left_on=join_keys,
        right_on=join_keys,
        how="inner",
        suffixes=("_source", "_dim"),
    )

    mapping_vin_to_dim_vehicle_model_id = (
        merged_df[["vin", "id_dim"]]
        .rename(columns={"id_dim": "dim_vehicle_model_id"})
        .set_index("vin")
        .to_dict()
    )
    mapping_vin_to_dim_vehicle_model_id_as_df = df_file_a[["vin"]].assign(
        dim_vehicle_model_id=lambda _df: _df["vin"].map(
            mapping_vin_to_dim_vehicle_model_id["dim_vehicle_model_id"]
        )
    )

    vehicle_data = mapping_vin_to_dim_vehicle_model_id_as_df.to_dict(orient="records")

    with Session(engine) as session:
        vehicles = [Vehicle(**info) for info in vehicle_data]
        session.bulk_save_objects(vehicles)
        session.commit()


def load_fact_inventory() -> None:
    engine = create_engine(os.environ.get("DATABASE_URL", ""))

    dim_vehicle_df = pd.read_sql("select * from autos_etl.dim_vehicle;", con=engine)

    df_file_a = get_df_file_a()
    vins_to_add = df_file_a["vin"].values.tolist()

    mapping_vin_to_dim_vehicle_id: Dict[str, int] = (
        dim_vehicle_df[["vin", "id"]].set_index("vin").to_dict()["id"]
    )
    rows_to_insert = [
        {"dim_vehicle_id": mapping_vin_to_dim_vehicle_id[vin], "is_in_stock": True}
        for vin in vins_to_add
    ]
    rows_to_insert = [tuple(item.values()) for item in rows_to_insert]

    # Parse the URL
    url = urlparse(os.environ.get("DATABASE_URL"))

    with psycopg2.connect(
        database=url.path[1:],
        user=url.username,
        password=url.password,
        host=url.hostname,
        port=url.port,
    ) as conn:
        # Bulk insert
        # id, created, and last_updated fields will be handled by the DB
        # However, we need to update last_updated manually if we use raw SQL in lieue of ORM
        with conn.cursor() as cursor:
            insert_query = "INSERT INTO autos_etl.fact_inventory (dim_vehicle_id, is_in_stock) VALUES %s"
            execute_values(cursor, insert_query, rows_to_insert)
            conn.commit()


def load_dim_customer() -> None:
    df_file_b = get_df_file_b()

    # `rows_to_insert` takes form:
    # [['Harry', 'Potter', 'D', '2008 Williams Dr', 'Chicago', 'IL', 'USA', False],
    #  ['Hermione', 'Granger', 'S', '190 Clemton Ave', None, 'IL', 'USA', False]]

    rows_to_insert: list[tuple] = (
        df_file_b.loc[
            :, ["FirstName", "LastName", "MI", "Address", "City", "State", "Country"]
        ]
        .rename(
            columns={
                "FirstName": "first_name",
                "LastName": "last_name",
                "MI": "middle_initial",
                "Address": "address",
                "City": "city",
                "State": "state",
                "Country": "country",
            }
        )
        .assign(is_repeat_customer=False)
        .fillna(pd.NA)
        # .to_dict(orient="records")
        .to_records(index=False)
        .tolist()
    )

    rows_to_insert = convert_NaNs_to_None_for_db(rows_to_insert)

    url = urlparse(os.environ.get("DATABASE_URL"))

    with psycopg2.connect(
        database=url.path[1:],
        user=url.username,
        password=url.password,
        host=url.hostname,
        port=url.port,
    ) as conn:
        with conn.cursor() as cursor:
            insert_query = """INSERT INTO autos_etl.dim_customer (
                first_name, 
                last_name, 
                middle_initial,
                address,
                city,
                state,
                country,
                is_repeat_customer
                ) VALUES %s"""
            execute_values(cursor, insert_query, rows_to_insert)
            conn.commit()


def convert_NaNs_to_None_for_db(rows: list[tuple]):
    for i, record in enumerate(rows):
        modified_record = [None if pd.isna(val) else val for val in record]
        rows[i] = modified_record
    return rows


def load_discount_type_dim():
    rows_to_insert = [[choice] for choice in DISCOUNT_TYPE_CHOICES]
    url = urlparse(os.environ.get("DATABASE_URL"))

    with psycopg2.connect(
        database=url.path[1:],
        user=url.username,
        password=url.password,
        host=url.hostname,
        port=url.port,
    ) as conn:
        with conn.cursor() as cursor:
            insert_query = """INSERT INTO autos_etl.dim_discount_type (
                name
                ) VALUES %s"""
            execute_values(cursor, insert_query, rows_to_insert)
            conn.commit()

def load_fact_customer_relations() -> None:
    df_file_c = get_df_file_c()
    records = df_file_c.map(lambda s: s.strip()).to_dict(orient="records")
    for row in records:
        row["customer_id"] = _get_customer_id_from_full_name(row["name"])

    rows_to_insert = [(row["customer_id"], row["note"]) for row in records]
    url = urlparse(os.environ.get("DATABASE_URL"))

    with psycopg2.connect(
        database=url.path[1:],
        user=url.username,
        password=url.password,
        host=url.hostname,
        port=url.port,
    ) as conn:
        with conn.cursor() as cursor:
            insert_query = """INSERT INTO autos_etl.fact_customer_relations (
                dim_customer_id, encounter_notes
                ) VALUES %s"""
            execute_values(cursor, insert_query, rows_to_insert)
            conn.commit()


def load_fact_sale_transactions() -> None:
    df_file_b = get_df_file_b()

    def make_full_name(row):
        last = row["LastName"]
        first = row["FirstName"]
        middle = row["MI"]
        return f"{last} {first} {middle}".strip()

    def clean_currency(value):
        if pd.isna(value):
            return None
        # Remove dollar sign, commas, and leading/trailing whitespace
        cleaned_value = value.replace("$", "").replace(",", "").strip()

        # Convert to float
        try:
            return float(cleaned_value)
        except ValueError:
            print(f"Unable to convert {value} to float")
            return None

    records = (
        df_file_b.assign(
            full_name=lambda _df: _df.fillna("").apply(make_full_name, axis=1)
        )
        .rename(
            columns={
                "SaleDate": "sale_date",
            }
        )
        .assign(
            dim_vehicle_id=lambda _df: _df["VIN"].apply(_get_vehicle_id_from_vin),
            dim_customer_id=lambda _df: _df["full_name"].apply(
                _get_customer_id_from_full_name
            ),
            dim_discount_type_id=lambda _df: _df["Discount"].apply(
                _get_discount_type_id_from_string
            ),
            is_trade_in=lambda _df: _df["TradeIn"].map(
                lambda x: {"Yes": True}.get(x, False)
            ),
            purchase_price_amount=lambda _df: _df["PurchasePrice"].apply(
                clean_currency
            ),
            trade_in_value_amount=lambda _df: _df["TradeInValue"].apply(clean_currency),
        )
        .loc[
            :,
            [
                "dim_customer_id",
                "dim_vehicle_id",
                "dim_discount_type_id",
                "sale_date",
                "purchase_price_amount",
                "is_trade_in",
                "trade_in_value_amount",
            ],
        ]
        .to_dict(orient="records")
    )

    rows_to_insert = convert_NaNs_to_None_for_db(
        [tuple(record.values()) for record in records]
    )
    url = urlparse(os.environ.get("DATABASE_URL"))

    with psycopg2.connect(
        database=url.path[1:],
        user=url.username,
        password=url.password,
        host=url.hostname,
        port=url.port,
    ) as conn:
        with conn.cursor() as cursor:
            insert_query = """INSERT INTO autos_etl.fact_sale_transactions (
                dim_customer_id, 
                dim_vehicle_id, 
                dim_discount_type_id, 
                sale_date, 
                purchase_price_amount, 
                is_trade_in, 
                trade_in_value_amount
                ) VALUES %s"""
            execute_values(cursor, insert_query, rows_to_insert)
            conn.commit()

# NOTE: cache can be stale if dim tables are re-updated with new keys
# @functools.lru_cache
def _get_customer_id_from_full_name(full_name: str) -> int:
    engine = create_engine(os.environ.get("DATABASE_URL", ""))
    dim_customer_df = pd.read_sql("select * from autos_etl.dim_customer;", con=engine)

    def make_full_name(row):
        last = row["last_name"]
        first = row["first_name"]
        middle = row["middle_initial"]
        return f"{last} {first} {middle}".strip()

    # Derive full_name in format "Last First MI" (ex: "Dumbledore Albus R")
    dim_customer_df = dim_customer_df.assign(
        full_name=lambda _df: _df.fillna("").apply(make_full_name, axis=1)
    )

    customer_id = dim_customer_df.query("full_name==@full_name")["id"].values.tolist()[
        0
    ]

    return customer_id

def _get_vehicle_id_from_vin(vin: str) -> int:
    vin_upper = vin.upper()
    engine = create_engine(os.environ.get("DATABASE_URL", ""))
    dim_vehicle_df = pd.read_sql("select * from autos_etl.dim_vehicle;", con=engine)    
    dim_vehicle_id = dim_vehicle_df.query("vin.str.upper()==@vin_upper")["id"].values.tolist()[0]
    return dim_vehicle_id

def _get_discount_type_id_from_string(discount_string: str) -> int:
    engine = create_engine(os.environ.get("DATABASE_URL", ""))
    dim_discount_type_df = pd.read_sql("select * from autos_etl.dim_discount_type;", con=engine)    
    
    try:
        dim_discount_type_id = dim_discount_type_df.query("name==@discount_string")["id"].values.tolist()[0]
    # ID not found
    except IndexError:
        dim_discount_type_id = dim_discount_type_df.query("name=='N/A'")["id"].values.tolist()[0]
    return dim_discount_type_id

