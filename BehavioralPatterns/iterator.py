# Iterator design pattern

# Iterator Interface
class Iterator:
    def __iter__(self):
        raise NotImplementedError
    
    def __next__(self):
        raise NotImplementedError
    


# Concrete Iterator
class MyIterator(Iterator):
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self     # Self as an iterator
    
    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = self.data[self.index]
        self.index += 1
        return value
    
# Collection Interface
class Collection:
    def create_iterator(self):
        raise NotImplementedError
    
# Concrete Collections
class MyCollection(Collection):
    def __init__(self):
        self.data = []

    def add(self, value):
        self.data.append(value)

    def create_iterator(self):
        return MyIterator(self.data)
    
# Client
mycollection = MyCollection()   # Collection creating
mycollection.add(1)
mycollection.add(2)
mycollection.add(3)
mycollection.add(4)
mycollection.add(5)
print(mycollection)

myiterator = mycollection.create_iterator()     # Iterator for collection

for element in myiterator:
    print(element)
