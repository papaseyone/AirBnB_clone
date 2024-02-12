#!/usr/bin/python3
""" Review class inheriting from the BaseModel """

from models.base_model import BaseModel


class Review(BaseModel):
    """ Review class that inherits from the base model """
    place_id = ""  # Represents the Place.id associated with the review
    user_id = ""   # Represents the User.id associated with the review
    text = ""

    def __init__(self, *args, **kwargs):
        """ Constructor """
        super().__init__(*args, **kwargs)
