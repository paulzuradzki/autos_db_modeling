/* See available tables */
select
    *
from
    information_schema."tables"
where
    table_schema = 'autos_etl'
order by
    table_name;

/* Preview tables */
select * from autos_etl.fact_inventory;
select * from autos_etl.dim_vehicle_model;
select * from autos_etl.dim_vehicle;
select * from autos_etl.dim_customer;
select * from autos_etl.dim_discount_type;
select * from autos_etl.fact_customer_relations;
select * from autos_etl.fact_sale_transactions;
select * from autos_etl.alembic_version;

/* Sample join */
select
    *
from
    autos_etl.dim_vehicle dv
    left join autos_etl.dim_vehicle_model dvh on dv.dim_vehicle_model_id = dvh.id
order by
    dv.id;

/* Test updates and last_updated field */
update
    autos_etl.fact_inventory
set
    is_in_stock = false;

select
    *
from
    autos_etl.fact_inventory
order by
    id;

/* We need to set last_update to current_stamp manually if we use raw SQL to update records */
/* In an ORM, we get this behavior for free once it's defined in the Python/ORM schema. */
update
    autos_etl.fact_inventory
set
    is_in_stock = true,
    last_updated = current_timestamp;

select
    *
from
    autos_etl.fact_inventory
order by
    id;