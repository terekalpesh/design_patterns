from abc import ABC, abstractmethod

# Component class
class Pizza(ABC):
    @abstractmethod
    def cost(self):
        pass

# Concrete component class
class PlainPizza(Pizza):
    def cost(self):
        return 70  #Base price
    

# Decorator Class
class ToppingDecorator(Pizza):
    def __init__(self, pizza):
        self._pizza = pizza

    def cost(self):
        return self._pizza.cost()
    
# Concrete Decorators
class CheeseDecorator(ToppingDecorator):
    def cost(self):
        return self._pizza.cost() + 10.0
    
class OlivesDecorator(ToppingDecorator):

    def cost(self):
        return self._pizza.cost() + 20.0
    
class MushroomsDecorator(ToppingDecorator):
    def cost(self):
        return self._pizza.cost() + 15.0
    

pizza = PlainPizza()
print('plain pizza cost: ', pizza.cost(), 'Rs.')

pizza_with_cheese = CheeseDecorator(pizza)
print('Pizza with Cheese cost: ', pizza_with_cheese.cost(), 'Rs.')

pizza_with_cheese_and_olives = OlivesDecorator(pizza_with_cheese)
print('Pizza with Cheese and Olives cost: ', pizza_with_cheese_and_olives.cost(), 'Rs.')

pizza_with_cheese_olives_and_mushrooms = MushroomsDecorator(pizza_with_cheese_and_olives)
print('Pizza with Cheese, Olives and Mushrooms cost: ', pizza_with_cheese_olives_and_mushrooms.cost())


