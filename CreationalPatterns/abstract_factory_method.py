# Abstract factory method

from abc import ABC, abstractmethod

class IProduct(ABC):
    "A Hypothetical Class Interface (Product)"

    @staticmethod
    @abstractmethod
    def create_object():
        pass


class ConcreteProductA(IProduct):
    "A Concrete Class that implements the IProduct interface"
    def __init__(self):
        self.name = 'ConcreteProductA'

    def create_object(self):
        return self


class ConcreteProductB(IProduct):
    "A Concrete Class that implements the IProduct interface"
    def __init__(self):
        self.name = 'ConcreteProductB'

    def create_object(self):
        return self


class ConcreteProductC(IProduct):
    "A Concrete Class that implements the IProduct interface"
    def __init__(self):
        self.name = 'ConcreteProductC'

    def create_object(self):
        return self


class Creator:
    "The Factory Class"

    @staticmethod
    def create_object(some_property):
        if some_property == 'a':
            return ConcreteProductA()
        if some_property == 'b':
            return ConcreteProductB()
        if some_property == 'c':
            return ConcreteProductC()
        return None
    
PRODUCT = Creator.create_object('b')
print(PRODUCT.name)
