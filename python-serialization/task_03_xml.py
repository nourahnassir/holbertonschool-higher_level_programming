#!/usr/init/env python3
"""Module for serializing and deserializing data using XML."""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serializes a Python dictionary into an XML file."""
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=False)


def deserialize_from_xml(filename):
    """Reads an XML file and returns a reconstructed Python dictionary."""
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        result_dict = {}
        for child in root:
            result_dict[child.tag] = child.text
        return result_dict
    except Exception:
        return None
