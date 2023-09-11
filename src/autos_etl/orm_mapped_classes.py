"""Definitions module for ORM Mapped Classes

This gets us access to ORM classes by associating classes to Table objects.

We use the "imperative mapping" approach in SQLAlchemy.
* We have defined our tables using SQLAlchemy Core (schema-centric API)
* But we still want to be able to use the SQLAlchemy ORM (domain-centric API)
* So we will manually ("imperatively") map classes to tables
    * Using the ORM-only ("declarative") approach 
      does the schema definition and mapping in one go
"""

from .model_01_dealer import (
    dim_vehicle,
    dim_vehicle_model,
    fact_inventory,
    dim_customer,
)
from sqlalchemy.orm import registry


# ORM Mapped Classes
class InventoryItem:
    def __init__(self):
        self.id = None

    def __repr__(self):
        return f"InventoryItem(id={self.id!r})"


class Vehicle:
    def __repr__(self):
        fields = ", ".join(
            f"{key}={getattr(self, key)}" for key in self.__table__.c.keys()
        )
        return f"<{self.__class__.__name__}({fields})>"


class VehicleModel:
    def __repr__(self):
        fields = ", ".join(
            f"{key}={getattr(self, key)}" for key in self.__table__.c.keys()
        )
        return f"<{self.__class__.__name__}({fields})>"


class Customer:
    def __init__(self):
        self.id = None

    def __repr__(self):
        return f"Customer(id={self.id!r})"


# SQLAlchemy v2.0+ style
mapper_registry = registry()
_ = mapper_registry.map_imperatively(InventoryItem, fact_inventory)
_ = mapper_registry.map_imperatively(Vehicle, dim_vehicle)
_ = mapper_registry.map_imperatively(VehicleModel, dim_vehicle_model)
_ = mapper_registry.map_imperatively(Customer, dim_customer)

# Legacy/deprecated SQLAlchemy <v2.0 style
# from sqlalchemy.orm import mapper
# mapper(InventoryItem, fact_inventory)
# mapper(Vehicle, dim_vehicle)
# mapper(VehicleModel, dim_vehicle_model)
