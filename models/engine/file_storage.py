#!/usr/bin/python3
"""Defines module for FileStorage class.
For serializing and deserializing object to FileStorage. 
"""

import json
from models.base_model import BaseModel


class FileStorage:
    """FileStorage class that represents an abstracted storage engine,
    for storing and retrieving data objects into and from a file respectively.

    Attributes:
        __file_path (str): Path/name of the file to save data object to.
        __objects (dict): Stores instantiated BaseModel class objects.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        obj_cls_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(obj_cls_name, obj.id)] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        obj_dict = FileStorage.__objects
        new_obj_dict = {obj: obj_dict[obj].to_dict() for obj in obj_dict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(new_obj_dict, f)

    def reload(self):
        """Deserializes the JSON file __file_path to __objects, if it exists.
        Otherwise do nothing, no exception should be raised.
        """
        try:
            with open(FileStorage.__file_path, "r") as f:
                new_obj_dict = json.load(f)
                for i in new_obj_dict.values():
                    class_name = i["__class__"]
                    del i["__class__"]
                    self.new(eval(class_name)(**i))
        except FileNotFoundError:
            return
