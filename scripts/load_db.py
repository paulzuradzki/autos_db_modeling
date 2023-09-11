import dotenv
from autos_etl.load import start_loading_sequence

dotenv.load_dotenv(override=True)

# Clears existing table data (keeping tables) and loads data
start_loading_sequence()
