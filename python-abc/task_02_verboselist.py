#!/usr/bin/env python3
class VerboseList(list):
    def append(self, item):
        super().append(item)
        print(f"Added {item} to the list.")

    def extend(self, iterable):
        length_before = len(self)
        super().extend(iterable)
        length_added = len(self) - length_before
        print(f"Extended the list with {length_added} items.")

    def remove(self, item):
        print(f"Removed {item} from the list.")
        super().remove(item)

    def pop(self, index=-1):
        item = self[index]
        print(f"Popped {item} from the list.")
        return super().pop(index)

# Testing the VerboseList class
if __name__ == "__main__":
    vlist = VerboseList()
    vlist.append(10)
    vlist.append(20)
    vlist.extend([30, 40, 50])
    vlist.remove(20)
    vlist.pop()
    vlist.pop(0)
