#!/usr/bin/python3
class MyList(list):
    def print_sorted(self):
        """
        Prints a sorted version of the list without modifying the original list.
        """
        sorted_list = sorted(self)  # Sort the list without changing the original
        print(sorted_list)
