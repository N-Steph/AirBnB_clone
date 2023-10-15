#!/usr/bin/python3
"""This script contains the class  for unit testing FileStorage class"""



import unittest
from models import storage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """class unit testing the Serialization of instances to a JSON file
    and deserializes JSON file to instances
    """
    def test_all(self):
        """Tests if the all() method returns a dictionary"""
        self.assertIsInstance(storage.all(), dict);

    def test_new(self):
        """Tests if the new() method adds a new object to __objects dictionary"""
        num_obj_before = len(storage.all())
        model_1 = BaseModel()
        num_obj_after = len(storage.all())
        self.assertNotEqual(num_obj_after, num_obj_before)

    def test_reload(self):
        """Tests whether deserialization of JSON file occured correctly"""
        all_objects = storage.all()
        for obj_key, obj_value in all_objects.items():
            self.assertIsInstance(obj_value, BaseModel)
