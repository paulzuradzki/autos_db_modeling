from sqlalchemy.orm import registry
from sqlalchemy import (
    BOOLEAN,
    DATE,
    TIMESTAMP,
    DECIMAL,
    TEXT,
    text,
    CheckConstraint,
    Column,
    ForeignKey,
    Integer,
    MetaData,
    String,
    Table,
)

metadata_obj = MetaData(schema="autos_etl")

fact_inventory = Table(
    "fact_inventory",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("created", TIMESTAMP, server_default=text("CURRENT_TIMESTAMP")),
    Column(
        "last_updated",
        TIMESTAMP,
        server_default=text("CURRENT_TIMESTAMP"),
        onupdate=text("CURRENT_TIMESTAMP"),
    ),
    Column("dim_vehicle_id", Integer, ForeignKey("dim_vehicle.id")),
    Column("is_in_stock", BOOLEAN),
    comment="Inventory table with a boolean flag to determine if a particular vehicle is in stock.",  # noqa
)

fact_sale_transactions = Table(
    "fact_sale_transactions",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("created", TIMESTAMP, server_default=text("CURRENT_TIMESTAMP")),
    Column(
        "last_updated",
        TIMESTAMP,
        server_default=text("CURRENT_TIMESTAMP"),
        onupdate=text("CURRENT_TIMESTAMP"),
    ),
    Column("dim_customer_id", Integer, ForeignKey("dim_customer.id")),
    Column("dim_vehicle_id", Integer, ForeignKey("dim_vehicle.id")),
    Column("dim_discount_type_id", Integer, ForeignKey("dim_discount_type.id")),
    Column("sale_date", DATE),
    Column("purchase_price_amount", DECIMAL),
    Column("is_trade_in", BOOLEAN),
    Column("trade_in_value_amount", DECIMAL),
    comment="Sale transactions table to caputure the event of a vehicle sale and measures like purchase price amount.",  # noqa
)

fact_customer_relations = Table(
    "fact_customer_relations",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("created", TIMESTAMP, server_default=text("CURRENT_TIMESTAMP")),
    Column(
        "last_updated",
        TIMESTAMP,
        server_default=text("CURRENT_TIMESTAMP"),
        onupdate=text("CURRENT_TIMESTAMP"),
    ),
    Column("dim_customer_id", Integer, ForeignKey("dim_customer.id")),
    Column("encounter_date", DATE, comment="Date of customer encounter."),
    Column(
        "encounter_notes",
        TEXT,
        comment="Notes for a given encounter with a customer.",
    ),
    comment="Track customer relation encounters and notes. An individual customer may have multiple notes and encounters.",  # noqa
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
    Column("created", TIMESTAMP, server_default=text("CURRENT_TIMESTAMP")),
    Column(
        "last_updated",
        TIMESTAMP,
        server_default=text("CURRENT_TIMESTAMP"),
        onupdate=text("CURRENT_TIMESTAMP"),
    ),
    Column("name", String(20)),
    CheckConstraint(
        f"name IN {tuple(DISCOUNT_TYPE_CHOICES)}", name="valid_discount_type"
    ),
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
    Column("dim_vehicle_model_id", Integer, ForeignKey("dim_vehicle_model.id")),
)

dim_vehicle_model = Table(
    "dim_vehicle_model",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("created", TIMESTAMP, server_default=text("CURRENT_TIMESTAMP")),
    Column(
        "last_updated",
        TIMESTAMP,
        server_default=text("CURRENT_TIMESTAMP"),
        onupdate=text("CURRENT_TIMESTAMP"),
    ),
    Column("year", Integer),
    Column("make", String(20)),
    Column("model", String(20)),
    Column("trim", String(100)),
    Column("wheel_drive_type", String(20)),
    Column("color", String(20)),
    Column("door_type", String(20)),
    Column("drive_train_type", String(20)),
    Column(
        "msrp_amount",
        DECIMAL,
        comment="Manufacturer suggest retail price amount. List Price.",
    ),
)


class Vehicle:
    def __repr__(self):
        fields = ", ".join(
            f"{key}={getattr(self, key)}" for key in self.__table__.c.keys()
        )
        return f"<{self.__class__.__name__}({fields})>"


class VehicleModel:
    def __repr__(self):
        fields = ", ".join(
            f"{key}={getattr(self, key)}" for key in self.__table__.c.keys()
        )
        return f"<{self.__class__.__name__}({fields})>"


# SQLAlchemy v2.0+ style
mapper_registry = registry()
_ = mapper_registry.map_imperatively(Vehicle, dim_vehicle)
_ = mapper_registry.map_imperatively(VehicleModel, dim_vehicle_model)
