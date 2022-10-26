#!/usr/bin/python3
""" Class FileStorage. """
import json


class FileStorage:
    """ Class FileStorage. """
    __file_path = "file.json"
    __objects = {}  # Empty Dictionary

    def all(self):
        """ Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id. """
        self.__objects[type(obj).__name__ + "." + obj.id] = obj

    def save(self):
        """ Serializes __objects to the JSON file (path: __file_path). """
        temp = {}
        with open(self.__file_path, 'w') as jsonfile:
            json.dump(temp, jsonfile)

    def reload(self):
        """ Deserializes the JSON file to __objects. """
        try:
            with open(self.__file_path, 'r') as f:
                self.__objects = json.load(f)
        except FileNotFoundError:
            pass
