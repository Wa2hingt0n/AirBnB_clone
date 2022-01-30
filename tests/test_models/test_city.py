#!/usr/bin/python3
""" Module contains unittests for the city module """

import models
import unittest
from datetime import datetime
from models.city import City


class TestCity_initialization(unittest.TestCase):
    """ Tests the initialization of instances of the City class """

    def test_amenity_instantiation(self):
        """ Tests that object is an instance of BaseModel """
        obj = City()
        self.assertIsInstance(obj, City)

    def test_attribute_initialization(self):
        """ Tests that an instance has id, created_at and updated_at attributes
        """
        obj = City()
        obj2 = City()
        self.assertIsNot(obj, obj2)
        self.assertIsNotNone(obj.id)
        self.assertIsNotNone(obj.created_at)
        self.assertIsNotNone(obj.updated_at)
        self.assertIsNotNone(obj.name)
        self.assertIsNotNone(obj.state_id)

    def test_id_initialization(self):
        """ Tests that id is a string and the id is unique """
        obj1 = City()
        obj2 = City()
        self.assertEqual(len(obj1.id), 36)
        self.assertNotEqual(obj1.id, obj2.id)
        self.assertIsInstance(obj1.id, str)

    def test_created_at_initialization(self):
        """ Tests the initialization of attributes as datetime objects """
        obj = City()
        self.assertIsInstance(obj.created_at, datetime)

    def test_updated_at_initialization(self):
        """ Verifies that updated_at attribute is a datetime object """
        self.assertIsInstance(City().updated_at, datetime)

    def test_name_initialization(self):
        """ Tests the initialization of attributes as datetime objects """
        obj = City()
        self.assertIsInstance(obj.name, str)

    def test_state_id_initialization(self):
        """ Tests the initialization of attributes as datetime objects """
        obj = City()
        self.assertIsInstance(obj.state_id, str)

    def test_save_method_with_updated_at_attribute(self):
        """ Verifies that the save method updates the updated at attribute """
        obj = City()
        updated_at_1 = obj.updated_at
        created_at_1 = obj.created_at
        name_1 = obj.name
        obj.save()
        updated_at_2 = obj.updated_at
        created_at_2 = obj.created_at
        name_2 = obj.name
        self.assertNotEqual(updated_at_1, updated_at_2)
        self.assertEqual(created_at_1, created_at_2)
        self.assertEqual(name_1, name_2)

    def test_to_dict_method_returns_dictionary(self):
        """ Verify that a dictionary is returned after a call to the to_dict
        method """
        obj = City()
        self.assertIsInstance(obj.to_dict(), dict)

    def test_class_name_as_value_in_to_dict_dictionary(self):
        """ Verify that the key __class__ and value 'class name' are part of
        attributes returned by the to_dict method """
        obj = City()
        obj_dict = obj.to_dict()
        key = "__class__"
        value = "City"
        self.assertIn(key, obj_dict)
        self.assertEqual(value, obj_dict[key])

    def test_to_dict_string_attributes(self):
        """ Verify the created_at and updated_at attributes are strings after
         a call to the to_dict method """
        obj = City()
        obj_dict = obj.to_dict()
        self.assertIsInstance(obj_dict['created_at'], str)
        self.assertIsInstance(obj_dict['updated_at'], str)

    def test_to_dict_attributes(self):
        """ Verify the to_dict() method returns all instance attributes """
        obj = City()
        obj_dict = obj.to_dict()
        self.assertIn('id', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)
        self.assertEqual(obj_dict['created_at'], obj.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'], obj.updated_at.isoformat())

    def test_to_dict_custom_attributes_added(self):
        obj = City()
        obj.my_name = "Betty"
        obj_dict = obj.to_dict()
        self.assertIn('my_name', obj_dict)

    def test_class_attribute_presence_with_kwargs_instantiation(self):
        """ Verify that id, created_at and updated_at attributes are present
        while creating an instance with kwargs """
        obj_dict = {}
        obj = City(**obj_dict)
        self.assertIsNotNone(obj.id)
        self.assertIsNotNone(obj.created_at)
        self.assertIsNotNone(obj.updated_at)

    def test_kwargs_instantiation(self):
        """ Tests instantiation with key-worded variable arguments """
        obj = City()
        obj.my_name = "Betty"
        obj.my_number = 89
        obj_dict = obj.to_dict()
        new_obj = City(**obj_dict)
        new_obj_dict = new_obj.to_dict()
        self.assertIsNot(new_obj, obj)
        self.assertDictEqual(new_obj_dict, obj_dict)

    def test_str_method(self):
        """ Tests __str__ output  is [class name] (self.id) <self.__dict__> """
        obj = City()
        obj_str = obj.__str__()
        self.assertIsInstance(obj_str, str)
        self.assertEqual(obj_str[:6], "[City]")


if __name__ == '__main__':
    unittest.main()
