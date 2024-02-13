#!/usr/bin/python3
""" Unit test User """
import unittest
import models
import os
from models.user import User


class TestUser(unittest.TestCase):
    """ Test class User"""

    def test_docstring(self):
        '''test if functs, methods, classes
        and modules have docstring'''
        msj = "Módulo does not has docstring"
        self.assertIsNotNone(models.user.__doc__, msj)  # Modules
        msj = "Clase does not has docstring"
        self.assertIsNotNone(User.__doc__, msj)  # Classes

    def test_executable_file(self):
        '''test if file has permissions u+x to exec'''
        # Check for read access
        is_read_true = os.access('models/user.py', os.R_OK)
        self.assertTrue(is_read_true)
        # Check for write access
        is_write_true = os.access('models/user.py', os.W_OK)
        self.assertTrue(is_write_true)
        # Check for execution access
        is_exec_true = os.access('models/user.py', os.X_OK)
        self.assertTrue(is_exec_true)

    def test_init_User(self):
        """test if an obj is an type User"""
        my_object = User()
        self.assertIsInstance(my_object, User)

    def test_id(self):
        """ test id unique """
        my_objectId = User()
        my_objectId1 = User()
        self.assertNotEqual(my_objectId.id, my_objectId1.id)

    def test_str(self):
        '''check if output of string is in the specified format'''
        my_strobject = User()
        _dict = my_strobject.__dict__
        string1 = "[User] ({}) {}".format(my_strobject.id, _dict)
        string2 = str(my_strobject)
        self.assertEqual(string1, string2)

    def test_save(self):
        """ check if date update save """
        my_objectupd = User()
        first_updated = my_objectupd.updated_at
        my_objectupd.save()
        second_updated = my_objectupd.updated_at
        self.assertNotEqual(first_updated, second_updated)

    def test_to_dict(self):
        '''check if to_dict returns a dict, if add a class
        key with class name of the obj and if updated_at and
        created_at are converted to str obj in ISO format.'''
        my_model3 = User()
        my_dict_model3 = my_model3.to_dict()
        self.assertIsInstance(my_dict_model3, dict)
        for key, value in my_dict_model3.items():
            flag = 0
            if my_dict_model3['__class__'] == 'User':
                flag += 1
            self.assertTrue(flag == 1)
        for key, value in my_dict_model3.items():
            if key == 'created_at':
                self.assertIsInstance(value, str)
            if key == 'updated_at':
                self.assertIsInstance(value, str)


if __name__ == '__main__':
    unittest.main()
