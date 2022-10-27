#!/usr/bin/python3
"""Console module for the AirBnB project."""
import cmd
import models
import shlex  # For splitting arguments passed
from models.base_model import BaseModel
from models.user import User

classes = {"BaseModel": BaseModel, "User": User}  # Dictionary of classes


class HBNBCommand(cmd.Cmd):
    """Command Line Interpreter for AirBnB project."""

    prompt = '(hbnb) '

    def do_quit(self, args):
        """Quit command to exit the program."""
        return True

    def help_quit(self):
        """Help for quit command."""
        print("Type 'quit' command to exit the program")

# ! Does not work
    def do_clear(self, args):
        """Clear the console."""
        pass

# ! Does not work
    def do_EOF(self, args):
        """Use 'CTRL + D' command to exit the program."""
        return True

    def help_EOF(self):
        """Help for EOF command."""
        print("Use 'CTRL + D' command to exit the program")

    def emptyline(self):
        """Empty line + ENTER shouldn’t execute anything."""
        pass

    def do_create(self, arg):
        """Create a new instance of a BaseModel."""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in classes:
            print(eval(args[0])().id)
            models.storage.save()
        else:
            print("** class doesn't exist **")

# ? Update this later
    def help_create(self):
        """Help for create command."""
        print("Create a new instance of a BaseModel")

    def do_show(self, arg):
        """Print the string representation of an instance."""
        args = shlex.split(arg)  # Split arguments passed
        if len(args) == 0:  # If no arguments passed
            print("** class name missing **")
            return False
        if args[0] in classes:  # If class name is valid (in classes)
            if len(args) > 1:  # Check If id is passed
                # Create key to search for in storage
                key = args[0] + "." + args[1]
                # Check If key exists in storage
                if key in models.storage.all():
                    print(models.storage.all()[key])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

# ? Update this later
    def help_show(self):
        """Help for show command."""
        print("Print the string representation of an instance")

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id."""
        args = shlex.split(arg)  # Split arguments passed
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                # Check If key exists in storage
                if key in models.storage.all():
                    del models.storage.all()[key]
                    models.storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

# ? Update this later
    def help_destroy(self):
        """Help for destroy command."""
        print("Delete an instance based on the class name and id")

    def do_all(self, arg):
        """Print all string representation of all instances."""
        args = shlex.split(arg)
        if len(args) > 0 and args[0] not in classes:
            print("** class doesn't exist **")
        else:
            obj_dict = []
            for obj in models.storage.all().values():
                # Checks if class name exists
                if len(args) > 0 and args[0] == obj.__class__.__name__:
                    # Append string representation of object
                    obj_dict.append(obj.__str__())
                elif len(args) == 0:  # For all objects
                    obj_dict.append(obj.__str__())
            # print(obj_dict) -- Rollback to this if not working
            # Added this Feature to print each object in a new line
            for i in range(len(obj_dict)):
                print(obj_dict[i])
                if i == len(obj_dict) - 1:
                    break

# ? Update this later
    def help_all(self):
        """Help for all command."""
        print("Print all string representation of all instances")

    def do_update(self, arg):
        """
        Summary: Update an instance based on the class name and id.

        Update an instance based on the class name and
        id by adding or updating attribute.
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    if len(args) > 2:
                        if len(args) > 3:
                            setattr(models.storage.all()[key], args[2],
                                    args[3])
                            models.storage.save()
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    console = HBNBCommand()
    console.cmdloop()
