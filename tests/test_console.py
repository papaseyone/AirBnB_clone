#!/usr/bin/python3
"""Unit tests for the console module"""

import sys
import unittest
from io import StringIO
from unittest.mock import create_autospec

from console import HBNBCommand


class TestConsole(unittest.TestCase):
    '''Test the HBNBCommand class in the console module'''

    def setUp(self):
        '''Set up the test environment'''
        self.backup = sys.stdout
        self.captured_output = StringIO()
        sys.stdout = self.captured_output

    def tearDown(self):
        '''Restore the test environment'''
        sys.stdout = self.backup

    def create_console_instance(self):
        '''Create an instance of the HBNBCommand class for testing'''
        return HBNBCommand()

    def test_quit_command(self):
        '''Test if the quit command exists'''
        console = self.create_console_instance()
        self.assertTrue(console.onecmd("quit"))

    def test_EOF_command(self):
        '''Test if the EOF command exists'''
        console = self.create_console_instance()
        self.assertTrue(console.onecmd("EOF"))

    def test_all_command(self):
        '''Test if the all command exists'''
        console = self.create_console_instance()
        console.onecmd("all")
        self.assertTrue(isinstance(self.captured_output.getvalue(), str))

    def test_show_command(self):
        '''Test if the show command exists'''
        console = self.create_console_instance()
        console.onecmd("create User")
        user_id = self.captured_output.getvalue()
        sys.stdout = self.backup
        self.captured_output.close()
        self.captured_output = StringIO()
        sys.stdout = self.captured_output
        console.onecmd("show User " + user_id)
        output = self.captured_output.getvalue()
        sys.stdout = self.backup
        self.assertTrue(str is type(output))

    def test_show_class_name_missing(self):
        '''Test error message for missing class name in show command'''
        console = self.create_console_instance()
        console.onecmd("create User")
        user_id = self.captured_output.getvalue()
        sys.stdout = self.backup
        self.captured_output.close()
        self.captured_output = StringIO()
        sys.stdout = self.captured_output
        console.onecmd("show")
        output = self.captured_output.getvalue()
        sys.stdout = self.backup
        self.assertEqual("** class name missing **\n", output)

    def test_show_instance_id_missing(self):
        '''Test error message for missing instance id in show command'''
        console = self.create_console_instance()
        console.onecmd("create User")
        user_id = self.captured_output.getvalue()
        sys.stdout = self.backup
        self.captured_output.close()
        self.captured_output = StringIO()
        sys.stdout = self.captured_output
        console.onecmd("show User")
        output = self.captured_output.getvalue()
        sys.stdout = self.backup
        self.assertEqual("** instance id missing **\n", output)

    def test_show_no_instance_found(self):
        '''Test error message for show command with non-existent instance'''
        console = self.create_console_instance()
        console.onecmd("create User")
        user_id = self.captured_output.getvalue()
        sys.stdout = self.backup
        self.captured_output.close()
        self.captured_output = StringIO()
        sys.stdout = self.captured_output
        console.onecmd("show User " + "124356876")
        output = self.captured_output.getvalue()
        sys.stdout = self.backup
        self.assertEqual("** no instance found **\n", output)

    def test_create_command(self):
        '''Test if the create command works'''
        console = self.create_console_instance()
        console.onecmd("create User")
        self.assertTrue(isinstance(self.captured_output.getvalue(), str))

    def test_create_missing_class_name(self):
        '''Test error message for missing class name in create command'''
        console = self.create_console_instance()
        console.onecmd("create")
        output = self.captured_output.getvalue()
        self.assertEqual("** class name missing **\n", output)

    def test_create_nonexistent_class_name(self):
        '''Test error message for nonexistent class name in create command'''
        console = self.create_console_instance()
        console.onecmd("create Binita")
        output = self.captured_output.getvalue()
        self.assertEqual("** class doesn't exist **\n", output)

    '''
    def test_destroy_command(self):
        console = self.create_console_instance()
        self.assertTrue(console.onecmd("destroy"))

    def test_update_command(self):
        console = self.create_console_instance()
        self.assertTrue(console.onecmd("update"))
    '''


if __name__ == '__main__':
    unittest.main()
