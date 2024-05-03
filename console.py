#!/usr/bin/python3
"""Defines the HBNB console."""
import cmd
from shlex import split
from models import storage
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter."""

    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Amenity",
        "Place",
        "Review"
    }

    def emptyline(self):
        """Ignore empty spaces."""
        pass

    def do_quit(self, line):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, line):
        """EOF signal to exit the program."""
        print("")
        return True

    def do_create(self, line):
        """Usage: create <class> <key 1>=<value 2>=<value 2> ...
        Create a new class instance with given keys/values and print its id.
        """
        try:
            if not line:
                raise SyntasError()
            my_list = line.split(" ")

            kwargs = {}
            for i in range(1, len(my_list)):
                key, value = tuple(my_list[i].split("="))
                if value[0] == '"':
                    value = value.strip('"').replace("_"," ")
                else:
                    try:
                        value = eval(value)
                    except (SyntaxError, NameError):
                        continue
                    kwargs[key] = value

                if kwarga == {}:
                    obj = eval(my_list[0]) ()
                else:
                    obj = eval(mylist[0]) (**kwargs)
                    storage.new(obj)
                print(obj.id)
                obj.save()

            except SyntaxError:
                print("** class name missing **")
            except NameError:
                print("** class dosen't exist **")
