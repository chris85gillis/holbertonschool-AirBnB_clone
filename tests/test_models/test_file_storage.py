#!/usr/bin/python3
"""Defines unittests for models/engine/file_storage.py"""

import os
import unittest
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.test_file_path = "test_file.json"
        FileStorage._FileStorage__file_path = self.test_file_path
        self.storage = FileStorage()
        self.obj = BaseModel()
        self.storage.new(self.obj)

    def tearDown(self):
        if os.path.exists(self.test_file_path):
            os.remove(self.test_file_path)

    def test_save_and_reload(self):
        self.storage.save()
        self.storage.reload()
        loaded_objects = self.storage.all()
        self.assertTrue(f"{self.obj.__class__.__name__}.{self.obj.id}" in loaded_objects)
        loaded_obj = loaded_objects["BaseModel.test_id"]
        self.assertEqual(loaded_obj.id, "test_id")

    def test_all(self):
        all_objects = self.storage.all()
        self.assertTrue("BaseModel.test_id" in all_objects)
        obj = all_objects["BaseModel.test_id"]
        self.assertEqual(obj.id, "test_id")

    def test_new(self):
        obj = BaseModel()
        obj.id = "new_test_id"
        self.storage.new(obj)
        all_objects = self.storage.all()
        self.assertTrue("BaseModel.new_test_id" in all_objects)

if __name__ == "__main__":
    unittest.main()
