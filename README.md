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

#### Run Database Migrations

* Migrations allow you to track, upgrade, and downgrade the states of the database schema.
* A migrations tool lets you compare the state of your database to the models defined in your application code.
* This helps solve the problem of keeping models (aka, ORM mapped classes) in sync with the database.
* In `alembic/versions`, you can see an append-only log of database schema changes. 
* You can also use `alembic` to get the lower-level SQL DDL (Data Definition Language).

```bash
# Example of making a migration
alembic revision --autogenerate -m "add transaction type table"

# Example of applying a migration
alembic upgrade head

# Generating SQL instead of applying the migration
alembic upgrade head --sql > migration.sql
```