# Mediator design pattern

from abc import ABC, abstractmethod

# Abstract mediator
class Mediator(ABC):
    @abstractmethod
    def send_message(self, message: str, user: 'User'):
        pass

# Concrete Mediator
class ChatRoom(Mediator):
    def __init__(self):
        self.users = []

    def add_user(self, user: 'User'):
        self.users.append(user)

    def send_message(self, message: str, user: 'User'):
        for u in self.users:
            if u != user:
                u.recieve_message(message)

# colleague
class User:
    def __init__(self, name: str, mediator: Mediator):
        self.name = name
        self.mediator = mediator
        self.mediator.add_user(self)

    def send_message(self, message: str):
        print(f'{self.name} sends: {message}')
        self.mediator.send_message(message, self)

    def recieve_message(self, message: str):
        print(f'{self.name} recieves: {message}')

# Usage
chat_room = ChatRoom()

# Creating users
alice = User('Alice', chat_room)
bob = User('Bob', chat_room)
charlie = User('Charlie', chat_room)

# Sending message from chatroom mediator
alice.send_message('Hi everyone!')
bob.send_message('Hello Alice!')
charlie.send_message('Good morning')