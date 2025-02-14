#!/usr/bin/env python3
"""XML serialization and deserialization."""
import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """Serializes a Python dictionary to an XML file."""
    try:
        root = ET.Element("data")
        
        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)
        
        tree = ET.ElementTree(root)
        tree.write(filename)
        return True
    except Exception as e:
        print(f"Error during XML serialization: {e}")
        return False

def deserialize_from_xml(filename):
    """Deserializes an XML file to a Python dictionary."""
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        
        result = {}
        for child in root:
            # Simple conversion logic; can be expanded for complex types
            value = child.text
            if value.isdigit():
                result[child.tag] = int(value)
            else:
                try:
                    result[child.tag] = float(value)
                except ValueError:
                    result[child.tag] = value
        
        return result
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return None
    except Exception as e:
        print(f"Error during XML deserialization: {e}")
        return None

