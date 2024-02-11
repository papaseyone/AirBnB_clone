#!/usr/bin/python3
"""
This module defines the HBNBCommand class for the command-line interface
of the airbnb_clone project.
"""
import cmd
import models
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    The HBNBCommand class represents the command-line interpreter for
    the airbnb_clone project.
    """

    prompt = "(hbnb) "

    def do_quit(self, argum):
        """
        Quit command to exit the program.
        """
        return True

    def do_EOF(self, argum):
        """
        Handle EOF signal to gracefully exit the program.
        """
        print()
        return True

    def help_quit(self):
        """
        Provide help message for the quit command.
        """
        print("Quit command to exit the program")

    def emptyline(self):
        """
        Do nothing when the user inputs an empty line.
        """
        pass

    def do_create(self, argum):
        """
        Create a new instance of BaseModel, save it, and print the id.
        """
        argums = argum.split()

        if not argums:
            print("** class name missing **")
            return
        class_name = argums[0]
        if class_name not in self.valid_class_names():
            print("** class doesn't exist **")
            return

        new_instance = BaseModel()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, argum):
        """
        Print the string representation of an instance.
        """
        argums = argum.split()

        if not argums:
            print("** class name missing **")
            return

        class_name = argums[0]
        if class_name not in self.valid_class_names():
            print("** class doesn't exist **")
            return

        if len(argums) < 2:
            print("** instance id missing **")
            return

        instance_id = argums[1]
        instance_key = f"{class_name}.{instance_id}"
        all_objects = models.storage.all()

        if instance_key not in all_objects:
            print("** no instance found **")
            return

        print(all_objects[instance_key])

    def do_destroy(self, argum):
        """
        Delete an instance based on class name and class id.
        """
        argums = argum.split()

        if not argums:
            print("** class name missing **")
            return

        class_name = argums[0]
        if class_name not in self.valid_class_names():
            print("** class doesn't exist **")
            return

        if len(argums) < 2:
            print("** instance id missing **")
            return

        instance_id = argums[1]
        instance_key = f"{class_name}.{instance_id}"
        all_objects = models.storage.all()

        if instance_key not in all_objects:
            print("** no instance found **")
            return

        del all_objects[instance_key]
        models.storage.save()

    def do_all(self, argum):
        """
        Print string representations of all instances.
        """
        class_name = argum.strip()

        if class_name and class_name not in self.valid_class_names():
            print("** class doesn't exist **")
            return

        all_objects = models.storage.all()

        if class_name:
            filtered_objs = [str(obj) for key, obj in all_objects.items()
                             if key.startswith(class_name + ".")]
        else:
            filtered_objs = [str(obj) for obj in all_objects.values()]

        print(filtered_objs)

    def do_update(self, argum):
        """
        Update an instance based on the name of the class and the id.
        """
        argums = argum.split()

        if not argums:
            print("** class name missing **")
            return

        class_name = argums[0]
        if class_name not in self.valid_class_names():
            print("** class doesn't exist **")
            return

        if len(argums) < 2:
            print("** instance id missing **")
            return

        instance_id = argums[1]
        instance_key = f"{class_name}.{instance_id}"
        all_objects = models.storage.all()

        if instance_key not in all_objects:
            print("** no instance found **")
            return

        if len(argums) < 3:
            print("** attribute name missing **")
            return

        attribute_name = argums[2]
        if len(argums) < 4:
            print("** value missing **")
            return

        new_value = argums[3]
        instance = all_objects[instance_key]

        """Update attribute"""
        setattr(instance, attribute_name, new_value)
        instance.save()

    def valid_class_names(self):
        """Return a list of valid class names."""
        return ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]


if __name__ == '__main__':
    HBNBCommand().cmdloop()

