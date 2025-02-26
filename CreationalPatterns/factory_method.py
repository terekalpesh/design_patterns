# The Factory Method

from abc import ABCMeta, abstractmethod

class IProduct(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod

    def create_object():
        "An abstract interface method"

class ConcreteProductA(IProduct):
    "A Concrete Class that implements the IProduct interface"

    def __init__(self):
        self.name = 'ConcreteProductA'

    def create_object(self):
        self

class ConcreteProductB(IProduct):
    "A Concrete Class that implements the IProduct interface"

    def __init__(self):
        self.name = 'ConcreteProductB'

    def create_object(self):
        self

class ConcreteProductC(IProduct):
    "A Concrete Class that implements the IProduct interface"

    def __init__(self):
        self.name = 'ConcreteProductC'

    def create_object(self):
        self


class Creator:
    "The Factory class"

    @staticmethod
    def create_object(some_property):
        "A static method to get a concrete product"
        if some_property == 'a':
            return ConcreteProductA()
        if some_property == 'b':
            return ConcreteProductB()
        if some_property == 'c':
            return ConcreteProductC()
        return None

# The client
PRODUCT = Creator.create_object('b')
print(PRODUCT.name)