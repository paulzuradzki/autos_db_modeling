<!--

classDiagram
class fact_inventory{
   *INTEGER id NOT NULL
   TIMESTAMP created
   INTEGER dim_vehicle_id
   BOOLEAN is_in_stock
   TIMESTAMP last_updated
}
class fact_sale_transactions{
   *INTEGER id NOT NULL
   TIMESTAMP created
   DECIMAL dealer_purchase_cost_amount
   INTEGER dealer_purchase_dim_vehicle_id
   INTEGER dealer_sale_dim_vehicle_id
   DECIMAL dealer_sale_price_amount
   INTEGER dim_customer_id
   INTEGER dim_discount_type_id
   INTEGER dim_employee_id
   INTEGER dim_transaction_notes_id
   BOOLEAN is_financed
   BOOLEAN is_trade_in
   TIMESTAMP last_updated
   DATE sale_date
   INTEGER transaction_id
}
class fact_customer_relations{
   *INTEGER id NOT NULL
   TIMESTAMP created
   INTEGER dim_customer_id
   DATE encounter_date
   TEXT encounter_notes
   BOOLEAN is_repeat_customer
   TIMESTAMP last_updated
}
class dim_customer{
   *INTEGER id NOT NULL
   VARCHAR<100> city
   VARCHAR<100> country
   TIMESTAMP created
   VARCHAR<50> first_name
   VARCHAR<500> full_address
   VARCHAR<100> full_name
   VARCHAR<50> last_name
   TIMESTAMP last_updated
   VARCHAR<10> middle_initial
   VARCHAR<100> phone
   VARCHAR<100> state
   VARCHAR<100> street_address
   VARCHAR<100> zip
}
class dim_employee{
   *INTEGER id NOT NULL
   TIMESTAMP created
   VARCHAR<50> first_name
   VARCHAR<100> full_name
   VARCHAR<50> last_name
   TIMESTAMP last_updated
}
class dim_discount_type{
   *INTEGER id NOT NULL
   TIMESTAMP created
   TIMESTAMP last_updated
   VARCHAR<20> name
}
class dim_vehicle{
   *INTEGER id NOT NULL
   TIMESTAMP created
   INTEGER dim_vehicle_model_id
   TIMESTAMP last_updated
   VARCHAR<100> vin
}
class dim_vehicle_model{
   *INTEGER id NOT NULL
   VARCHAR<20> color
   TIMESTAMP created
   VARCHAR<20> door_type
   VARCHAR<20> drive_train_type
   TIMESTAMP last_updated
   VARCHAR<20> make
   VARCHAR<20> model
   DECIMAL msrp_amount
   VARCHAR<100> trim
   VARCHAR<20> wheel_drive_type
   INTEGER year
}
class dim_transaction_notes{
   *INTEGER id NOT NULL
   TIMESTAMP created
   TIMESTAMP last_updated
   TEXT notes
}
dim_vehicle "0..1" -- "0..n" fact_inventory
dim_customer "0..1" -- "0..n" fact_sale_transactions
dim_discount_type "0..1" -- "0..n" fact_sale_transactions
dim_employee "0..1" -- "0..n" fact_sale_transactions
dim_vehicle "0..1" -- "0..n" fact_sale_transactions
dim_transaction_notes "0..1" -- "0..n" fact_sale_transactions
dim_vehicle "0..1" -- "0..n" fact_sale_transactions
dim_customer "0..1" -- "0..n" fact_customer_relations
dim_vehicle_model "0..1" -- "0..n" dim_vehicle

-->
![](https://mermaid.ink/img/Y2xhc3NEaWFncmFtCmNsYXNzIGZhY3RfaW52ZW50b3J5ewogICAqSU5URUdFUiBpZCBOT1QgTlVMTAogICBUSU1FU1RBTVAgY3JlYXRlZAogICBJTlRFR0VSIGRpbV92ZWhpY2xlX2lkCiAgIEJPT0xFQU4gaXNfaW5fc3RvY2sKICAgVElNRVNUQU1QIGxhc3RfdXBkYXRlZAp9CmNsYXNzIGZhY3Rfc2FsZV90cmFuc2FjdGlvbnN7CiAgICpJTlRFR0VSIGlkIE5PVCBOVUxMCiAgIFRJTUVTVEFNUCBjcmVhdGVkCiAgIERFQ0lNQUwgZGVhbGVyX3B1cmNoYXNlX2Nvc3RfYW1vdW50CiAgIElOVEVHRVIgZGVhbGVyX3B1cmNoYXNlX2RpbV92ZWhpY2xlX2lkCiAgIElOVEVHRVIgZGVhbGVyX3NhbGVfZGltX3ZlaGljbGVfaWQKICAgREVDSU1BTCBkZWFsZXJfc2FsZV9wcmljZV9hbW91bnQKICAgSU5URUdFUiBkaW1fY3VzdG9tZXJfaWQKICAgSU5URUdFUiBkaW1fZGlzY291bnRfdHlwZV9pZAogICBJTlRFR0VSIGRpbV9lbXBsb3llZV9pZAogICBJTlRFR0VSIGRpbV90cmFuc2FjdGlvbl9ub3Rlc19pZAogICBCT09MRUFOIGlzX2ZpbmFuY2VkCiAgIEJPT0xFQU4gaXNfdHJhZGVfaW4KICAgVElNRVNUQU1QIGxhc3RfdXBkYXRlZAogICBEQVRFIHNhbGVfZGF0ZQogICBJTlRFR0VSIHRyYW5zYWN0aW9uX2lkCn0KY2xhc3MgZmFjdF9jdXN0b21lcl9yZWxhdGlvbnN7CiAgICpJTlRFR0VSIGlkIE5PVCBOVUxMCiAgIFRJTUVTVEFNUCBjcmVhdGVkCiAgIElOVEVHRVIgZGltX2N1c3RvbWVyX2lkCiAgIERBVEUgZW5jb3VudGVyX2RhdGUKICAgVEVYVCBlbmNvdW50ZXJfbm90ZXMKICAgQk9PTEVBTiBpc19yZXBlYXRfY3VzdG9tZXIKICAgVElNRVNUQU1QIGxhc3RfdXBkYXRlZAp9CmNsYXNzIGRpbV9jdXN0b21lcnsKICAgKklOVEVHRVIgaWQgTk9UIE5VTEwKICAgVkFSQ0hBUjwxMDA-IGNpdHkKICAgVkFSQ0hBUjwxMDA-IGNvdW50cnkKICAgVElNRVNUQU1QIGNyZWF0ZWQKICAgVkFSQ0hBUjw1MD4gZmlyc3RfbmFtZQogICBWQVJDSEFSPDUwMD4gZnVsbF9hZGRyZXNzCiAgIFZBUkNIQVI8MTAwPiBmdWxsX25hbWUKICAgVkFSQ0hBUjw1MD4gbGFzdF9uYW1lCiAgIFRJTUVTVEFNUCBsYXN0X3VwZGF0ZWQKICAgVkFSQ0hBUjwxMD4gbWlkZGxlX2luaXRpYWwKICAgVkFSQ0hBUjwxMDA-IHBob25lCiAgIFZBUkNIQVI8MTAwPiBzdGF0ZQogICBWQVJDSEFSPDEwMD4gc3RyZWV0X2FkZHJlc3MKICAgVkFSQ0hBUjwxMDA-IHppcAp9CmNsYXNzIGRpbV9lbXBsb3llZXsKICAgKklOVEVHRVIgaWQgTk9UIE5VTEwKICAgVElNRVNUQU1QIGNyZWF0ZWQKICAgVkFSQ0hBUjw1MD4gZmlyc3RfbmFtZQogICBWQVJDSEFSPDEwMD4gZnVsbF9uYW1lCiAgIFZBUkNIQVI8NTA-IGxhc3RfbmFtZQogICBUSU1FU1RBTVAgbGFzdF91cGRhdGVkCn0KY2xhc3MgZGltX2Rpc2NvdW50X3R5cGV7CiAgICpJTlRFR0VSIGlkIE5PVCBOVUxMCiAgIFRJTUVTVEFNUCBjcmVhdGVkCiAgIFRJTUVTVEFNUCBsYXN0X3VwZGF0ZWQKICAgVkFSQ0hBUjwyMD4gbmFtZQp9CmNsYXNzIGRpbV92ZWhpY2xlewogICAqSU5URUdFUiBpZCBOT1QgTlVMTAogICBUSU1FU1RBTVAgY3JlYXRlZAogICBJTlRFR0VSIGRpbV92ZWhpY2xlX21vZGVsX2lkCiAgIFRJTUVTVEFNUCBsYXN0X3VwZGF0ZWQKICAgVkFSQ0hBUjwxMDA-IHZpbgp9CmNsYXNzIGRpbV92ZWhpY2xlX21vZGVsewogICAqSU5URUdFUiBpZCBOT1QgTlVMTAogICBWQVJDSEFSPDIwPiBjb2xvcgogICBUSU1FU1RBTVAgY3JlYXRlZAogICBWQVJDSEFSPDIwPiBkb29yX3R5cGUKICAgVkFSQ0hBUjwyMD4gZHJpdmVfdHJhaW5fdHlwZQogICBUSU1FU1RBTVAgbGFzdF91cGRhdGVkCiAgIFZBUkNIQVI8MjA-IG1ha2UKICAgVkFSQ0hBUjwyMD4gbW9kZWwKICAgREVDSU1BTCBtc3JwX2Ftb3VudAogICBWQVJDSEFSPDEwMD4gdHJpbQogICBWQVJDSEFSPDIwPiB3aGVlbF9kcml2ZV90eXBlCiAgIElOVEVHRVIgeWVhcgp9CmNsYXNzIGRpbV90cmFuc2FjdGlvbl9ub3Rlc3sKICAgKklOVEVHRVIgaWQgTk9UIE5VTEwKICAgVElNRVNUQU1QIGNyZWF0ZWQKICAgVElNRVNUQU1QIGxhc3RfdXBkYXRlZAogICBURVhUIG5vdGVzCn0KZGltX3ZlaGljbGUgIjAuLjEiIC0tICIwLi5uIiBmYWN0X2ludmVudG9yeQpkaW1fY3VzdG9tZXIgIjAuLjEiIC0tICIwLi5uIiBmYWN0X3NhbGVfdHJhbnNhY3Rpb25zCmRpbV9kaXNjb3VudF90eXBlICIwLi4xIiAtLSAiMC4ubiIgZmFjdF9zYWxlX3RyYW5zYWN0aW9ucwpkaW1fZW1wbG95ZWUgIjAuLjEiIC0tICIwLi5uIiBmYWN0X3NhbGVfdHJhbnNhY3Rpb25zCmRpbV92ZWhpY2xlICIwLi4xIiAtLSAiMC4ubiIgZmFjdF9zYWxlX3RyYW5zYWN0aW9ucwpkaW1fdHJhbnNhY3Rpb25fbm90ZXMgIjAuLjEiIC0tICIwLi5uIiBmYWN0X3NhbGVfdHJhbnNhY3Rpb25zCmRpbV92ZWhpY2xlICIwLi4xIiAtLSAiMC4ubiIgZmFjdF9zYWxlX3RyYW5zYWN0aW9ucwpkaW1fY3VzdG9tZXIgIjAuLjEiIC0tICIwLi5uIiBmYWN0X2N1c3RvbWVyX3JlbGF0aW9ucwpkaW1fdmVoaWNsZV9tb2RlbCAiMC4uMSIgLS0gIjAuLm4iIGRpbV92ZWhpY2xl)
