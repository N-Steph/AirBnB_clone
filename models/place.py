#!/usr/bin/python3
"""Defines the Place class which inherits from BaseModel super class."""


from models.base_model import BaseModel


class Place(BaseModel):
    """Represents a place.

    Attributes:
    city_id (str): The City id.
    user_id (str): The User id.
    name (str): The name of the place.
    description (str): The description of the place.
    number_rooms (int): The number of the place rooms.
    number_bathrooms (int): The number of bathrooms of the place.
    max_guest (int): The maximum number of guests of the place.
    price_by_night (int): The price per night for the place.
    latitude (float): The latitude coordinate of the place.
    longitude (float): The longitude coordinate of the place.
    amenity_ids (list): The list of the Amenity id.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guests = 0
    price_per_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
