# Facade design pattern

# Subsystems  - (DVDPlayer, Projector, SoundSystem and Lights)
class DVDPlayer:
    def on(self):
        print('DVD Player is now ON.')

    def play(self, movie):
        print(f'Playing movie: {movie}')

    def off(self):
        print('DVD Player is now OFF.')


class Projector:
    def on(self):
        print('Projector is ON.')

    def set_input(self, input_source):
        print(f'Projector input set to: {input_source}.')

    def off(self):
        print('Projector is OFF.')


class SoundSystem:
    def on(self):
        print('Sound system is ON.')

    def set_volume(self, level):
        print(f'Setting volume to {level}.')

    def off(self):
        print('Sound system is now OFF.')


class Lights:
    def dim(self):
        print('Dimming lights.')

    def on(self):
        print('Lights are ON.')


# Facade Class
class HomeTheaterFacade:
    def __init__(self):
        self.dvd = DVDPlayer()
        self.projector = Projector()
        self.sound_system = SoundSystem()
        self.lights = Lights()

    def watch_movie(self, movie, volume):
        print('Get ready to watch a movie...')
        self.lights.dim()
        self.projector.on()
        self.projector.set_input('DVD')
        self.sound_system.on()
        self.sound_system.set_volume(volume)
        self.dvd.on()
        self.dvd.play(movie)

    def end_movie(self):
        print('Shutting down the home theater...')
        self.dvd.off()
        self.projector.off()
        self.sound_system.off()
        self.lights.on()

# Client
home_theater = HomeTheaterFacade()

home_theater.watch_movie('Avengers', 10)
print('\n')
home_theater.end_movie()