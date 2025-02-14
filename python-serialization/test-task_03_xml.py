#!/usr/bin/env python3
"""Test the serialize_to_xml and deserialize_from_xml functions."""
from task_03_xml import serialize_to_xml, deserialize_from_xml

def main():
    """
    Test the serialize_to_xml and deserialize_from_xml functions.

    Serializes a sample dictionary to an XML file and prints a success message.
    Then deserializes the same XML file and prints the deserialized data.
    """
    sample_dict = {
        'name': 'John',
        'age': '28',
        'city': 'New York'
    }

    xml_file = "data.xml"
    serialize_to_xml(sample_dict, xml_file)
    print(f"Dictionary serialized to {xml_file}")

    deserialized_data = deserialize_from_xml(xml_file)
    print("\nDeserialized Data:")
    print(deserialized_data)

if __name__ == "__main__":
    main()