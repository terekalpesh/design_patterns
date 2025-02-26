# Memento design pattern

class Memento:
    def __init__(self, state):
        self.state = state

class Originator:           # Creating and setting the state, get the memento, restore the memento
    def __init__(self):
        self.state = 'initial string'

    def set_state(self, state):
        self.state = state

    def get_memento(self):
        return Memento(self.state)
    
    def restore_memento(self, memento):
        self.state = memento.state

class CareTaker:
    def __init__(self):
        self.mementos = []

    def add_memento(self, memento):
        self.mementos.append(memento)

    def get_memento(self, index):
        return self.mementos[index]
    

originator = Originator()
caretaker = CareTaker()

originator.set_state('My name is Jon')
memento = originator.get_memento()
caretaker.add_memento(memento)
print('Current state:- ', originator.state)

originator.set_state('My name is John')
print('Current state:- ', originator.state)

originator.restore_memento(caretaker.get_memento(0))
print('Current state:- ', originator.state)
