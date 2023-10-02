<!--

classDiagram
class fact_transaction{
   *INTEGER id NOT NULL
   TIMESTAMP created
   DECIMAL dealer_purchase_cost_amount
   INTEGER dealer_purchase_dim_vehicle_id
   INTEGER dealer_sale_dim_vehicle_id
   DECIMAL dealer_sale_price_amount
   INTEGER dim_customer_id
   INTEGER dim_employee_id
   INTEGER dim_transaction_notes_id
   BOOLEAN is_financed
   BOOLEAN is_trade_in
   TIMESTAMP last_updated
   DATE sale_date
   INTEGER transaction_id
}
class dim_customer{
   *INTEGER id NOT NULL
   VARCHAR<100> city
   TIMESTAMP created
   VARCHAR<50> first_name
   VARCHAR<100> full_address
   VARCHAR<100> full_name
   VARCHAR<50> last_name
   TIMESTAMP last_updated
   VARCHAR<100> phone
   VARCHAR<100> state
   VARCHAR<100> street
}
class dim_employee{
   *INTEGER id NOT NULL
   TIMESTAMP created
   VARCHAR<50> first_name
   VARCHAR<100> full_name
   VARCHAR<50> last_name
   TIMESTAMP last_updated
}
class dim_vehicle{
   *INTEGER id NOT NULL
   TIMESTAMP created
   TIMESTAMP last_updated
   DECIMAL msrp_amount
   VARCHAR<100> vin
}
class dim_transaction_notes{
   *INTEGER id NOT NULL
   TIMESTAMP created
   TIMESTAMP last_updated
   TEXT notes
}
dim_vehicle "0..1" -- "0..n" fact_transaction
dim_employee "0..1" -- "0..n" fact_transaction
dim_transaction_notes "0..1" -- "0..n" fact_transaction
dim_vehicle "0..1" -- "0..n" fact_transaction
dim_customer "0..1" -- "0..n" fact_transaction

-->
![](https://mermaid.ink/img/Y2xhc3NEaWFncmFtCmNsYXNzIGZhY3RfdHJhbnNhY3Rpb257CiAgICpJTlRFR0VSIGlkIE5PVCBOVUxMCiAgIFRJTUVTVEFNUCBjcmVhdGVkCiAgIERFQ0lNQUwgZGVhbGVyX3B1cmNoYXNlX2Nvc3RfYW1vdW50CiAgIElOVEVHRVIgZGVhbGVyX3B1cmNoYXNlX2RpbV92ZWhpY2xlX2lkCiAgIElOVEVHRVIgZGVhbGVyX3NhbGVfZGltX3ZlaGljbGVfaWQKICAgREVDSU1BTCBkZWFsZXJfc2FsZV9wcmljZV9hbW91bnQKICAgSU5URUdFUiBkaW1fY3VzdG9tZXJfaWQKICAgSU5URUdFUiBkaW1fZW1wbG95ZWVfaWQKICAgSU5URUdFUiBkaW1fdHJhbnNhY3Rpb25fbm90ZXNfaWQKICAgQk9PTEVBTiBpc19maW5hbmNlZAogICBCT09MRUFOIGlzX3RyYWRlX2luCiAgIFRJTUVTVEFNUCBsYXN0X3VwZGF0ZWQKICAgREFURSBzYWxlX2RhdGUKICAgSU5URUdFUiB0cmFuc2FjdGlvbl9pZAp9CmNsYXNzIGRpbV9jdXN0b21lcnsKICAgKklOVEVHRVIgaWQgTk9UIE5VTEwKICAgVkFSQ0hBUjwxMDA-IGNpdHkKICAgVElNRVNUQU1QIGNyZWF0ZWQKICAgVkFSQ0hBUjw1MD4gZmlyc3RfbmFtZQogICBWQVJDSEFSPDEwMD4gZnVsbF9hZGRyZXNzCiAgIFZBUkNIQVI8MTAwPiBmdWxsX25hbWUKICAgVkFSQ0hBUjw1MD4gbGFzdF9uYW1lCiAgIFRJTUVTVEFNUCBsYXN0X3VwZGF0ZWQKICAgVkFSQ0hBUjwxMDA-IHBob25lCiAgIFZBUkNIQVI8MTAwPiBzdGF0ZQogICBWQVJDSEFSPDEwMD4gc3RyZWV0Cn0KY2xhc3MgZGltX2VtcGxveWVlewogICAqSU5URUdFUiBpZCBOT1QgTlVMTAogICBUSU1FU1RBTVAgY3JlYXRlZAogICBWQVJDSEFSPDUwPiBmaXJzdF9uYW1lCiAgIFZBUkNIQVI8MTAwPiBmdWxsX25hbWUKICAgVkFSQ0hBUjw1MD4gbGFzdF9uYW1lCiAgIFRJTUVTVEFNUCBsYXN0X3VwZGF0ZWQKfQpjbGFzcyBkaW1fdmVoaWNsZXsKICAgKklOVEVHRVIgaWQgTk9UIE5VTEwKICAgVElNRVNUQU1QIGNyZWF0ZWQKICAgVElNRVNUQU1QIGxhc3RfdXBkYXRlZAogICBERUNJTUFMIG1zcnBfYW1vdW50CiAgIFZBUkNIQVI8MTAwPiB2aW4KfQpjbGFzcyBkaW1fdHJhbnNhY3Rpb25fbm90ZXN7CiAgICpJTlRFR0VSIGlkIE5PVCBOVUxMCiAgIFRJTUVTVEFNUCBjcmVhdGVkCiAgIFRJTUVTVEFNUCBsYXN0X3VwZGF0ZWQKICAgVEVYVCBub3Rlcwp9CmRpbV92ZWhpY2xlICIwLi4xIiAtLSAiMC4ubiIgZmFjdF90cmFuc2FjdGlvbgpkaW1fZW1wbG95ZWUgIjAuLjEiIC0tICIwLi5uIiBmYWN0X3RyYW5zYWN0aW9uCmRpbV90cmFuc2FjdGlvbl9ub3RlcyAiMC4uMSIgLS0gIjAuLm4iIGZhY3RfdHJhbnNhY3Rpb24KZGltX3ZlaGljbGUgIjAuLjEiIC0tICIwLi5uIiBmYWN0X3RyYW5zYWN0aW9uCmRpbV9jdXN0b21lciAiMC4uMSIgLS0gIjAuLm4iIGZhY3RfdHJhbnNhY3Rpb24=)
