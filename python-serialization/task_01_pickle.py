#!/usr/bin/env python3
"""Module for serializing and deserializing custom classes using pickle."""
import pickle


class CustomObject:
    """A custom class with name, age, and is_student attributes."""

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Displays the object's attributes in the required format."""
        print(f"Name: {self.name}, Age: {self.age}, Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serializes the current instance and saves it to a file using pickle."""
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Loads and returns an instance of CustomObject from a file using pickle."""
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except Exception:
            return None
