#!/usr/bin/python3
""" Amenity Class Module """

from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Amenity class that inherits from BaseModel """
    name = ""

    def __init__(self, *args, **kwargs):
        """ Amenity Constructor """
        super().__init__(*args, **kwargs)
