#!/usr/bin/python3
""" Module for models """

from models.engine.file_storage import FileStorage

# Dictionary mapping class names to corresponding module names
class_names = {
    'BaseModel': 'BaseModel',
    'Amenity': 'Amenity',
    'State': 'State',
    'Place': 'Place',
    'Review': 'Review',
    'User': 'User'
}

# Create an instance of FileStorage for data storage
storage = FileStorage()

# Reload stored data from the file
storage.reload()
