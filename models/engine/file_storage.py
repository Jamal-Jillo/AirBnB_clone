#!/usr/bin/python3
""" Class FileStorage. """
import json


class FileStorage:
    """ Class FileStorage. """
    __file_path = "file.json"
    __objects = {}  # Empty Dictionary

    def all(self):
        """ Returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id. """
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """ Serializes __objects to the JSON file (path: __file_path). """
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(FileStorage.__objects, f)

    def reload(self):
        """ Deserializes the JSON file to __objects. """
        try:
            with open(FileStorage.__file_path, 'r') as f:
                FileStorage.__objects = json.load(f)
        except FileNotFoundError:
            pass