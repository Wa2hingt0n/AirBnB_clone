#!/usr/bin/python3
""" Defines a class FileStorage for storing instances to a JSON file """


import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """ Serializes instances to a JSON file and deserializes JSON file to
    instances """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns a dictionary of all objects """
        return FileStorage.__objects

    def new(self, obj):
        """ Sets the object to be stored in the __object dictionary by its
        classname and id

        Args:
            obj: The object to be set
        """
        FileStorage.__objects[obj.__class__.__name__ + "." +
                              obj.id] = obj

    def save(self):
        """ Serializes the dictionary of objects to a JSON file """
        obj_dict = {}
        for k, v in FileStorage.__objects.items():
            obj_dict[k] = v.to_dict()

        with open(FileStorage.__file_path, 'w') as f:
            json_string = json.dumps(obj_dict)
            f.write(json_string)

    def reload(self):
        """ Deserializes a json string back to an instance """
        try:
            with open(FileStorage.__file_path, 'r') as f:
                json_dict = json.load(f)
                for obj in json_dict.values():
                    cls_name = obj["__class__"]
                    self.new(eval("{}({})".format(cls_name, "**obj")))
        except FileNotFoundError:
            pass
