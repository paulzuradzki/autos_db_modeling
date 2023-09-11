"""Script to create an Excel workbook with a table showing column-level database schema.

This includes table names, column names, types, and comments.
"""

import dotenv
import pandas as pd
from autos_etl.model_01_dealer import metadata_obj
from sqlalchemy import create_engine
import os

dotenv.load_dotenv(override=True)

column_items = []
for table_name, table in metadata_obj.tables.items():
    for column in table.columns:
        column_item = {
            "table_name": table_name,
            "column.name": column.name,
            "column.type": column.type,
            "column.primary_key": column.primary_key,
            "column.foreign_keys": ", ".join(
                [f"{k.column.table.name}.{k.column.name}" for k in column.foreign_keys]
            ),
            # "column.unique": column.unique,
            "column.nullable": column.nullable,
            # Description of column
            "column_comment": column.comment,
            # Description of table
            "table_comment": table.comment,
        }
        column_items.append(column_item)

schema_df = pd.DataFrame(column_items)

out_filepath = "./out/model_1_schema_and_example_data.xlsx"

with pd.ExcelWriter(out_filepath) as writer:
    schema_df.to_excel(writer, index=False, sheet_name="schema")

    table_names = [
        "fact_inventory",
        "dim_vehicle_model",
        "dim_vehicle",
        "dim_customer",
        "dim_discount_type",
        "fact_customer_relations",
        "fact_sale_transactions",
    ]

    engine = create_engine(os.environ.get("DATABASE_URL", ""))
    for table_name in table_names:
        table_df = pd.read_sql(f"select * from autos_etl.{table_name};", con=engine)
        table_df.to_excel(writer, index=False, sheet_name=f"table_{table_name}")
