#!/usr/bin/python3
""" Unit test Place """
import unittest
import models
import os
from models.place import Place


class TestPlace(unittest.TestCase):
    """ Test class Place"""

    def test_docstring(self):
        '''test if functions, methods, classes
        and modules have docstring'''
        msj = "Módulo does not has docstring"
        self.assertIsNotNone(models.place.__doc__, msj)  # Modules
        msj = "Clase does not has docstring"
        self.assertIsNotNone(Place.__doc__, msj)  # Classes

    def test_executable_file(self):
        '''test if file has permissions u+x to execute'''
        # Check for read access
        is_read_true = os.access('models/place.py', os.R_OK)
        self.assertTrue(is_read_true)
        # Check for write access
        is_write_true = os.access('models/place.py', os.W_OK)
        self.assertTrue(is_write_true)
        # Check for execution access
        is_exec_true = os.access('models/place.py', os.X_OK)
        self.assertTrue(is_exec_true)

    def test_init_Place(self):
        """test if an obj is a type Place"""
        my_object = Place()
        self.assertIsInstance(my_object, Place)

    def test_id(self):
        """ test id unique """
        my_objectId = Place()
        my_objectId1 = Place()
        self.assertNotEqual(my_objectId.id, my_objectId1.id)

    def test_str(self):
        '''check if output of string is in the specified format'''
        my_strobject = Place()
        _dict = my_strobject.__dict__
        string1 = "[Place] ({}) {}".format(my_strobject.id, _dict)
        string2 = str(my_strobject)
        self.assertEqual(string1, string2)

    def test_save(self):
        """ check if date update when save """
        my_objectupd = Place()
        first_updated = my_objectupd.updated_at
        my_objectupd.save()
        second_updated = my_objectupd.updated_at
        self.assertNotEqual(first_updated, second_updated)

    def test_to_dict(self):
        '''check if to_dict returns a dict, if add a class
        key with class name of obj and if updated_at and
        created_at are converted to str obj in ISO format.'''
        my_model3 = Place()
        my_dict_model3 = my_model3.to_dict()
        self.assertIsInstance(my_dict_model3, dict)
        for key, value in my_dict_model3.items():
            flag = 0
            if my_dict_model3['__class__'] == 'Place':
                flag += 1
            self.assertTrue(flag == 1)
        for key, value in my_dict_model3.items():
            if key == 'created_at':
                self.assertIsInstance(value, str)
            if key == 'updated_at':
                self.assertIsInstance(value, str)


if __name__ == '__main__':
    unittest.main()
