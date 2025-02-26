# Prototype design patterns

from abc import ABC, abstractmethod
import copy

# Prototype interface
class Prototype(ABC):
    @abstractmethod
    def clone(self):
        pass

# Concrete prototype
class EnemyPrototype(Prototype):
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def clone(self):
        return copy.deepcopy(self)
    
    def __str__(self):
        return f'Enemy(name = {self.name}, health = {self.health}, attack_power = {self.attack_power})'
    

# Client
def client_code(prototype: Prototype):
    prototype_clone = prototype.clone()
    print(f'Cloned enemy: {prototype_clone}')

    # Customize
    prototype_clone.health += 10
    prototype_clone.attack_power += 5
    print(f'Customized cloned enemy: {prototype_clone}')


# Original Enemy
og_enemy = EnemyPrototype('Goblin', 100, 15)
print(f'Original enemy: {og_enemy}')

client_code(og_enemy)