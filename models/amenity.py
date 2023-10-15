#!/usr/bin/python3
"""Defines the Amenity class which inherits from the BaseModel super class."""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represents an Amenity.

    Attributes:
    name (str): The name of the amenity.
    """

    name = ""
