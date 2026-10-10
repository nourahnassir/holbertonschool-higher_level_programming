#!/usr/bin/env python3
"""Module that provides basic serialization and deserialization functions."""
import json
def serialize_and_save_to_file(data, filename):
    """Serializes a Python dictionary to a JSON file."""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Loads and deserializes a JSON file to a Python dictionary."""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
