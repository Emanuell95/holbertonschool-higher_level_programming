#!/usr/bin/env python3
class CountedIterator:
    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.count = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration
    
    def get_count(self):
        return self.count

# Testing the CountedIterator class
if __name__ == "__main__":
    numbers = [10, 20, 30, 40, 50]
    counted_iter = CountedIterator(numbers)
    
    for num in counted_iter:
        print(f"Next item: {num}, Items iterated: {counted_iter.get_count()}")
