# Command design pattern

# Receiver Classes
class Light:
    def turn_on(self):
        print('Light is ON')

    def turn_off(self):
        print('Light is OFF')

class Fan:
    def start(self):
        print('Fan is ON')

    def stop(self):
        print('Fan is OFF')

# Command Interface
class Command:
    def execute(self):
        pass

# Concrete Command for Light
class TurnOnLightCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_on()

class TurnOffLightCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_off()

# Concrete Command for Fan
class StartFanCommand(Command):
    def __init__(self, fan):
        self.fan = fan

    def execute(self):
        self.fan.start()

class StopFanCommand(Command):
    def __init__(self, fan):
        self.fan = fan

    def execute(self):
        self.fan.stop()

# Invoker
class RemoteControl:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def press_button(self):
        if self.command:
            self.command.execute()

# Client

# Creating receivers (devices)
light = Light()
fan = Fan()

# Creating concrete command
light_on = TurnOnLightCommand(light)
light_off = TurnOffLightCommand(light)
fan_on = StartFanCommand(fan)
fan_off = StopFanCommand(fan)

# Creating invoker (Remote control)
remote = RemoteControl()

# Turning on the light using the remote control
remote.set_command(light_on)
remote.press_button()

# Turning off the light using the remote control
remote.set_command(light_off)
remote.press_button()

# Starting the fan using the remote control
remote.set_command(fan_on)
remote.press_button()

# Stopping the fan using the remote control
remote.set_command(fan_off)
remote.press_button()