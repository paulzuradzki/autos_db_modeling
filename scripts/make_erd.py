"""Script to generate Entity Relationship Diagrams (ERDs) from SQLAlchemy MetaData 
objects.

Note: ERAlchemy does not currently support table schemas (like `schema.table` prefix) 
with Postgres when defining metadata from Python. 
* E.g., `MetaData(schema="autos_etl")` will not work
* Go to your models file and modify to use `MetaData()` (no schema argument)
  for creating the ERD
"""

from pathlib import Path

from autos_etl import model_01_dealer, model_02_preowned_dealer, model_03_merged_dealer
from eralchemy2 import render_er

Path("out").mkdir(exist_ok=True)

model_map = {
    "model_01_dealer": model_01_dealer,
    "model_02_preowned_dealer": model_02_preowned_dealer,
    "model_03_merged_dealer": model_03_merged_dealer,
}

for model_name, model_module in model_map.items():
    # TODO: not implemented yet
    if model_name == "model_03_merged_dealer":
        continue
    render_er(model_module.metadata_obj, f"./out/erd_{model_name}.pdf")
