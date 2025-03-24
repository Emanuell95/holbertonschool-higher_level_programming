#!/usr/bin/python3
Rectangle = __import__('1-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print(my_rectangle.__dict__)

my_rectangle.width = 10
my_rectangle.height = 3
<<<<<<< HEAD
print(my_rectangle.__dict__)
=======
print(my_rectangle.__dict__)
>>>>>>> 524550f753e0cae514ef13d2489a5c00a12f8bc3
