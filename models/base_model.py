#!/usr/bin/python3
# This module defines the BaseModel class, which serves as the foundation for all other classes in the project.

import uuid
from datetime import datetime
import models


class BaseModel:
    # The BaseModel class contains attributes and methods that are common to all other classes.
    
    def __init__(self, *args, **kwargs):
        # Initializes instance attributes.
        # If kwargs is provided, it updates the instance attributes with the values from kwargs.
        # Otherwise, it generates a unique id, sets the creation and update timestamps, and adds the instance to the storage.
        
        if kwargs:
            if "__class__" in kwargs:
                del kwargs["__class__"]
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        # Returns a string representation of the BaseModel instance.
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        # Updates the updated_at attribute with the current datetime and saves the instance to the storage.
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        # Returns a dictionary representation of the BaseModel instance.
        my_dict = self.__dict__.copy()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["__class__"] = self.__class__.__name__
        return my_dict

