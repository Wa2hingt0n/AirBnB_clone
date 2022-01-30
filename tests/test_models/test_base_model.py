#!/usr/bin/python3
""" Module contains unittests for the base_model module """

import models
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel_initialization(unittest.TestCase):
    """ Tests the initialization of instances of the BaseModel class """

    def test_base_model_instantiation(self):
        """ Tests that object is an instance of BaseModel """
        obj = BaseModel()
        self.assertIsInstance(obj, BaseModel)

    def test_base_model_id_attribute_initialization(self):
        """ Tests that an instance has id, created_at and updated_at attributes
        """
        obj = BaseModel()
        obj2 = BaseModel()
        self.assertIsNot(obj, obj2)
        self.assertIsNotNone(obj.id)
        self.assertIsNotNone(obj.created_at)
        self.assertIsNotNone(obj.updated_at)

    def test_id_initialization(self):
        """ Tests that id is a string and the id is unique """
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertEqual(len(obj1.id), 36)
        self.assertNotEqual(obj1.id, obj2.id)
        self.assertIsInstance(obj1.id, str)

    def test_created_at_updated_at_initialization(self):
        """ Tests the initialization of attributes as datetime objects """
        obj = BaseModel()
        self.assertIsInstance(obj.created_at, datetime)

    def test_updated_at_initialization(self):
        """ Verifies that updated_at attribute is a datetime object """
        self.assertIsInstance(BaseModel().updated_at, datetime)

    def test_save_method_with_updated_at_attribute(self):
        """ Verifies that the save method updates the updated at attribute """
        obj = BaseModel()
        updated_at_1 = obj.updated_at
        created_at_1 = obj.created_at
        obj.save()
        updated_at_2 = obj.updated_at
        created_at_2 = obj.created_at
        self.assertNotEqual(updated_at_1, updated_at_2)
        self.assertEqual(created_at_1, created_at_2)

    def test_to_dict_method_returns_dictionary(self):
        """ Verify that a dictionary is returned after a call to the to_dict
        method """
        obj = BaseModel()
        self.assertIsInstance(obj.to_dict(), dict)

    def test_class_name_as_value_in_to_dict_dictionary(self):
        """ Verify that the key __class__ and value 'class name' are part of
        attributes returned by the to_dict method """
        obj = BaseModel()
        obj_dict = obj.to_dict()
        key = "__class__"
        value = "BaseModel"
        self.assertIn(key, obj_dict)
        self.assertEqual(value, obj_dict[key])

    def test_to_dict_string_attributes(self):
        """ Verify the created_at and updated_at attributes are strings after
         a call to the to_dict method """
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertIsInstance(obj_dict['created_at'], str)
        self.assertIsInstance(obj_dict['updated_at'], str)

    def test_to_dict_attributes(self):
        """ Verify the to_dict() method returns all instance attributes """
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertIn('id', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)
        self.assertEqual(obj_dict['created_at'], obj.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'], obj.updated_at.isoformat())

    def test_to_dict_custom_attributes_added(self):
        obj = BaseModel()
        obj.my_name = "Betty"
        obj_dict = obj.to_dict()
        self.assertIn('my_name', obj_dict)

    def test_class_attribute_presence_with_kwargs_instantiation(self):
        """ Verify that id, created_at and updated_at attributes are present
        while creating an instance with kwargs """
        obj_dict = {}
        obj = BaseModel(**obj_dict)
        self.assertIsNotNone(obj.id)
        self.assertIsNotNone(obj.created_at)
        self.assertIsNotNone(obj.updated_at)

    def test_kwargs_instantiation(self):
        """ Tests instantiation with key-worded variable arguments """
        obj = BaseModel()
        obj.my_name = "Betty"
        obj.my_number = 89
        obj_dict = obj.to_dict()
        new_obj = BaseModel(**obj_dict)
        new_obj_dict = new_obj.to_dict()
        self.assertIsNot(new_obj, obj)
        self.assertDictEqual(new_obj_dict, obj_dict)

    def test_str_method(self):
        """ Tests __str__ output  is [class name] (self.id) <self.__dict__> """
        obj = BaseModel()
        obj_str = obj.__str__()
        self.assertIsInstance(obj_str, str)
        self.assertEqual(obj_str[:11], "[BaseModel]")


if __name__ == '__main__':
    unittest.main()
