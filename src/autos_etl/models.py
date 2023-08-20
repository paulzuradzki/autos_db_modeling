from sqlalchemy import (
    BOOLEAN,
    DATE,
    DATETIME,
    DECIMAL,
    TEXT,
    CheckConstraint,
    Column,
    ForeignKey,
    Integer,
    MetaData,
    String,
    Table,
)
from sqlalchemy.sql.functions import now

metadata_obj = MetaData()

fact_inventory = Table(
    "fact_inventory",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("created", DATETIME, default=now),
    Column("last_updated", DATETIME, onupdate=now),
    Column("dim_vehicle_id", Integer, ForeignKey("dim_vehicle.id")),
    Column("is_in_stock", BOOLEAN),
)

fact_sale_transactions = Table(
    "fact_sale_transactions",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("created", DATETIME, default=now),
    Column("last_updated", DATETIME, onupdate=now),
    Column("dim_customer_id", Integer, ForeignKey("dim_customer.id")),
    Column("dim_vehicle_id", Integer, ForeignKey("dim_vehicle.id")),
    Column("dim_discount_type_id", Integer, ForeignKey("dim_discount_type.id")),
    Column("sale_date", DATE),
    Column("purchase_price_amount", DECIMAL),
    Column("is_trade_in", BOOLEAN),
    Column("trade_in_value_amount", DECIMAL),
)

fact_customer_relations = Table(
    "fact_customer_relations",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("created", DATETIME, default=now),
    Column("last_updated", DATETIME, onupdate=now),
    Column("dim_customer_id", Integer, ForeignKey("dim_customer.id")),
    Column("encounter_date", DATE, comment="Date of customer encounter."),
    Column(
        "encounter_notes",
        TEXT,
        comment="Notes for a given encounter with a customer. A customer may have multiple encounters.",  # noqa
    ),
)

dim_customer = Table(
    "dim_customer",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("created", DATETIME, default=now),
    Column("last_updated", DATETIME, onupdate=now),
    Column("first_name", String(50)),
    Column("last_name", String(50)),
    Column("address", String(100)),
    Column("is_repeat_customer", BOOLEAN),
)

DISCOUNT_TYPE_CHOICES = {
    "N/A",
    "EndofYear",
    "First Time Driver",
    "Repeat Customer",
    "Senior Citizen",
}
dim_discount_type = Table(
    "dim_discount_type",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("created", DATETIME, default=now),
    Column("last_updated", DATETIME, onupdate=now),
    Column("name", String(20)),
    CheckConstraint(
        f"name IN {tuple(DISCOUNT_TYPE_CHOICES)}", name="valid_discount_type"
    ),
)

dim_vehicle = Table(
    "dim_vehicle",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("created", DATETIME, default=now),
    Column("last_updated", DATETIME, onupdate=now),
    Column("vin", String(100)),
    Column("dim_vehicle_model_id", Integer, ForeignKey("dim_vehicle_model.id")),
)

dim_vehicle_model = Table(
    "dim_vehicle_model",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("created", DATETIME, default=now),
    Column("last_updated", DATETIME, onupdate=now),
    Column("year", Integer),
    Column("make", String(20)),
    Column("model", String(20)),
    Column("trim", String(100)),
    Column("wheel_drive_type", String(20)),
    Column("color", String(20)),
    Column("drive_train_type", String(20)),
    Column(
        "msrp_amount",
        DECIMAL,
        comment="Manufacturer suggest retail price amount. List Price.",
    ),
)
