#!/usr/bin/python3
"""Package initializer"""

# Import necessary modules
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User

# Create a FileStorage instance
storage = FileStorage()

# Reload the stored data
storage.reload()

