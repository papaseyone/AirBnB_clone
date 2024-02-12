#!/usr/bin/python3
""" BaseModel Module """

import uuid
from datetime import datetime
import models


class BaseModel:
    """ Base class for models """
    def __init__(self, *args, **kwargs):
        """ Constructor """
        if kwargs:
            # Initialize attributes based on key-value pairs in kwargs
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key != "__class__":
                    setattr(self, key, value)
        else:
            # Gen. unique id, set created_at and updated_at to curr datetime
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ String representation of the BaseModel instance """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """ Update with the current datetime and save changes """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Return a dictionary with all keys/values of the instance """
        dict_copy = self.__dict__.copy()
        dict_copy["created_at"] = self.created_at.isoformat()
        dict_copy["updated_at"] = self.updated_at.isoformat()
        dict_copy['__class__'] = self.__class__.__name__
        return dict_copy

    # @property
    # def id(self):
    #     return self.id
