#!/usr/bin/python3
"""Defines the BaseModel class which defines all common attributes/methods
"""


import models
from datetime import datetime
from uuid import uuid4


class BaseModel:
    """Represents HBnB BaseModel class which is a parent class
    for all other classes"""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel constructor

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        date_creation = datetime.now()
        self.created_at = date_creation
        self.updated_at = date_creation
        if len(kwargs) != 0:
            for i, j in kwargs.items():
                if i == "created_at" or i == "updated_at":
                    self.__dict__[i] = datetime.strptime(j, time_format)
                else:
                    self.__dict__[i] = j
        else:
            models.storage.new(self)

    def __str__(self):
        """Returns the official print/str representation of
        the BaseModel instance.
        """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """Updates instance updated_at with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns the dictionary of the BaseModel instance.

        Includes the key/value pair __class__ representing
        the class name of the object.
        """
        new_dict = self.__dict__.copy()
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        new_dict["__class__"] = self.__class__.__name__
        return new_dict
