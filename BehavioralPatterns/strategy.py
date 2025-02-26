# Strategy design pattern

from abc import ABC, abstractmethod

# Strategy interface
class PasswordStrategy(ABC):
    @abstractmethod
    def generate(self):
        pass
    
class AlphaPasswordStrategy(PasswordStrategy):
    def generate(self):
        return 'abcdefghijklmnopqrstuvwxyz'
    
class NumericPasswordStrategy(PasswordStrategy):
    def generate(self):
        return '1234567890'
    
class DefaultPasswordStrategy(PasswordStrategy):
    def generate(self):
        return 'abcd1234'

# Main class   
class PasswordGenerator:
    def generate_password(self, password_gen: PasswordStrategy):
        return password_gen.generate()
    
pg = PasswordGenerator()
password = pg.generate_password(NumericPasswordStrategy())
print('Generated password: ', password)