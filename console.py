#!/usr/bin/python3
"""Console module.
Method for command interpreter.
"""

import cmd
import re
from models import storage
from shlex import split
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review


def parse(arg):
    """parses and splits input arguments"""
    brace_curly = re.search(r"\{(.*?)\}", arg)
    bracket_square = re.search(r"\[(.*?)\]", arg)
    if brace_curly is None:
        if bracket_square is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[: bracket_square.span()[0]])
            ret_lexer = [i.strip(",") for i in lexer]
            ret_lexer.append(bracket_square.group())
            return ret_lexer
    else:
        lexer = split(arg[: brace_curly.span()[0]])
        ret_lexer = [i.strip(",") for i in lexer]
        ret_lexer.append(brace_curly.group())
        return ret_lexer


class HBNBCommand(cmd.Cmd):
    """Defines the HBNBCommand class command interpreter.

    Attributes:
        prompt (str): The prompt of the console.
    """

    prompt = "(hbnb) "
    __classes = {"BaseModel", "User",
                 "Amenity", "Place",
                 "City", "State",
                 "Review"}

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def help_quit(self):
        """prints help message for quit command"""
        print("Exit the program")

    def do_EOF(self, arg):
        """EOF signal to exit the program"""
        print("")
        return True

    def help_create(self):
        """Display help message for the create command"""
        print("Creates a new instance")
        print("create <class name>")

    def do_create(self, arg):
        """Creates a new instance of BaseModel, save it and print the id.
        Usage: create <class name>
        """
        new_arg = parse(arg)
        if len(new_arg) == 0:
            print("** class name missing **")
        elif new_arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(new_arg[0])().id)
            storage.save()

    def do_show(self, arg):
        """Prints the string representation of an instance based on the
        class name and id.
        Usage: show <class name> <id>
        """
        new_arg = parse(arg)
        obj_dict = storage.all()
        if len(new_arg) == 0:
            print("** class name missing **")
        elif new_arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(new_arg) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(new_arg[0], new_arg[1]) not in obj_dict:
            print("** no instance found **")
        else:
            print(obj_dict["{}.{}".format(new_arg[0], new_arg[1])])

    def help_show(self):
        """Display help message for the show command"""
        print("Prints the string representation of an instance")
        print("base on class name and id")

    def help_destroy(self):
        """Display help message for the destroy command"""
        print("Deletes an instance based on the class name and id")
        print("delete <class name> <id>")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id.
        Usage: destroy <class name> <id>
        """
        new_arg = parse(arg)
        obj_dict = storage.all()
        if len(new_arg) == 0:
            print("** class name missing **")
        elif new_arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist")
        elif len(new_arg) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(new_arg[0], new_arg[1]) not in obj_dict.keys():
            print("** no instance found **")
        else:
            del obj_dict["{}.{}".format(new_arg[0], new_arg[1])]
            storage.save()

    def help_all(self):
        """Display help message for the destroy command"""
        print("prints all string representation of all instance if")
        print("'all' is input without any argument")
        print("prints all string representation of all instance of a class")
        print("if 'all <class name>' is input")

    def do_all(self, arg):
        """Prints all string representation of all instances
        Usage: all <class name>
        """
        new_arg = parse(arg)
        if len(new_arg) > 0 and new_arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            new_obj = []
            for obj in storage.all().values():
                if len(new_arg) > 0 and new_arg[0] == obj.__class__.__name__:
                    new_obj.append(obj.__str__())
                elif len(new_arg) == 0:
                    new_obj.append(obj.__str__())
            print(new_obj)

    """do_count method"""

    def help_update(self):
        """Display help message for the destroy command"""
        print("update an instance based on the class name and id")
        print("This is done by adding or updating attributes")
        print("update <classname> <id> <attribute> <value>")

    def do_update(self, arg):
        """Updates an instance based on the class name and id.
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        new_arg = parse(arg)
        obj_dict = storage.all()

        if len(new_arg) == 0:
            print("** class name missing **")
            return False
        if new_arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(new_arg) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(new_arg[0], new_arg[1]) not in obj_dict.keys():
            print("** no  instance found **")
            return False
        if len(new_arg) == 2:
            print("** attribute name missing **")
            return False
        if len(new_arg) == 3:
            try:
                type(eval(new_arg[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(new_arg) == 4:
            obj = obj_dict["{}.{}".format(new_arg[0], new_arg[1])]
            if new_arg[2] in obj.__class__.__dict__.keys():
                val_type = type(obj.__class__.__dict__[new_arg[2]])
                obj.__dict__[new_arg[2]] = val_type(new_arg[3])
            else:
                obj.__dict__[new_arg[2]] = new_arg[3]
        elif type(eval(new_arg[2])) == dict:
            obj = obj_dict["{}.{}".format(new_arg[0], new_arg[1])]
            for i, j in eval(new_arg[2]).items():
                if i in obj.__class__.__dict__keys() and type(
                    obj.__class__.__dict__[i]
                ) in {str, int, float}:
                    val_type = type(obj.__class__.__dict__[i])
                    obj.__dict__[i] = val_type(j)
                else:
                    obj.__dict__[i] = j
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
