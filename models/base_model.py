#!/usr/bin/python3
""" This module defines the class BaseModel which is the base class for all
classes used in this project """


from datetime import datetime
from models import storage
from uuid import uuid4



class BaseModel:
    """ Defines instance attributes used for all sub-classes """
    def __init__(self, *args, **kwargs):
        """ Initializes instances with common attributes

        Args:
            args: A tuple that contains all arguments
            kwargs: A dictionary that contains all arguments by key/value
        """
        if len(kwargs) > 0:
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                elif k == "created_at":
                    self.created_at = datetime.strptime(v,
                                                        '%Y-%m-%dT%H:%M:%S.%f')
                elif k == "updated_at":
                    self.updated_at = datetime.strptime(v,
                                                        '%Y-%m-%dT%H:%M:%S.%f')
                elif k == "name":
                    self.name = v
                elif k == "my_number":
                    self.my_number = v
                elif k == "__class__":
                    continue
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """ Overrides the __str__ method to print custom text """
        string = "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                       self.__dict__)
        return string

    def save(self):
        """ Updated the updated_at instance attribute with the current datetime
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ Returns a dictionary containing all keys/values of __dict__ of the
        instance """
        self.created_at = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        self.updated_at = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        obj_dict = self.__dict__
        obj_dict['__class__'] = self.__class__.__name__
        return obj_dict
