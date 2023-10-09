#!/usr/bin/python3
"""Defines unittests for models/base_model.py."""

import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

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

    def test_new_instance_added_to_storage(self):
        initial_count = len(FileStorage.all())

        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89

        # Check that the instance is not in storage before calling save
        self.assertNotIn(my_model.__class__.__name__ + "." + my_model.id, FileStorage.all())

        # Save the instance to storage (this should call 'new' internally)
        my_model.save()

        # Check that the instance is now in storage
        self.assertIn(my_model.__class__.__name__ + "." + my_model.id, FileStorage.all())

        # Check that the count of objects in storage increased by 1
        final_count = len(FileStorage.all())
        self.assertEqual(final_count, initial_count + 1)

    def test_to_dict_method(self):
        """Test the to_dict method of BaseModel."""
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89

        my_model_dict = my_model.to_dict()
        
        self.assertIsInstance(my_model_dict, dict)

        self.assertEqual(my_model_dict['__class__'], "BaseModel")
        self.assertEqual(my_model_dict['name'], "My First Model")
        self.assertEqual(my_model_dict['my_number'], 89)

    def test_deserialization_from_dict(self):
        """Test deserialization from a dictionary."""
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89

        my_model_json = my_model.to_dict()

        my_new_model = BaseModel(**my_model_json)

        self.assertEqual(my_model.id, my_new_model.id)
        self.assertEqual(my_model.created_at, my_new_model.created_at)
        self.assertEqual(my_model.updated_at, my_new_model.updated_at)
        self.assertEqual(my_model.name, my_new_model.name)
        self.assertEqual(my_model.my_number, my_new_model.my_number)

    def test_identity_after_deserialization(self):
        """Test identity of the original and deserialized objects."""
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        
        my_model_json = my_model.to_dict()
        
        my_new_model = BaseModel(**my_model_json)
        
        self.assertEqual(my_model, my_new_model)

if __name__ == "__main__":
    unittest.main()
