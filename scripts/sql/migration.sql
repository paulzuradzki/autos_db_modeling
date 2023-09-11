BEGIN;

CREATE TABLE alembic_version (
    version_num VARCHAR(32) NOT NULL, 
    CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);

-- Running upgrade  -> 0d783cb99fa3

CREATE TABLE autos_etl.dim_customer (
    id SERIAL NOT NULL, 
    created TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP, 
    last_updated TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP, 
    first_name VARCHAR(50), 
    last_name VARCHAR(50), 
    middle_initial VARCHAR(10), 
    address VARCHAR(100), 
    city VARCHAR(100), 
    state VARCHAR(100), 
    country VARCHAR(100), 
    is_repeat_customer BOOLEAN, 
    PRIMARY KEY (id)
);

COMMENT ON TABLE autos_etl.dim_customer IS 'Customer dimension table.';

COMMENT ON COLUMN autos_etl.dim_customer.id IS 'Unique ID. Primary key.';

COMMENT ON COLUMN autos_etl.dim_customer.created IS 'Datetime stamp for when the record was created.';

COMMENT ON COLUMN autos_etl.dim_customer.last_updated IS 'Datetime stamp for when the record was last updated.';

COMMENT ON COLUMN autos_etl.dim_customer.first_name IS 'Customer first name.';

COMMENT ON COLUMN autos_etl.dim_customer.last_name IS 'Customer last name.';

COMMENT ON COLUMN autos_etl.dim_customer.middle_initial IS 'Customer middle initial.';

COMMENT ON COLUMN autos_etl.dim_customer.address IS 'Customer street address.';

COMMENT ON COLUMN autos_etl.dim_customer.city IS 'Customer address city.';

COMMENT ON COLUMN autos_etl.dim_customer.state IS 'Customer address state.';

COMMENT ON COLUMN autos_etl.dim_customer.country IS 'Customer address country.';

COMMENT ON COLUMN autos_etl.dim_customer.is_repeat_customer IS 'True if customer is a repeat customer. Otherwise, False.';

CREATE TABLE autos_etl.dim_discount_type (
    id SERIAL NOT NULL, 
    created TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP, 
    last_updated TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP, 
    name VARCHAR(20), 
    PRIMARY KEY (id), 
    CONSTRAINT valid_discount_type CHECK (name IN ('N/A', 'EndofYear', 'First Time Driver', 'Repeat Customer', 'Senior Citizen'))
);

COMMENT ON TABLE autos_etl.dim_discount_type IS 'Discount type mapping table.';

COMMENT ON COLUMN autos_etl.dim_discount_type.id IS 'Unique ID. Primary key.';

COMMENT ON COLUMN autos_etl.dim_discount_type.created IS 'Datetime stamp for when the record was created.';

COMMENT ON COLUMN autos_etl.dim_discount_type.last_updated IS 'Datetime stamp for when the record was last updated.';

COMMENT ON COLUMN autos_etl.dim_discount_type.name IS 'Description of discount type. Constrained to N/A,EndofYear,First Time Driver,Repeat Customer,Senior Citizen.';

CREATE TABLE autos_etl.dim_vehicle_model (
    id SERIAL NOT NULL, 
    created TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP, 
    last_updated TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP, 
    year INTEGER, 
    make VARCHAR(20), 
    model VARCHAR(20), 
    trim VARCHAR(100), 
    wheel_drive_type VARCHAR(20), 
    color VARCHAR(20), 
    door_type VARCHAR(20), 
    drive_train_type VARCHAR(20), 
    msrp_amount DECIMAL, 
    PRIMARY KEY (id)
);

COMMENT ON TABLE autos_etl.dim_vehicle_model IS 'Vehicle model dimensions for details such as year, make, model, trim, color, and more.';

COMMENT ON COLUMN autos_etl.dim_vehicle_model.id IS 'Unique ID. Primary key.';

COMMENT ON COLUMN autos_etl.dim_vehicle_model.created IS 'Datetime stamp for when the record was created.';

COMMENT ON COLUMN autos_etl.dim_vehicle_model.last_updated IS 'Datetime stamp for when the record was last updated.';

COMMENT ON COLUMN autos_etl.dim_vehicle_model.year IS 'Vehicle model year.';

COMMENT ON COLUMN autos_etl.dim_vehicle_model.make IS 'Vehical model make (A.K.A., manufacturer; ex: ''Nissan'').';

COMMENT ON COLUMN autos_etl.dim_vehicle_model.model IS 'Vehicel model (ex: ''Altima'')';

COMMENT ON COLUMN autos_etl.dim_vehicle_model.trim IS 'Vehicle model trim (ex: ''Hatchback'')';

COMMENT ON COLUMN autos_etl.dim_vehicle_model.wheel_drive_type IS 'Vehicle model wheel drive type. E.g., 4-wheel drive or all-wheel drive.';

COMMENT ON COLUMN autos_etl.dim_vehicle_model.color IS 'Vehicle model color.';

COMMENT ON COLUMN autos_etl.dim_vehicle_model.door_type IS 'Vehicle model door type.';

COMMENT ON COLUMN autos_etl.dim_vehicle_model.drive_train_type IS 'Vehicle model drivetrain type.';

COMMENT ON COLUMN autos_etl.dim_vehicle_model.msrp_amount IS 'Manufacturer suggest retail price amount. List Price.';

CREATE TABLE autos_etl.dim_vehicle (
    id SERIAL NOT NULL, 
    created TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP, 
    last_updated TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP, 
    vin VARCHAR(100), 
    dim_vehicle_model_id INTEGER, 
    PRIMARY KEY (id), 
    FOREIGN KEY(dim_vehicle_model_id) REFERENCES autos_etl.dim_vehicle_model (id)
);

COMMENT ON TABLE autos_etl.dim_vehicle IS 'Unique list of VINs. Vehicle dimension table mapping to ''Vehicle Model'' dimension. From ''vin'' to ''dim_vehicle_model.id''. Multiple VINs may be associated with the same vehicle model.';

COMMENT ON COLUMN autos_etl.dim_vehicle.id IS 'Unique ID. Primary key.';

COMMENT ON COLUMN autos_etl.dim_vehicle.created IS 'Datetime stamp for when the record was created.';

COMMENT ON COLUMN autos_etl.dim_vehicle.last_updated IS 'Datetime stamp for when the record was last updated.';

COMMENT ON COLUMN autos_etl.dim_vehicle.vin IS 'Vehicle Identification Number';

COMMENT ON COLUMN autos_etl.dim_vehicle.dim_vehicle_model_id IS 'Vehicle Model ID for joining to vehicle model detail dimensions.';

CREATE TABLE autos_etl.fact_customer_relations (
    id SERIAL NOT NULL, 
    created TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP, 
    last_updated TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP, 
    dim_customer_id INTEGER, 
    encounter_date DATE, 
    encounter_notes TEXT, 
    PRIMARY KEY (id), 
    FOREIGN KEY(dim_customer_id) REFERENCES autos_etl.dim_customer (id)
);

COMMENT ON TABLE autos_etl.fact_customer_relations IS 'Track customer relation encounters and notes. An individual customer may have multiple notes and encounters.';

COMMENT ON COLUMN autos_etl.fact_customer_relations.id IS 'Unique ID. Primary key.';

COMMENT ON COLUMN autos_etl.fact_customer_relations.created IS 'Datetime stamp for when the record was created.';

COMMENT ON COLUMN autos_etl.fact_customer_relations.last_updated IS 'Datetime stamp for when the record was last updated.';

COMMENT ON COLUMN autos_etl.fact_customer_relations.dim_customer_id IS 'Customer ID for joining to customer dimension.';

COMMENT ON COLUMN autos_etl.fact_customer_relations.encounter_date IS 'Date of customer encounter.';

COMMENT ON COLUMN autos_etl.fact_customer_relations.encounter_notes IS 'Notes for a given encounter with a customer.';

CREATE TABLE autos_etl.fact_inventory (
    id SERIAL NOT NULL, 
    created TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP, 
    last_updated TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP, 
    dim_vehicle_id INTEGER, 
    is_in_stock BOOLEAN, 
    PRIMARY KEY (id), 
    FOREIGN KEY(dim_vehicle_id) REFERENCES autos_etl.dim_vehicle (id)
);

COMMENT ON TABLE autos_etl.fact_inventory IS 'Inventory table with a boolean flag to determine if a particular vehicle is in stock.';

COMMENT ON COLUMN autos_etl.fact_inventory.id IS 'Unique ID. Primary key.';

COMMENT ON COLUMN autos_etl.fact_inventory.created IS 'Datetime stamp for when the record was created.';

COMMENT ON COLUMN autos_etl.fact_inventory.last_updated IS 'Datetime stamp for when the record was last updated.';

COMMENT ON COLUMN autos_etl.fact_inventory.dim_vehicle_id IS 'Vehicle ID for join to vehicle/VIN and vehicle model detail dimensions.';

COMMENT ON COLUMN autos_etl.fact_inventory.is_in_stock IS 'True/False for whether vehicle is in stock.';

CREATE TABLE autos_etl.fact_sale_transactions (
    id SERIAL NOT NULL, 
    created TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP, 
    last_updated TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP, 
    dim_customer_id INTEGER, 
    dim_vehicle_id INTEGER, 
    dim_discount_type_id INTEGER, 
    sale_date DATE, 
    purchase_price_amount DECIMAL, 
    is_trade_in BOOLEAN, 
    trade_in_value_amount DECIMAL, 
    PRIMARY KEY (id), 
    FOREIGN KEY(dim_customer_id) REFERENCES autos_etl.dim_customer (id), 
    FOREIGN KEY(dim_discount_type_id) REFERENCES autos_etl.dim_discount_type (id), 
    FOREIGN KEY(dim_vehicle_id) REFERENCES autos_etl.dim_vehicle (id)
);

COMMENT ON TABLE autos_etl.fact_sale_transactions IS 'Sale transactions table to caputure the event of a vehicle sale and measures like purchase price amount.';

COMMENT ON COLUMN autos_etl.fact_sale_transactions.id IS 'Unique ID. Primary key.';

COMMENT ON COLUMN autos_etl.fact_sale_transactions.created IS 'Datetime stamp for when the record was created.';

COMMENT ON COLUMN autos_etl.fact_sale_transactions.last_updated IS 'Datetime stamp for when the record was last updated.';

COMMENT ON COLUMN autos_etl.fact_sale_transactions.dim_customer_id IS 'Customer ID for joining to customer dimensions.';

COMMENT ON COLUMN autos_etl.fact_sale_transactions.dim_vehicle_id IS 'Vehicel ID for joining to vehicle dimensions.';

COMMENT ON COLUMN autos_etl.fact_sale_transactions.dim_discount_type_id IS 'Discount type ID for joining to discount description dimension.';

COMMENT ON COLUMN autos_etl.fact_sale_transactions.sale_date IS 'Date of sale.';

COMMENT ON COLUMN autos_etl.fact_sale_transactions.purchase_price_amount IS 'Purchase price amount.';

COMMENT ON COLUMN autos_etl.fact_sale_transactions.is_trade_in IS 'True if trade-in vehicle was sold on the transaction. False otherwise.';

COMMENT ON COLUMN autos_etl.fact_sale_transactions.trade_in_value_amount IS 'Value of trade-in vehicle.';

INSERT INTO alembic_version (version_num) VALUES ('0d783cb99fa3') RETURNING alembic_version.version_num;

COMMIT;

