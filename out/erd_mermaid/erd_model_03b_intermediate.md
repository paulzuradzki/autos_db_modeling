<!--

classDiagram
class dim_vehicle_dealer_01{
   *INTEGER id NOT NULL
   TIMESTAMP created
   INTEGER dim_vehicle_model_id
   TIMESTAMP last_updated
   VARCHAR<100> vin
}
class dim_vehicle_model_dealer_01{
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
class dim_vehicle_dealer_02{
   *INTEGER id NOT NULL
   TIMESTAMP created
   TIMESTAMP last_updated
   DECIMAL msrp_amount
   VARCHAR<100> vin
}
class dim_vehicle_dealer_integrated{
   *INTEGER id NOT NULL
   TIMESTAMP created
   INTEGER dim_vehicle_model_id
   TIMESTAMP last_updated
   VARCHAR<100> vin
}
class dim_vehicle_model_integrated{
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
dim_vehicle_model_dealer_01 "0..1" -- "0..n" dim_vehicle_dealer_01
dim_vehicle_model_integrated "0..1" -- "0..n" dim_vehicle_dealer_integrated

-->
![](https://mermaid.ink/img/Y2xhc3NEaWFncmFtCmNsYXNzIGRpbV92ZWhpY2xlX2RlYWxlcl8wMXsKICAgKklOVEVHRVIgaWQgTk9UIE5VTEwKICAgVElNRVNUQU1QIGNyZWF0ZWQKICAgSU5URUdFUiBkaW1fdmVoaWNsZV9tb2RlbF9pZAogICBUSU1FU1RBTVAgbGFzdF91cGRhdGVkCiAgIFZBUkNIQVI8MTAwPiB2aW4KfQpjbGFzcyBkaW1fdmVoaWNsZV9tb2RlbF9kZWFsZXJfMDF7CiAgICpJTlRFR0VSIGlkIE5PVCBOVUxMCiAgIFZBUkNIQVI8MjA-IGNvbG9yCiAgIFRJTUVTVEFNUCBjcmVhdGVkCiAgIFZBUkNIQVI8MjA-IGRvb3JfdHlwZQogICBWQVJDSEFSPDIwPiBkcml2ZV90cmFpbl90eXBlCiAgIFRJTUVTVEFNUCBsYXN0X3VwZGF0ZWQKICAgVkFSQ0hBUjwyMD4gbWFrZQogICBWQVJDSEFSPDIwPiBtb2RlbAogICBERUNJTUFMIG1zcnBfYW1vdW50CiAgIFZBUkNIQVI8MTAwPiB0cmltCiAgIFZBUkNIQVI8MjA-IHdoZWVsX2RyaXZlX3R5cGUKICAgSU5URUdFUiB5ZWFyCn0KY2xhc3MgZGltX3ZlaGljbGVfZGVhbGVyXzAyewogICAqSU5URUdFUiBpZCBOT1QgTlVMTAogICBUSU1FU1RBTVAgY3JlYXRlZAogICBUSU1FU1RBTVAgbGFzdF91cGRhdGVkCiAgIERFQ0lNQUwgbXNycF9hbW91bnQKICAgVkFSQ0hBUjwxMDA-IHZpbgp9CmNsYXNzIGRpbV92ZWhpY2xlX2RlYWxlcl9pbnRlZ3JhdGVkewogICAqSU5URUdFUiBpZCBOT1QgTlVMTAogICBUSU1FU1RBTVAgY3JlYXRlZAogICBJTlRFR0VSIGRpbV92ZWhpY2xlX21vZGVsX2lkCiAgIFRJTUVTVEFNUCBsYXN0X3VwZGF0ZWQKICAgVkFSQ0hBUjwxMDA-IHZpbgp9CmNsYXNzIGRpbV92ZWhpY2xlX21vZGVsX2ludGVncmF0ZWR7CiAgICpJTlRFR0VSIGlkIE5PVCBOVUxMCiAgIFZBUkNIQVI8MjA-IGNvbG9yCiAgIFRJTUVTVEFNUCBjcmVhdGVkCiAgIFZBUkNIQVI8MjA-IGRvb3JfdHlwZQogICBWQVJDSEFSPDIwPiBkcml2ZV90cmFpbl90eXBlCiAgIFRJTUVTVEFNUCBsYXN0X3VwZGF0ZWQKICAgVkFSQ0hBUjwyMD4gbWFrZQogICBWQVJDSEFSPDIwPiBtb2RlbAogICBERUNJTUFMIG1zcnBfYW1vdW50CiAgIFZBUkNIQVI8MTAwPiB0cmltCiAgIFZBUkNIQVI8MjA-IHdoZWVsX2RyaXZlX3R5cGUKICAgSU5URUdFUiB5ZWFyCn0KZGltX3ZlaGljbGVfbW9kZWxfZGVhbGVyXzAxICIwLi4xIiAtLSAiMC4ubiIgZGltX3ZlaGljbGVfZGVhbGVyXzAxCmRpbV92ZWhpY2xlX21vZGVsX2ludGVncmF0ZWQgIjAuLjEiIC0tICIwLi5uIiBkaW1fdmVoaWNsZV9kZWFsZXJfaW50ZWdyYXRlZA==)