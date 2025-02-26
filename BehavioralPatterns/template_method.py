# Template design method

from abc import ABC, abstractmethod

class ThreeDaysTrip(ABC):
    @abstractmethod
    def transport(self):
        pass

    @abstractmethod
    def day1(self):
        pass

    @abstractmethod
    def day2(self):
        pass

    @abstractmethod
    def day3(self):
        pass

    @abstractmethod
    def back_to_home(self):
        pass

    def iternery(self):
        print('Trip is started')
        self.transport()
        self.day1()
        self.day2()
        self.day3()
        self.back_to_home()
        print('Trip is over')

class SouthTrip(ThreeDaysTrip):
    def transport(self):
        print('Go by train! check in to hotel')

    def day1(self):
        print('Day 1: Enjoy the hotel beach whole day')

    def day2(self):
        print('Day 2: Visit historical places and Enjoy cruise life at night')

    def day3(self):
        print('Day 3: Enjoy shopping day with family and go anywhere you wish')

    def back_to_home(self):
        print('Check out and go home by air')
        
class NorthTrip(ThreeDaysTrip):
    def transport(self):
        print('Go by air! check in to hotel')

    def day1(self):
        print('Day 1: Go to very heighted place and enjoy snow activity')

    def day2(self):
        print('Day 2: Enjoy river rafting and lavish dinner at night')

    def day3(self):
        print('Day 3: Enjoy shopping day with family and go anywhere you wish')

    def back_to_home(self):
        print('Check out and go home by air')



place = input('Where do you want to go?')
if place == 'north':
    trip = NorthTrip()
    trip.iternery()
elif place == 'south':
    trip = SouthTrip()
    trip.iternery()