#!/usr/bin/python3
"""Defines the FileStorage class."""

import json
import os
from models.base_model import BaseModel


class FileStorage:
    """ class interacting w json files
    """
    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {}

    def save(self):
        """serializes data to json file
        """
        data = {}
        for key, value in self.__objects.items():
            data[key] = value.to_dict()
            with open(self.__file_path, "w", encoding="utf-8") as file:
                json.dump(data, file)

    def all(self):
        """way to access all loaded and reloaded in filestorage instance

        Returns:
            __object: dictionary containging all obj stores
        """
        return self.__objects

    def new(self, obj):
        """Add a new object to the storage.
        """
        key = "{}, {}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def reload(self):
        """reload: deserilizes data back to json file
        """
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                for key, obj_data in data.items():
                    class_name, obj_id = key.split('.')
                    obj = models[class_name](**obj_data)
                    self.__objects[key] = obj


storage = FileStorage()
"""create an instance of the storage class"""

models = {
    'BaseModel': BaseModel
    """add other model classes here"""
}
