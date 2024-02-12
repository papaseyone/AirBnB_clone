#!/usr/bin/python3
""" User class inheriting from the BaseModel """

from models.base_model import BaseModel


class User(BaseModel):
    """ User class that inherits from the base model """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
