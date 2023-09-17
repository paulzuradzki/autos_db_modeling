from sqlalchemy import (
    TIMESTAMP,
    DECIMAL,
    text,
    Column,
    ForeignKey,
    Integer,
    MetaData,
    String,
    Table,
)

# For ERAlchemy2. No schema supportin ERD creation from Python/SQLAlchemy.
# metadata_obj = MetaData(schema="autos_etl")
metadata_obj = MetaData()

dim_vehicle_dealer_01 = Table(
    "dim_vehicle_dealer_01",
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
    Column("vin", String(100), comment="Vehicle Identification Number"),  # noqa
    Column(
        "dim_vehicle_model_id",
        Integer,
        ForeignKey("dim_vehicle_model_dealer_01.id"),
        comment="Vehicle Model ID for joining to vehicle model detail dimensions.",
    ),  # noqa
    comment="Unique list of VINs. Vehicle dimension table mapping to 'Vehicle Model' dimension. From 'vin' to 'dim_vehicle_model.id'. Multiple VINs may be associated with the same vehicle model.",  # noqa
)


dim_vehicle_model_dealer_01 = Table(
    "dim_vehicle_model_dealer_01",
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
    Column("year", Integer, comment="Vehicle model year."),  # noqa
    Column(
        "make",
        String(20),
        comment="Vehical model make (A.K.A., manufacturer; ex: 'Nissan').",
    ),  # noqa
    Column("model", String(20), comment="Vehicel model (ex: 'Altima')"),  # noqa
    Column("trim", String(100), comment="Vehicle model trim (ex: 'Hatchback')"),  # noqa
    Column(
        "wheel_drive_type",
        String(20),
        comment="Vehicle model wheel drive type. E.g., 4-wheel drive or all-wheel drive.",
    ),  # noqa
    Column("color", String(20), comment="Vehicle model color."),  # noqa
    Column("door_type", String(20), comment="Vehicle model door type."),  # noqa
    Column(
        "drive_train_type", String(20), comment="Vehicle model drivetrain type."
    ),  # noqa
    Column(
        "msrp_amount",
        DECIMAL,
        comment="Manufacturer suggest retail price amount. List Price.",
    ),
    comment="Vehicle model dimensions for details such as year, make, model, trim, color, and more.",  # noqa
)

dim_vehicle_dealer_02 = Table(
    "dim_vehicle_dealer_02",
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

dim_vehicle_dealer_integrated = Table(
    "dim_vehicle_dealer_integrated",
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
    Column("vin", String(100), comment="Vehicle Identification Number"),  # noqa
    Column(
        "dim_vehicle_model_id",
        Integer,
        ForeignKey("dim_vehicle_model_integrated.id"),
        comment="Vehicle Model ID for joining to vehicle model detail dimensions.",
    ),  # noqa
    comment="Unique list of VINs. Vehicle dimension table mapping to 'Vehicle Model' dimension. From 'vin' to 'dim_vehicle_model.id'. Multiple VINs may be associated with the same vehicle model.",  # noqa
)


dim_vehicle_model_integrated = Table(
    "dim_vehicle_model_integrated",
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
    Column("year", Integer, comment="Vehicle model year."),  # noqa
    Column(
        "make",
        String(20),
        comment="Vehical model make (A.K.A., manufacturer; ex: 'Nissan').",
    ),  # noqa
    Column("model", String(20), comment="Vehicel model (ex: 'Altima')"),  # noqa
    Column("trim", String(100), comment="Vehicle model trim (ex: 'Hatchback')"),  # noqa
    Column(
        "wheel_drive_type",
        String(20),
        comment="Vehicle model wheel drive type. E.g., 4-wheel drive or all-wheel drive.",
    ),  # noqa
    Column("color", String(20), comment="Vehicle model color."),  # noqa
    Column("door_type", String(20), comment="Vehicle model door type."),  # noqa
    Column(
        "drive_train_type", String(20), comment="Vehicle model drivetrain type."
    ),  # noqa
    Column(
        "msrp_amount",
        DECIMAL,
        comment="Manufacturer suggest retail price amount. List Price.",
    ),
    comment="Vehicle model dimensions for details such as year, make, model, trim, color, and more.",  # noqa
)
