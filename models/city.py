#!/user/bin/python3
"""Defines the City class which inherits from BaseModel parent class."""


from models.base_model import BaseModel


class City(BaseModel):
    """Represents a city.

    Attributes:
    state_id (str): The state id.
    name (str): The name of this city
    """

    state_id = ""
    name = ""
