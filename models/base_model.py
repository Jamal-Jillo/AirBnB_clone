#!/usr/bin/env python3
"""This module contains the BaseModel class."""
from datetime import datetime
import uuid


class BaseModel:
    """
    This class will define all common.
    attributes/methods for other classes.
    """

    def __init__(self, id, created_at, updated_at):
        """__init__ constructor method for BaseModel class."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """__str__ method to print a string representation of the class."""
        classname = self.__class__.__name__
        return ("[{}] ({}) {}".format(classname, self.id, self.__dict__))

    def save(self):
        """Save method to update the public instance attribute updated_at."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """to_dict method to return a dictionary containing all keys/values."""
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
