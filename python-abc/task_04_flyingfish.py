#!/usr/bin/env python3
# Parent Classes
class Fish:
    def swim(self):
        """Prints a message indicating that the flying fish is swimming."""
        print("The flying fish is swimming!")
    
    def habitat(self):
        print("The fish lives in water")

class Bird:
    def fly(self):
        print("The bird is flying")
    
    def habitat(self):
        print("The bird lives in the sky")

# Child Class using Multiple Inheritance
class FlyingFish(Fish, Bird):
    def fly(self):
        print("The flying fish is soaring!")
    
    def swim(self):
        print("The flying fish is swimming!")
    
    def habitat(self):
        print("The flying fish lives both in water and the sky!")

# Testing the FlyingFish class
ff = FlyingFish()
ff.fly()      # Expected: The flying fish is soaring!
ff.swim()     # Expected: The flying fish is swimming!
ff.habitat()  # Expected: The flying fish lives both in water and the sky!

# Exploring the Method Resolution Order (MRO)
print(FlyingFish.mro())
