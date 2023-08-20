from pathlib import Path

from autos_etl import models
from eralchemy2 import render_er

Path("out").mkdir(exist_ok=True)
render_er(models.metadata_obj, "./out/erd_from_sqlalchemy.pdf")
