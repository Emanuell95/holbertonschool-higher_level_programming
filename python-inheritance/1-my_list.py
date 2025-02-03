#!/usr/bin/python3
class MyList(list):
    def print_sorted(self):
        
        """
        Prints a sorted version of the list
        """
        sorted_list = sorted(self)
        print(sorted(self))

my_list = MyList([1,2,5,8,3])
my_list.print_sorted()
