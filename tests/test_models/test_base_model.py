#!/usr/bin/python3
"""
Unittest tests for the BaseModel Class
"""
import unittest
import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """ TestBaseModel class """

    def setUp(self):
        """ Setup method to create instances for testing """
        self.base_model = BaseModel()

    def test_uuid(self):
        """Test cases for uuid"""
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertIsInstance(bm1, BaseModel)
        self.assertTrue(hasattr(bm1, "id"))
        self.assertNotEqual(bm1.id, bm2.id)
        self.assertIsInstance(bm1.id, str)

    def test_id_is_string(self):
        """Test if id is a string"""
        self.assertIsInstance(self.base_model.id, str)

    def test_created_at_is_datetime(self):
        """Test if created_at is a datetime object"""
        self.assertIsInstance(self.base_model.created_at, datetime.datetime)

    def test_updated_at_is_datetime(self):
        """Test if updated_at is a datetime object"""
        self.assertIsInstance(self.base_model.updated_at, datetime.datetime)

    def test_str_representation(self):
        """Test the string representation of BaseModel"""
        expected_str = f"[{self.base_model.__class__.__name__}]({self.base_model.id}) {self.base_model.__dict__}"
        self.assertEqual(str(self.base_model), expected_str)

    def test_save_updates_updated_at(self):
        """Test if calling save() updates updated_at"""
        old_updated_at = self.base_model.updated_at
        self.base_model.save()
        new_updated_at = self.base_model.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict_returns_correct_dict(self):
        """Test if to_dict() returns the correct dictionary"""
        obj_dict = self.base_model.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertIn('id', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)

    def test_to_dict_contains_isoformat_dates(self):
        """Test if to_dict() contains ISO formatted dates"""
        obj_dict = self.base_model.to_dict()
        self.assertEqual(obj_dict['created_at'], self.base_model.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'], self.base_model.updated_at.isoformat())


if __name__ == '__main__':
    unittest.main()

