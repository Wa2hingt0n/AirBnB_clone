#!/usr/bin/python3
""" This module defines a class HBNBCommand that is the entry point to the
command interpreter """
import cmd
import shlex
import models
from models.base_model import BaseModel

def parse(line):
    """ Parses a string of commands and returns a list of the tokens """
    return shlex.split(line)

class HBNBCommand(cmd.Cmd):
    """ Defines the entry point to the command line interpreter """
    intro = "Welocome to the hbnb shell. Type help or ? to list commands.\n"
    prompt = "(hbnb) "
    available_classes = ["BaseModel"]


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
        """ Prints all string representation of all instances based on an
        optional class name argument

        Usage: all <classname> OR all
        """
        #class_name = parse(line)
        #if class_name[0] not in HBNBCommand.available_classes:
         #   print("** class doesn't exist **")

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
