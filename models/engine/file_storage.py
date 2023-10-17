#!/usr/bin/python3
"""Defines module for FileStorage class.
For serializing and deserializing object to FileStorage.
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.city import City
from models.state import State
from models.review import Review


class FileStorage:
    """FileStorage class that represents an abstracted storage engine,
    for storing and retrieving data objects into and from a file respectively.

    Attributes:
        __file_path (str): Path/name of the file to save data object to.
        __objects (dict): Stores instantiated BaseModel class objects.
    """

    __file_path = "file.json"
    __objects = {}
    constructors = {
            'BaseModel': BaseModel, 'User': User,
            'State': State, 'City': City,
            'Amenity': Amenity, 'Place': Place,
            'Review': Review
            }

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
        new_obj_dict = {}
        for key in obj_dict.keys():
            new_obj_dict[key] = obj_dict[key].to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(new_obj_dict, f)

    def reload(self):
        """Deserializes the JSON file __file_path to __objects, if it exists.
        Otherwise do nothing, no exception should be raised.
        """
        try:
            json_file = open(self.__file_path, "r", encoding="utf-8")
        except Exception:
            return
        try:
            self.__objects = json.load(json_file)
        except Exception:
            json_file.close()
        for obj_id in self.__objects.keys():
            curr_obj_class = obj_id.split(".")
            obj = self.__objects[obj_id]
            for key in self.constructors:
                if key == curr_obj_class[0]:
                    obj = self.constructors[key](**obj)
                    break
            self.__objects[obj_id] = obj
        json_file.close()
