#!/usr/bin/python3
"""Defines the FileStorage class."""

import json
import os


class FileStorage:
    """ class interacting w json files
    """
    __file_path = "file.json"
    __objects = {}

    def save(self):
        """serilizes data to json file
        """
        data = {}
        for key, value in self.__objects.items():
            data[key] = value.to_dict()
            with open("self.__objects", "w", encoding="utf-8") as file:
                json.dump(data, self.__filepath)

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
        named_class = obj.__class__.__FileStorage__
        object_id = obj.id
        key = "{}, {}".format(FileStorage, object_id)
        self.__objects[key] = obj

    def reload(self):
        """reload: deserilizes data back to json file
        """
        __file_path = "__objects"
        if os.path.exists(__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                for key, value in data.items():
                    named_class, obj.id = key.split
                    inst_class = eval(named_class)
                    obj = inst_class(**value)
                self.__objects[key] = obj
        else:
            pass
