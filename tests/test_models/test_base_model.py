#!/usr/bin/python3
"""This script defined the class for unit testing BaseModel class"""


import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Defines all unit test cases for the BaseModel class"""

    def setUp(self):
        """This method prepare the test fixture"""
        pass

    def test__init__(self):
        """Tests if the object created from BaseModel() is actually
        BaseModel type
        """
        my_model_json = {
                "my_number": 89,
                "name": "My First Model",
                "__class__": "BaseModel",
                "updated_at": "2017-09-28T21:05:54.119572",
                "id": "b6a6e15c-c67d-4312-9a75-9d084935e579",
                "created_at": "2017-09-28T21:05:54.119427"
                }
        model_1 = BaseModel()
        model_2 = BaseModel()
        model_3 = BaseModel(**my_model_json)
        self.assertIsInstance(model_1, BaseModel)
        self.assertIsInstance(model_1.id, str)
        self.assertIsInstance(model_1, BaseModel)
        self.assertNotEqual(model_1.id, model_2.id)
        self.assertIsInstance(model_1.created_at, datetime)
        self.assertIsInstance(model_1.updated_at, datetime)
        self.assertEqual(model_1.created_at, model_1.updated_at)

    def test__str__(self):
        """Tests if __str__() method returns a string"""
        model_1 = BaseModel()
        str_model_1 = model_1.__str__()
        self.assertIsInstance(str_model_1, str)

    def test_save(self):
        """Tests if instance method save() actually updates the update_at
        instance attribute
        """
        model_1 = BaseModel()
        model_1.save()
        self.assertNotEqual(model_1.updated_at, model_1.created_at)

    def test_dict(self):
        """Tests if the instance method to_dict() returns a dictionary
        containing all keys/values of __dict__ of the instance
        """
        model_1 = BaseModel()
        model_1_dict = model_1.to_dict()
        self.assertIsInstance(model_1_dict, dict)
        self.assertIn("__class__", model_1_dict)
        self.assertIsInstance(model_1_dict["created_at"], str)
        self.assertIsInstance(model_1_dict["updated_at"], str)
