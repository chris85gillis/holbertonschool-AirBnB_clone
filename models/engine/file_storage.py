#!/usr/bin/python3
"""Defines the FileStorage class."""

import json
import os
from models.user import User
from models.base_model import BaseModel

classes = {
    'BaseModel': BaseModel,
    'User': User,
}


class FileStorage:
    """ class interacting w json files
    """
    __file_path = "file.json"
    __objects = {}

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
        return FileStorage.__objects

    def new(self, obj):
        """new _summary_
        Args:
            obj (_type_): _description_
        """
        named_class = obj.__class__.__name__
        object_id = obj.id
        key = "{}, {}".format(named_class, object_id)
        self.__objects[key] = obj

    def reload(self):
        """reload: deserilizes data back to json file
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                for key, value in data.items():
                    named_class, obj_id = key.split(", ")
                    inst_class = eval(named_class)
                    obj = inst_class(**value)
                    obj.id = obj_id
                    self.__objects[key] = obj
        else:
            pass
