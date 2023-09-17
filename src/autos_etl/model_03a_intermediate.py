from sqlalchemy import (
    BOOLEAN,
    TIMESTAMP,
    Column,
    Integer,
    MetaData,
    String,
    Table,
    text,
)

# metadata_obj = MetaData(schema="autos_etl")
# For ERAlchemy2. No schema supportin ERD creation from Python/SQLAlchemy.
metadata_obj = MetaData()


dim_customer_dealer_01 = Table(
    "dim_customer_dealer_01",
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
    Column("middle_initial", String(10), comment="Customer middle initial."),  # noqa
    Column("address", String(100), comment="Customer street address."),  # noqa
    Column("city", String(100), comment="Customer address city."),  # noqa
    Column("state", String(100), comment="Customer address state."),  # noqa
    Column("country", String(100), comment="Customer address country."),  # noqa
    Column(
        "is_repeat_customer",
        BOOLEAN,
        comment="True if customer is a repeat customer. Otherwise, False.",
    ),  # noqa
    comment="Customer dimension table.",  # noqa
)

dim_customer_dealer_02 = Table(
    "dim_customer_dealer_02",
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

dim_customer_integrated = Table(
    "dim_customer_integrated",
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
    # Column(
    #     "is_repeat_customer",
    #     BOOLEAN,
    #     comment="True if customer is a repeat customer. Otherwise, False.",
    # ),  # noqa
    comment="Customer dimension table.",  # noqa
)
