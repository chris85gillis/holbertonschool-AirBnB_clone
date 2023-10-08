#!/usr/bin/python3
"""Defines unittests for models/base_model.py."""

import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class"""

    def test_attributes(self):
        """Test if attributes are correctly assigned."""
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89

        self.assertEqual(my_model.name, "My First Model")
        self.assertEqual(my_model.my_number, 89)

    def test_str_method(self):
        """Test the __str__ method of BaseModel."""
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89

        expected_str = "[BaseModel] ({}) {}".format(my_model.id, my_model.__dict__)

        self.assertEqual(str(my_model), expected_str)

    def test_save_method(self):
        """Test the save method of BaseModel."""
        my_model = BaseModel()
        initial_updated_at = my_model.updated_at

        my_model.save()
        updated_updated_at = my_model.updated_at

        self.assertNotEqual(initial_updated_at, updated_updated_at)

    def test_to_dict_method(self):
        """Test the to_dict method of BaseModel."""
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89

        my_model_dict = my_model.to_dict()

        self.assertEqual(my_model_dict['__class__'], "BaseModel")
        self.assertEqual(my_model_dict['name'], "My First Model")
        self.assertEqual(my_model_dict['my_number'], 89)

if __name__ == "__main__":
    unittest.main()
