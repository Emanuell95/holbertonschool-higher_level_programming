#!/usr/bin/python3
"""Defines a class_to_json function."""
def class_to_json(obj):
    """Returns the dictionary description for JSON serialization of an object."""
    return obj.__dict__