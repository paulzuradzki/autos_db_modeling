from sqlalchemy import (
    BOOLEAN,
    DATE,
    DECIMAL,
    TEXT,
    TIMESTAMP,
    CheckConstraint,
    Column,
    ForeignKey,
    Integer,
    MetaData,
    String,
    Table,
    Text,
    text,
)

# For ERAlchemy2. No schema supportin ERD creation from Python/SQLAlchemy.
# metadata_obj = MetaData(schema="autos_etl")
metadata_obj = MetaData()

fact_inventory = Table(
    "fact_inventory",
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
        "dim_vehicle_id",
        Integer,
        ForeignKey("dim_vehicle.id"),
        comment="Vehicle ID for join to vehicle/VIN and vehicle model detail dimensions.",
    ),  # noqa
    Column(
        "is_in_stock", BOOLEAN, comment="True/False for whether vehicle is in stock."
    ),
    comment="Inventory table with a boolean flag to determine if a particular vehicle is in stock.",  # noqa
)

fact_sale_transactions = Table(
    "fact_sale_transactions",
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
        "dealer_purchase_dim_vehicle_id",
        ForeignKey("dim_vehicle.id"),
        comment="Vehicle ID of the vehicle purchased by the dealer (e.g., from a supplier or trade-in customer.)",  # noqa
    ),
    Column(
        "dealer_sale_dim_vehicle_id",
        ForeignKey("dim_vehicle.id"),
        comment="Vehicle ID of the vehicle sold by the dealer (e.g., to a supplier or individual customer.)", # noqa
    ),
    Column(
        "dim_discount_type_id",
        Integer,
        ForeignKey("dim_discount_type.id"),
        comment="Discount type ID for joining to discount description dimension.",
    ),  # noqa
    Column("dim_transaction_notes_id", ForeignKey("dim_transaction_notes.id")),
    Column("sale_date", DATE, comment="Date of sale."),
    Column("dealer_sale_price_amount", DECIMAL),
    Column("dealer_purchase_cost_amount", DECIMAL),
    Column(
        "is_trade_in",
        BOOLEAN,
        comment="True if trade-in vehicle was sold on the transaction. False otherwise.",
    ),
    Column(
        "is_financed",
        BOOLEAN,
        comment="True if financing was given.",
    ),    
    # Column("trade_in_value_amount", DECIMAL, comment="Value of trade-in vehicle."),
    comment="Sale transactions table to caputure the event of a vehicle sale and measures like purchase price amount.",  # noqa
)
fact_customer_relations = Table(
    "fact_customer_relations",
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
        comment="Customer ID for joining to customer dimension.",
    ),  # noqa
    Column("encounter_date", DATE, comment="Date of customer encounter."),
    Column(
        "encounter_notes",
        TEXT,
        comment="Notes for a given encounter with a customer.",
    ),
    Column(
        "is_repeat_customer",
        BOOLEAN,
        comment="True if customer is a repeat customer. Otherwise, False.",
    ),  # noqa
    comment="Track customer relation encounters and notes. An individual customer may have multiple notes and encounters.",  # noqa
)

dim_customer = Table(
    "dim_customer",
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
    Column("first_name", String(50), comment="Customer first name."),  # noqa
    Column("last_name", String(50), comment="Customer last name."),  # noqa
    Column("full_name", String(100)),
    Column("middle_initial", String(10), comment="Customer middle initial."),  # noqa
    Column("phone", String(100)),
    Column("street_address", String(100), comment="Customer street address."),  # noqa
    Column("city", String(100), comment="Customer address city."),  # noqa
    Column("state", String(100), comment="Customer address state."),  # noqa
    Column("zip", String(100), comment="Customer address zip code."),  # noqa
    Column("country", String(100), comment="Customer address country."),  # noqa
    Column(
        "full_address",
        String(500),
        comment="Customer full address in format: <street_address> <city>, <state> <zip>",
    ),  # noqa
    comment="Customer dimension table.",  # noqa
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

DISCOUNT_TYPE_CHOICES = [
    "N/A",
    "EndofYear",
    "First Time Driver",
    "Repeat Customer",
    "Senior Citizen",
]
dim_discount_type = Table(
    "dim_discount_type",
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
        "name",
        String(20),
        comment=f"Description of discount type. Constrained to {','.join(DISCOUNT_TYPE_CHOICES)}.",
    ),  # noqa
    CheckConstraint(
        f"name IN {tuple(DISCOUNT_TYPE_CHOICES)}", name="valid_discount_type"
    ),
    comment="Discount type mapping table.",  # noqa
)

dim_vehicle = Table(
    "dim_vehicle",
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
        ForeignKey("dim_vehicle_model.id"),
        comment="Vehicle Model ID for joining to vehicle model detail dimensions.",
    ),  # noqa
    comment="Unique list of VINs. Vehicle dimension table mapping to 'Vehicle Model' dimension. From 'vin' to 'dim_vehicle_model.id'. Multiple VINs may be associated with the same vehicle model.",  # noqa
)

dim_vehicle_model = Table(
    "dim_vehicle_model",
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

dim_transaction_notes = Table(
    "dim_transaction_notes",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("created", TIMESTAMP, server_default=text("CURRENT_TIMESTAMP")),
    Column(
        "last_updated",
        TIMESTAMP,
        server_default=text("CURRENT_TIMESTAMP"),
        onupdate=text("CURRENT_TIMESTAMP"),
    ),
    Column("notes", Text, comment="Transaction notes."),
)
