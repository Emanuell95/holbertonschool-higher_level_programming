#!/usr/bin/env python3
class SwimMixin:
    def swim(self):
        """Prints a message indicating that the creature is swimming."""
        print("The creature swims!")

class FlyMixin:
    def fly(self):
        print("The creature flies!")

class Dragon(SwimMixin, FlyMixin):
    def roar(self):
        print("The dragon roars!")

if __name__ == "__main__":
    draco = Dragon()
    draco.swim()
    draco.fly()
    draco.roar()
