#!/usr/bin/python3
""" This module defines a class HBNBCommand that is the entry point to the
command interpreter """
import cmd
import shlex
import models
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


def parse(line):
    """ Parses a string of commands and returns a list of the tokens """
    return shlex.split(line)

class HBNBCommand(cmd.Cmd):
    """ Defines the entry point to the command line interpreter """
    intro = "Welocome to the hbnb shell. Type help or ? to list commands.\n"
    prompt = "(hbnb) "
    available_classes = ["BaseModel", "User", "Amenity", "City", "Place",
                         "Review", "State"]


    def emptyline(self):
        """ Overrides the emptyline() method """
        pass

    def do_create(self, class_name):
        """ Creates a new instance, saves it to file.json and prints the id
        """

        if not class_name:
             print("** class name missing **")
        else:
            try:
                new = eval(class_name + "()")
                new.save()
                print(new.id)
            except:
                print("** class doesn't exist **")

    def do_show(self, line):
        """ Prints the string representation of an instance

        Usage: show <class_name> <instance_id>
        """
        if not line:
            print("** class name missing **")
        else:
            commands = parse(line)
            if commands[0] not in HBNBCommand.available_classes:
                print("** class doesn't exist **")
            elif len(commands) < 2:
                print("** instance id missing **")
            else:
                instances = models.storage.all()
                key = "{}.{}".format(commands[0], commands[1])
                try:
                    print(instances[key])
                except:
                    print("** no instance found **")

    def do_destroy(self, line):
        """ Deletes an instance and saves the change into the JSON file storage

        Usage: destroy <classname> <id>
        """
        if not line:
            print("** class name missing **")
        else:
            commands = parse(line)
            if commands[0] not in HBNBCommand.available_classes:
                print("** class doesn't exist **")
            elif len(commands) < 2:
                print("** instance id missing **")
            else:
                try:
                    instances = models.storage.all()
                    key = "{}.{}".format(commands[0], commands[1])
                    del instances[key]
                    models.storage.save()
                except:
                    print("** no instance found **")

    def do_all(self, line):
        """ Prints a string representation of all instances based on an
        optional class name argument

        Usage: all <classname> OR all
        """
        clsname = parse(line)
        obj_list = []
        if len(clsname) > 0:
            if clsname[0] not in HBNBCommand.available_classes:
                print("** class doesn't exist **")
        else:
            for obj in models.storage.all().values():
                if len(clsname) > 0 and clsname[0] == obj.__class__.__name__:
                    obj_list.append(obj.__str__())
                elif len(clsname) == 0:
                    obj_list.append(obj.__str__())
            print(obj_list)

    def do_update(self, line):
        """ Updates an instance based on the class name and id by adding or
        updating attribute. The changes are then saved into a JSON file

        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = parse(line)
        instance_dict = models.storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.available_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in instance_dict.keys():
            print("** no instance found")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            obj = instance_dict["{}.{}".format(args[0], args[1])]
            if args[2] in obj.__class__.__dict__.keys():
                attr_type = type(obj.__class__.__dict__[args[2]])
                obj.__dict__[args[2]] = attr_type(args[3])
            else:
                obj.__dict__[args[2]] = args[3]

        models.storage.save()

    def do_quit(self, arg):
        """ Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """ EOF command to exit the program """
        print()
        return True




if __name__ == '__main__':
    HBNBCommand().cmdloop()
