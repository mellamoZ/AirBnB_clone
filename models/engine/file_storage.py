#!/usr/bin/env python3
""" Class FileStorage that serializes instances to a JSON file
    and deserializes JSON file to instances
"""

import json
from os import read
from models.base_model import BaseModel
from models.city import City
from models.state import State
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import os.path


class FileStorage:
    """ Class FileStorage that serilizes
    and deserialize instances to JSON
        __file_path: the path of the json file
        __objects: a dictionnary of all objects"
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns a dictionary of all objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """serialize and save objects from __objects to a file
        in json in format json"""
        dictionary = {}
        """dicttionary is an empty dictionnary"""
        for key, value in FileStorage.__objects.items():
            dictionary[key] = value.to_dict()
        """dict[key] is equal to value.__dict__"""
        with open(self.__file_path, 'w') as f:
            """open(self.__file_path, 'w') open the json file in write mode"""
            json.dump(dictionary, f)
            """dump(dictionary, f) dump the dictionnary in the file f"""

    def reload(self):
        """deserialize and lode objects from the file into python
        objects to dictionary __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                """open( self.__file_path, 'r') open the json file
                in read mode"""
                my_dict = json.load(f)
                """load(f.read) load the file f and read it"""
            for key, value in my_dict.items():
                """this for loop utilise a key and valiu to run
                    my_dict.items() and create a dictioanry of key and value"""
                new_object = key.split('.')
                class_name = new_object[0]
                """new_object is equal to key.split('.')[0]
                    this split the key and take the first part of the key"""
                if new_object in classes:
                    self.__objects[key] = classes[new_object](**value)
                    """this if statement is used to create a new object
                        with the class name of new_object and its value"""
        except FileNotFoundError:
            pass
