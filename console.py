#!/usr/bin/python3
"""Console module for the AirBnB project."""
import cmd


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


if __name__ == '__main__':
    console = HBNBCommand()
    console.cmdloop()
