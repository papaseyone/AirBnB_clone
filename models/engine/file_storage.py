"""FileStorage module"""
import json
from models.base_model import BaseModel


class FileStorage:
    """
    This class serializes instances to a JSON file
    and deserializes JSON to instances.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns:
            dict: Dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id

        Args:
            obj (BaseModel): An instance object
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to JSON file."""
        obj_dict = {}
        for key, val in FileStorage.__objects.items():
            obj_dict[key] = val.to_dict()

        with open(FileStorage.__file_path, mode='w', encoding="UTF8") as fd:
            json.dump(obj_dict, fd)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            with open(FileStorage.__file_path, mode='r') as fd:
                data = json.load(fd)
                for key, obj_dict in data.items():
                    obj = BaseModel(**obj_dict)
                    FileStorage.__objects[key] = obj

        except FileNotFoundError:
            pass

    def valid_class_names(self):
        """
        Returns:
            list: A list of valid class names.
        """
        return ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]

