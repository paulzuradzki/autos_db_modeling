from sqlalchemy import (
    BOOLEAN,
    DATE,
    DECIMAL,
    TIMESTAMP,
    Column,
    ForeignKey,
    Integer,
    MetaData,
    String,
    Table,
    text,
)

metadata_obj = MetaData(schema="autos_etl")
# For ERAlchemy2. No schema supportin ERD creation from Python/SQLAlchemy.
# metadata_obj = MetaData()

fact_transaction = Table(
    "fact_transaction",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("created", TIMESTAMP, server_default=text("CURRENT_TIMESTAMP")),
    Column(
        "last_updated",
        TIMESTAMP,
        server_default=text("CURRENT_TIMESTAMP"),
        onupdate=text("CURRENT_TIMESTAMP"),
    ),
    Column("transaction_id", Integer),
    Column("dim_employee_id", ForeignKey("dim_employee.id")),
    Column("dim_customer_id", ForeignKey("dim_customer.id")),
    Column("dim_vehicle_id", ForeignKey("dim_vehicle.id")),
    Column("sale_date", DATE),
    Column("purchase_price_amount", DECIMAL),
    Column(
        "is_trade_in",
        BOOLEAN,
        comment="True if transaction involves a trade-in vehicle.",
    ),  # noqa
    Column("trade_in_value_amount", DECIMAL),
    comment="""Transaction table of used cars. Transactions include (1) purchases from 
    customers buying car with or without a trade-in sale and (2) sales from suppliers to
    our organization.""",  # noqa
)

dim_customer = Table(
    "dim_customer",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("created", TIMESTAMP, server_default=text("CURRENT_TIMESTAMP")),
    Column(
        "last_updated",
        TIMESTAMP,
        server_default=text("CURRENT_TIMESTAMP"),
        onupdate=text("CURRENT_TIMESTAMP"),
    ),
    Column("first_name", String(50)),
    Column("last_name", String(50)),
    Column("full_name", String(100)),
    Column("phone", String(100)),
    Column("street", String(100)),
    Column("city", String(100)),
    Column("state", String(100)),
    Column("full_address", String(100)),
)

dim_employee = Table(
    "dim_employee",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("created", TIMESTAMP, server_default=text("CURRENT_TIMESTAMP")),
    Column(
        "last_updated",
        TIMESTAMP,
        server_default=text("CURRENT_TIMESTAMP"),
        onupdate=text("CURRENT_TIMESTAMP"),
    ),
    Column("first_name", String(50)),
    Column("last_name", String(50)),
    Column("full_name", String(100)),
)

dim_vehicle = Table(
    "dim_vehicle",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("created", TIMESTAMP, server_default=text("CURRENT_TIMESTAMP")),
    Column(
        "last_updated",
        TIMESTAMP,
        server_default=text("CURRENT_TIMESTAMP"),
        onupdate=text("CURRENT_TIMESTAMP"),
    ),
    Column("vin", String(100)),
    Column(
        "msrp_amount",
        DECIMAL,
        comment="Manufacturer suggest retail price amount. List Price.",
    ),
)
