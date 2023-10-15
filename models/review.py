#!/user/bin/python3
"""Defines the Review class which inherits from BaseModel parent class."""


from models.base_model import BaseModel


class Review(BaseModel):
    """Represents the review.

    Attributes:
    place_id (str): The Place id.
    user_id (str): The User id.
    text (str): The text of the review.
    """

    place_id = ""
    user_id = ""
    text = ""
