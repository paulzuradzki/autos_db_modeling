<!--

classDiagram
class fact_sale_transactions_dealer_01{
   *INTEGER id NOT NULL
   TIMESTAMP created
   INTEGER dim_customer_id
   INTEGER dim_discount_type_id
   INTEGER dim_vehicle_id
   BOOLEAN is_trade_in
   TIMESTAMP last_updated
   DECIMAL purchase_price_amount
   DATE sale_date
   DECIMAL trade_in_value_amount
}
class fact_transaction_02{
   *INTEGER id NOT NULL
   TIMESTAMP created
   DECIMAL dealer_purchase_cost_amount
   NULL dealer_purchase_dim_vehicle_id
   NULL dealer_sale_dim_vehicle_id
   DECIMAL dealer_sale_price_amount
   NULL dim_customer_id
   NULL dim_employee_id
   NULL dim_transaction_notes_id
   BOOLEAN is_financed
   BOOLEAN is_trade_in
   TIMESTAMP last_updated
   DATE sale_date
   DECIMAL trade_in_value_amount
   INTEGER transaction_id
}
class fact_sale_transactions_integrated{
   *INTEGER id NOT NULL
   TIMESTAMP created
   INTEGER dim_customer_id
   INTEGER dim_discount_type_id
   NULL dim_employee_id
   INTEGER dim_vehicle_id
   BOOLEAN is_trade_in
   TIMESTAMP last_updated
   DECIMAL purchase_price_amount
   DATE sale_date
   DECIMAL trade_in_value_amount
   INTEGER transaction_id
}


-->
![](https://mermaid.ink/img/Y2xhc3NEaWFncmFtCmNsYXNzIGZhY3Rfc2FsZV90cmFuc2FjdGlvbnNfZGVhbGVyXzAxewogICAqSU5URUdFUiBpZCBOT1QgTlVMTAogICBUSU1FU1RBTVAgY3JlYXRlZAogICBJTlRFR0VSIGRpbV9jdXN0b21lcl9pZAogICBJTlRFR0VSIGRpbV9kaXNjb3VudF90eXBlX2lkCiAgIElOVEVHRVIgZGltX3ZlaGljbGVfaWQKICAgQk9PTEVBTiBpc190cmFkZV9pbgogICBUSU1FU1RBTVAgbGFzdF91cGRhdGVkCiAgIERFQ0lNQUwgcHVyY2hhc2VfcHJpY2VfYW1vdW50CiAgIERBVEUgc2FsZV9kYXRlCiAgIERFQ0lNQUwgdHJhZGVfaW5fdmFsdWVfYW1vdW50Cn0KY2xhc3MgZmFjdF90cmFuc2FjdGlvbl8wMnsKICAgKklOVEVHRVIgaWQgTk9UIE5VTEwKICAgVElNRVNUQU1QIGNyZWF0ZWQKICAgREVDSU1BTCBkZWFsZXJfcHVyY2hhc2VfY29zdF9hbW91bnQKICAgTlVMTCBkZWFsZXJfcHVyY2hhc2VfZGltX3ZlaGljbGVfaWQKICAgTlVMTCBkZWFsZXJfc2FsZV9kaW1fdmVoaWNsZV9pZAogICBERUNJTUFMIGRlYWxlcl9zYWxlX3ByaWNlX2Ftb3VudAogICBOVUxMIGRpbV9jdXN0b21lcl9pZAogICBOVUxMIGRpbV9lbXBsb3llZV9pZAogICBOVUxMIGRpbV90cmFuc2FjdGlvbl9ub3Rlc19pZAogICBCT09MRUFOIGlzX2ZpbmFuY2VkCiAgIEJPT0xFQU4gaXNfdHJhZGVfaW4KICAgVElNRVNUQU1QIGxhc3RfdXBkYXRlZAogICBEQVRFIHNhbGVfZGF0ZQogICBERUNJTUFMIHRyYWRlX2luX3ZhbHVlX2Ftb3VudAogICBJTlRFR0VSIHRyYW5zYWN0aW9uX2lkCn0KY2xhc3MgZmFjdF9zYWxlX3RyYW5zYWN0aW9uc19pbnRlZ3JhdGVkewogICAqSU5URUdFUiBpZCBOT1QgTlVMTAogICBUSU1FU1RBTVAgY3JlYXRlZAogICBJTlRFR0VSIGRpbV9jdXN0b21lcl9pZAogICBJTlRFR0VSIGRpbV9kaXNjb3VudF90eXBlX2lkCiAgIE5VTEwgZGltX2VtcGxveWVlX2lkCiAgIElOVEVHRVIgZGltX3ZlaGljbGVfaWQKICAgQk9PTEVBTiBpc190cmFkZV9pbgogICBUSU1FU1RBTVAgbGFzdF91cGRhdGVkCiAgIERFQ0lNQUwgcHVyY2hhc2VfcHJpY2VfYW1vdW50CiAgIERBVEUgc2FsZV9kYXRlCiAgIERFQ0lNQUwgdHJhZGVfaW5fdmFsdWVfYW1vdW50CiAgIElOVEVHRVIgdHJhbnNhY3Rpb25faWQKfQo=)
