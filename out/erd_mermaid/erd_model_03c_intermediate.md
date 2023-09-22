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
class fact_transaction_dealer_02{
   *INTEGER id NOT NULL
   TIMESTAMP created
   NULL dim_customer_id
   NULL dim_employee_id
   NULL dim_transaction_notes_id
   NULL dim_vehicle_id
   BOOLEAN is_trade_in
   TIMESTAMP last_updated
   DECIMAL purchase_price_amount
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
![](https://mermaid.ink/img/Y2xhc3NEaWFncmFtCmNsYXNzIGZhY3Rfc2FsZV90cmFuc2FjdGlvbnNfZGVhbGVyXzAxewogICAqSU5URUdFUiBpZCBOT1QgTlVMTAogICBUSU1FU1RBTVAgY3JlYXRlZAogICBJTlRFR0VSIGRpbV9jdXN0b21lcl9pZAogICBJTlRFR0VSIGRpbV9kaXNjb3VudF90eXBlX2lkCiAgIElOVEVHRVIgZGltX3ZlaGljbGVfaWQKICAgQk9PTEVBTiBpc190cmFkZV9pbgogICBUSU1FU1RBTVAgbGFzdF91cGRhdGVkCiAgIERFQ0lNQUwgcHVyY2hhc2VfcHJpY2VfYW1vdW50CiAgIERBVEUgc2FsZV9kYXRlCiAgIERFQ0lNQUwgdHJhZGVfaW5fdmFsdWVfYW1vdW50Cn0KY2xhc3MgZmFjdF90cmFuc2FjdGlvbl9kZWFsZXJfMDJ7CiAgICpJTlRFR0VSIGlkIE5PVCBOVUxMCiAgIFRJTUVTVEFNUCBjcmVhdGVkCiAgIE5VTEwgZGltX2N1c3RvbWVyX2lkCiAgIE5VTEwgZGltX2VtcGxveWVlX2lkCiAgIE5VTEwgZGltX3RyYW5zYWN0aW9uX25vdGVzX2lkCiAgIE5VTEwgZGltX3ZlaGljbGVfaWQKICAgQk9PTEVBTiBpc190cmFkZV9pbgogICBUSU1FU1RBTVAgbGFzdF91cGRhdGVkCiAgIERFQ0lNQUwgcHVyY2hhc2VfcHJpY2VfYW1vdW50CiAgIERBVEUgc2FsZV9kYXRlCiAgIERFQ0lNQUwgdHJhZGVfaW5fdmFsdWVfYW1vdW50CiAgIElOVEVHRVIgdHJhbnNhY3Rpb25faWQKfQpjbGFzcyBmYWN0X3NhbGVfdHJhbnNhY3Rpb25zX2ludGVncmF0ZWR7CiAgICpJTlRFR0VSIGlkIE5PVCBOVUxMCiAgIFRJTUVTVEFNUCBjcmVhdGVkCiAgIElOVEVHRVIgZGltX2N1c3RvbWVyX2lkCiAgIElOVEVHRVIgZGltX2Rpc2NvdW50X3R5cGVfaWQKICAgTlVMTCBkaW1fZW1wbG95ZWVfaWQKICAgSU5URUdFUiBkaW1fdmVoaWNsZV9pZAogICBCT09MRUFOIGlzX3RyYWRlX2luCiAgIFRJTUVTVEFNUCBsYXN0X3VwZGF0ZWQKICAgREVDSU1BTCBwdXJjaGFzZV9wcmljZV9hbW91bnQKICAgREFURSBzYWxlX2RhdGUKICAgREVDSU1BTCB0cmFkZV9pbl92YWx1ZV9hbW91bnQKICAgSU5URUdFUiB0cmFuc2FjdGlvbl9pZAp9Cg==)