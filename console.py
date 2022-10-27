#!/usr/bin/python3
"""Console module for the AirBnB project."""
import cmd
import models
import shlex  # For splitting arguments passed
from models.base_model import BaseModel

classes = {"BaseModel": BaseModel}


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

    def do_create(self, args):
        """Create a new instance of a BaseModel."""
        if args == "":
            print("** class name missing **")
        elif args != "BaseModel":
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


if __name__ == '__main__':
    console = HBNBCommand()
    console.cmdloop()
