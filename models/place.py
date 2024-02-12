#!/usr/bin/python3
""" Place Class Module """

from models.base_model import BaseModel


class Place(BaseModel):
    """ Place class that inherits from BaseModel """
    city_id = ""          # City ID associated with the place
    user_id = ""          # User ID associated with the place
    name = ""             # Place name
    description = ""      # Place description
    number_rooms = 0      # Number of rooms in the place
    number_bathrooms = 0  # Number of bathrooms in the place
    max_guest = 0         # Maximum number of guests the place can accommodate
    price_by_night = 0    # Price per night for the place
    latitude = 0.0        # Latitude of the place
    longitude = 0.0       # Longitude of the place
    amenity_ids = []      # List of Amenity IDs associated with the place

    def __init__(self, *args, **kwargs):
        """ Place Constructor """
        super().__init__(*args, **kwargs)
