# State design pattern

from abc import ABC, abstractmethod

# Interface for Interface of states
class State(ABC):

    @abstractmethod
    def push_up_btn(self):
        pass

    @abstractmethod
    def push_down_btn(self):
        pass


class GroundFloor(State):
    
    def push_up_btn(self):
        self.elevator.set_elevator(FirstFloor())
        print('You are going to first floor')

    def push_down_btn(self):
        print('You are already at ground floor')


class FirstFloor(State):

    def push_up_btn(self):
        self.elevator.set_elevator(SecondFloor())
        print('You are going to second floor')

    def push_down_btn(self):
        self.elevator.set_elevator(GroundFloor())
        print('You are goint to ground floor')


class SecondFloor(State):

    def push_up_btn(self):
        print('You are already at top floor')

    def push_down_btn(self):
        self.elevator.set_elevator(FirstFloor())
        print('You are going to first floor')


class Elevator:
    def __init__(self) -> None:
        self.set_elevator(GroundFloor())

    def set_elevator(self, state: State) -> None:
        self._state = state
        self._state.elevator = self

    def push_up(self):
        self._state.push_up_btn()

    def push_down(self):
        self._state.push_down_btn()

    def current_state(self):
        print(f'You are at {self._state.__class__.__name__}')

elevator = Elevator()
elevator.current_state()

elevator.push_down()

elevator.push_up()
elevator.push_up()
elevator.current_state()

elevator.push_up()
elevator.current_state()