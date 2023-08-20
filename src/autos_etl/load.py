import pandas as pd


from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import os
from autos_etl.models import Vehicle, VehicleModel

from autos_etl.extract import (
    get_df_file_a,
    # get_df_file_b,
    # get_df_file_c,
    # get_df_ex2_file_a_transactions,
    # get_df_ex2_file_a_customers,
)


def load_dim_vehicle_model() -> None:
    df_file_a = get_df_file_a()

    file_a_data = df_file_a.drop(columns=["id", "vin"]).to_dict(orient="records")
    engine = create_engine(os.environ.get("DATABASE_URL", ""), echo=True)

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
