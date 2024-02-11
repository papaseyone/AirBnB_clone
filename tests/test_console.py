#!/usr/bin/python3
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestConsole(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.mock_stdout = StringIO()

    def setUp(self):
        # Initialize a new instance of HBNBCommand for each test
        self.console = HBNBCommand(stdout=self.mock_stdout)

    # Testing the 'create' command
    def test_create(self):
        with patch('builtins.input', side_effect=["create BaseModel"]):
            self.console.onecmd("create BaseModel")
            output = self.mock_stdout.getvalue().strip()
            self.assertTrue(len(output) == 36)  # ID should be a UUID

    # Testing 'create' command with missing class name
    def test_create_missing_class(self):
        with patch('builtins.input', side_effect=["create"]):
            self.console.onecmd("create")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

    # Testing 'create' command with invalid class name
    def test_create_invalid_class(self):
        with patch('builtins.input', side_effect=["create MyModel"]):
            self.console.onecmd("create MyModel")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    # Testing the 'show' command with a valid instance
    def test_show_valid_instance(self):
        with patch('builtins.input', side_effect=[
                "create BaseModel", "show BaseModel 1234-1234-1234"]):
            self.console.onecmd("create BaseModel")
            self.console.onecmd("show BaseModel 1234-1234-1234")
            output = self.mock_stdout.getvalue().strip()
            self.assertTrue("BaseModel" in output)
            self.assertTrue("1234-1234-1234" in output)

    # Testing 'show' command with missing class name
    def test_show_missing_class(self):
        with patch('builtins.input', side_effect=["show"]):
            self.console.onecmd("show")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

    # Testing 'show' command with invalid class name
    def test_show_invalid_class(self):
        with patch('builtins.input', side_effect=[
                "show MyModel 1234-1234-1234"]):
            self.console.onecmd("show MyModel 1234-1234-1234")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    # Testing 'show' command with missing instance ID
    def test_show_missing_instance_id(self):
        with patch('builtins.input', side_effect=["show BaseModel"]):
            self.console.onecmd("show BaseModel")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(output, "** instance id missing **")

    # Testing 'show' command with nonexistent instance
    def test_show_nonexistent_instance(self):
        with patch('builtins.input', side_effect=["show BaseModel 121212"]):
            self.console.onecmd("show BaseModel 121212")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    # Testing the 'destroy' command with a valid instance
    def test_destroy_valid_instance(self):
        with patch('builtins.input', side_effect=[
                "create BaseModel", "destroy BaseModel 1234-1234-1234"]):
            self.console.onecmd("create BaseModel")
            self.console.onecmd("destroy BaseModel 1234-1234-1234")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(output, "")
            # Verify that the instance was actually deleted from storage
            self.assertEqual(len(self.console.valid_class_names()), 0)

    # Testing 'destroy' command with missing class name
    def test_destroy_missing_class(self):
        with patch('builtins.input', side_effect=["destroy"]):
            self.console.onecmd("destroy")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

    # Testing 'destroy' command with invalid class name
    def test_destroy_invalid_class(self):
        with patch('builtins.input', side_effect=[
                "destroy MyModel 1234-1234-1234"]):
            self.console.onecmd("destroy MyModel 1234-1234-1234")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    # Testing 'destroy' command with missing instance ID
    def test_destroy_missing_instance_id(self):
        with patch('builtins.input', side_effect=["destroy BaseModel"]):
            self.console.onecmd("destroy BaseModel")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(output, "** instance id missing **")

    # Testing 'destroy' command with nonexistent instance
    def test_destroy_nonexistent_instance(self):
        with patch('builtins.input', side_effect=["destroy BaseModel 121212"]):
            self.console.onecmd("destroy BaseModel 121212")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    # Testing the 'all' command without specifying class name
    def test_all_without_class(self):
        with patch('builtins.input', side_effect=[
                "create BaseModel", "create BaseModel"]):
            self.console.onecmd("create BaseModel")
            self.console.onecmd("create BaseModel")
            with patch('builtins.input', side_effect=["all"]):
                self.console.onecmd("all")
                output = self.mock_stdout.getvalue().strip()
                self.assertTrue("BaseModel" in output)
                self.assertTrue("1234-1234-1234" in output)
                self.assertTrue("5678-5678-5678" in output)  # IDs may vary

    # Testing the 'all' command with specifying class name
    def test_all_with_class(self):
        with patch('builtins.input', side_effect=[
                "create BaseModel", "create BaseModel"]):
            self.console.onecmd("create BaseModel")
            self.console.onecmd("create BaseModel")
            with patch('builtins.input', side_effect=["all BaseModel"]):
                self.console.onecmd("all BaseModel")
                output = self.mock_stdout.getvalue().strip()
                self.assertTrue("BaseModel" in output)
                self.assertTrue("1234-1234-1234" in output)
                self.assertTrue("5678-5678-5678" in output)


if __name__ == '__main__':
    unittest.main()

