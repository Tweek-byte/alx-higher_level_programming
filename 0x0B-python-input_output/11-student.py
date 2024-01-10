#!/usr/bin/python3
"""
Contains the Student class
"""


class Student:
    """Representation of a student"""
    def __init__(self, first_name, last_name, age):
        """Initializes the student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a dictionary named Student"""
        if attrs is None:
            return self.__dict__
        new_dict = {}
        for a in attrs:
            try:
                new_dict[a] = self.__dict__[a]
            except AttributeError:
                pass
        return new_dict

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance."""
        for key in json:
            if hasattr(self, key):
                setattr(self, key, json[key])
