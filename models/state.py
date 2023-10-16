#!/usr/bin/python3
"""Defines the State class which inherits from BaseModel class."""


from models.base_model import BaseModel


class State(BaseModel):
    """Represents a state.

    Attributes:
    name (str): the name of the state.
    """

    name = ""
