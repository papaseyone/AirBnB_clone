#!/usr/bin/python3
"""
Unit tests for the FileStorage class
"""
import unittest
import json
import models
from models.engine.file_storage import FileStorage


class TestFileStorageInstantiation(unittest.TestCase):
    """
    Testing instantiation of the FileStorage class.
    """

    def test_instantiation_with_no_args(self):
        """Test instantiation with no arguments"""
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_instantiation_with_arg(self):
        """Test instantiation with an argument"""
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_file_path_is_private_str(self):
        """Test if file_path is a private string"""
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_objects_is_private_dict(self):
        """Test if objects is a private dictionary"""
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage_initializing(self):
        """Test if models.storage is initialized as FileStorage"""
        self.assertEqual(type(models.storage), FileStorage)

    def test_initialization(self):
        """Test if the storage object is an instance of FileStorage"""
        self.assertIsInstance(models.storage, FileStorage)

    def test_new_and_all_methods(self):
        """Test new() and all() methods"""
        dummy_obj = {'__class__': 'BaseModel', 'id': 'test_id'}
        models.storage.new(dummy_obj)
        objects = models.storage.all()
        self.assertIn('BaseModel.test_id', objects)

    def test_save_and_reload(self):
        """Test save() and reload() methods"""
        dummy_obj = {'__class__': 'BaseModel', 'id': 'test_id'}
        models.storage.new(dummy_obj)
        models.storage.save()
        models.storage.reload()
        objects = models.storage.all()
        self.assertIn('BaseModel.test_id', objects)

    def test_save_and_reload_file(self):
        """Test save() and reload() methods for file content"""
        dummy_obj = {'__class__': 'BaseModel', 'id': 'test_id'}
        models.storage.new(dummy_obj)
        models.storage.save()
        models.storage.reload()
        with open(models.storage._FileStorage__file_path, 'r') as file:
            data = json.load(file)
            self.assertIn('BaseModel.test_id', data)


if __name__ == '__main__':
    unittest.main()

