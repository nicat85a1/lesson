"""
class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = self.data[self.index]
        self.index += 1
        return value
    
    def __iter__(self):
        return self
    
my_list = [1, 2, 3, 4, 5]
my_iterator = MyIterator(my_list)

for item in my_iterator:
    print(item)
"""
class Range:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start >= self.stop:
            raise StopIteration
        result = self.start
        self.start += 1
        return result

print(list(Range(2, 6)))