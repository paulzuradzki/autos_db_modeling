# `autos_etl`

# Description

Package for schema definition and ETL for auto data.

# Setup

This setup assumes you are cloning the source code locally and building from source rather than pip-installing the package from Git.

#### Clone the source 
```bash
$ git clone git+https://github.com/paulzuradzki/autos_db_modeling.git
$ cd autos_db_modeling
```

#### Install Python dependencies
```bash
$ python -m venv venv
$ source venv/bin/activate
(venv) $ python -m pip install --upgrade pip

(venv) $ python -m pip install -r requirements.txt
(venv) $ python -m pip install -r requirements_dev.txt
```

#### Load environment variables
* You only need to do this if you are running migrations.
* This bash script will load the `DATABASE_URL` environment variable from `.env` file.

```bash
(venv) $ source ./setup.sh
```

* The `DATABASE_URL` variable is accessed in `alembic.ini` for migrations. 
* The idea behind parameterizing this variable is if you wanted to alternate between a dev and prod database.


# Usage

#### Generate ERD

```bash
(venv) $ scripts/make_erd.py
```

#### Apply Database Schema Changes

* Migrations allow you to track, upgrade, and downgrade the states of the database schema.
* A migrations tool lets you compare the state of your database to the models defined in your application code.
* This helps solve the problem of keeping models (aka, ORM mapped classes) in sync with the database.
* In `alembic/versions`, you can see an append-only log of database schema changes. 
* You can also use `alembic` to get the lower-level SQL DDL (Data Definition Language).

```bash
# Example of making a migration
# This creates a migrations  file in alembic/versions/*.py
alembic revision --autogenerate -m "initial schema"

# Example of applying a migration
# On first execution (if there is a migration file), 
# this will run all the create-table statements in the database
alembic upgrade head

# Generate the SQL
# This does not apply changes to the database
alembic upgrade head --sql > migration.sql
```

#### Using a different schema / metadata object

See `alembic/env.py`

```python
# alembic/env.py
from autos_etl.model_01_dealer import metadata_obj
target_metadata = metadata_obj
```

Update the import and `target_metadata` as needed if you want to point to a different schema as opposed to running incremental migrations from schema A to B.

#### Load the database

Transform and load source data to the datababse.

```bash
python scripts/load_db.py
```

# Troubleshooting

#### Issue: ERAlchemy2-generated diagrams are not displaying joins. 

Solution: ERAlchemy won't correctly render if you use a schema.

```python
metadata_obj = MetaData(schema="autos_etl")
```

For diagram generation, update to use default schema in SQLAlchemy database objects by removing the schema argument like so.

```python
metadata_obj = MetaData()
```
