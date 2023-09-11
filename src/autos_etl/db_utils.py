import os
from urllib.parse import urlparse

import psycopg2


def clear_db() -> None:
    # includes alembic_version
    sql = """\
        drop table autos_etl.fact_customer_relations;
        drop table autos_etl.fact_inventory;
        drop table autos_etl.fact_sale_transactions;
        drop table autos_etl.dim_vehicle;
        drop table autos_etl.dim_customer;
        drop table autos_etl.dim_discount_type;
        drop table autos_etl.dim_vehicle_model;
        drop table autos_etl.alembic_version;
        """

    # Parse the DB URL
    url = urlparse(os.environ.get("DATABASE_URL"))

    # Connect to DB
    with psycopg2.connect(
        database=url.path[1:],
        user=url.username,
        password=url.password,
        host=url.hostname,
        port=url.port,
    ) as conn:
        with conn.cursor() as cursor:
            cursor.execute(sql)
            conn.commit()


def delete_from_tables() -> None:
    sql = """\
        delete from autos_etl.fact_customer_relations;
        delete from autos_etl.fact_inventory;
        delete from autos_etl.fact_sale_transactions;
        delete from autos_etl.dim_vehicle;
        delete from autos_etl.dim_customer;
        delete from autos_etl.dim_discount_type;
        delete from autos_etl.dim_vehicle_model;
        """

    url = urlparse(os.environ.get("DATABASE_URL"))

    with psycopg2.connect(
        database=url.path[1:],
        user=url.username,
        password=url.password,
        host=url.hostname,
        port=url.port,
    ) as conn:
        with conn.cursor() as cursor:
            cursor.execute(sql)
            conn.commit()
