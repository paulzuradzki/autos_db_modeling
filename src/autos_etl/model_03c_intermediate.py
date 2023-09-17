from sqlalchemy import (
    BOOLEAN,
    DATE,
    TIMESTAMP,
    DECIMAL,
    text,
    Column,
    ForeignKey,
    Integer,
    MetaData,
    Table,
)


# For ERAlchemy2. No schema supportin ERD creation from Python/SQLAlchemy.
# metadata_obj = MetaData(schema="autos_etl")
metadata_obj = MetaData()

fact_sale_transactions_dealer_01 = Table(
    "fact_sale_transactions_dealer_01",
    metadata_obj,
    Column("id", Integer, primary_key=True, comment="Unique ID. Primary key."),  # noqa
    Column(
        "created",
        TIMESTAMP,
        server_default=text("CURRENT_TIMESTAMP"),
        comment="Datetime stamp for when the record was created.",
    ),  # noqa
    Column(
        "last_updated",
        TIMESTAMP,
        server_default=text("CURRENT_TIMESTAMP"),
        onupdate=text("CURRENT_TIMESTAMP"),
        comment="Datetime stamp for when the record was last updated.",
    ),  # noqa
    Column(
        "dim_customer_id",
        Integer,
        ForeignKey("dim_customer.id"),
        comment="Customer ID for joining to customer dimensions.",
    ),  # noqa
    Column(
        "dim_vehicle_id",
        Integer,
        ForeignKey("dim_vehicle.id"),
        comment="Vehicel ID for joining to vehicle dimensions.",
    ),  # noqa
    Column(
        "dim_discount_type_id",
        Integer,
        ForeignKey("dim_discount_type.id"),
        comment="Discount type ID for joining to discount description dimension.",
    ),  # noqa
    Column("sale_date", DATE, comment="Date of sale."),
    Column("purchase_price_amount", DECIMAL, comment="Purchase price amount."),
    Column(
        "is_trade_in",
        BOOLEAN,
        comment="True if trade-in vehicle was sold on the transaction. False otherwise.",
    ),  # noqa
    Column("trade_in_value_amount", DECIMAL, comment="Value of trade-in vehicle."),
    comment="Sale transactions table to caputure the event of a vehicle sale and measures like purchase price amount.",  # noqa
)

fact_transaction_dealer_02 = Table(
    "fact_transaction_dealer_02",
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


fact_sale_transactions_integrated = Table(
    "fact_sale_transactions_integrated",
    metadata_obj,
    Column("id", Integer, primary_key=True, comment="Unique ID. Primary key."),  # noqa
    Column(
        "transaction_id",
        Integer,
        comment="External system transaction ID (pre-owned dealer).",
    ),  # noqa
    Column(
        "created",
        TIMESTAMP,
        server_default=text("CURRENT_TIMESTAMP"),
        comment="Datetime stamp for when the record was created.",
    ),  # noqa
    Column(
        "last_updated",
        TIMESTAMP,
        server_default=text("CURRENT_TIMESTAMP"),
        onupdate=text("CURRENT_TIMESTAMP"),
        comment="Datetime stamp for when the record was last updated.",
    ),  # noqa
    Column(
        "dim_customer_id",
        Integer,
        ForeignKey("dim_customer.id"),
        comment="Customer ID for joining to customer dimensions.",
    ),  # noqa
    Column(
        "dim_employee_id",
        ForeignKey("dim_employee.id"),
        comment="Employee ID.",
    ),
    Column(
        "dim_vehicle_id",
        Integer,
        ForeignKey("dim_vehicle.id"),
        comment="Vehicel ID for joining to vehicle dimensions.",
    ),  # noqa
    Column(
        "dim_discount_type_id",
        Integer,
        ForeignKey("dim_discount_type.id"),
        comment="Discount type ID for joining to discount description dimension.",
    ),  # noqa
    Column("sale_date", DATE, comment="Date of sale."),
    Column("purchase_price_amount", DECIMAL, comment="Purchase price amount."),
    Column(
        "is_trade_in",
        BOOLEAN,
        comment="True if trade-in vehicle was sold on the transaction. False otherwise.",
    ),  # noqa
    Column("trade_in_value_amount", DECIMAL, comment="Value of trade-in vehicle."),
    comment="Sale transactions table to caputure the event of a vehicle sale and measures like purchase price amount.",  # noqa
)
