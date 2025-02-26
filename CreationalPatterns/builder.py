# Builder design pattern

# Product class
class MobilePhone:
    def __init__(self, os, screen_size, battery, ram):
        self.os = os
        self.screen_size = screen_size
        self.battery = battery
        self.ram = ram

    def __str__(self):
        return f'MobilePhone [OS = {self.os}, Screen Size = {self.screen_size}, Battery = {self.battery}mAH, RAM = {self.ram}GB]'
    
# Builder Interface
class MobilePhoneBuilder:
    def set_os(self, os):
        raise NotImplementedError
    
    def set_screen_size(self, screen_size):
        raise NotImplementedError
    
    def set_battery(self, battery):
        raise NotImplementedError
    
    def set_ram(self, ram):
        raise NotImplementedError
    
    def build(self):
        raise NotImplementedError
    
# Concrete Builder
class AndroidPhoneBuilder(MobilePhoneBuilder):
    def __init__(self):
        self.os = 'Android'
        self.screen_size = None
        self.battery = None
        self.ram = None

    def set_screen_size(self, screen_size):
        self.screen_size = screen_size
        return self
    
    def set_battery(self, battery):
        self.set_battery = battery
        return self
    
    def set_ram(self, ram):
        self.ram = ram
        return self
    
    def build(self):
        return MobilePhone(self.os, self.screen_size, self.battery, self.ram)

# Concrete Builder
class IOSPhoneBuilder(MobilePhoneBuilder):
    def __init__(self):
        self.os = 'iOS'
        self.screen_size = None
        self.battery = None
        self.ram = None

    def set_screen_size(self, screen_size):
        self.screen_size = screen_size
        return self
    
    def set_battery(self, battery):
        self.battery = battery
        return self
    
    def set_ram(self, ram):
        self.ram = ram
        return self
    
    def build(self):
        return MobilePhone(self.os, self.screen_size, self.battery, self.ram)
    

# Director
class MobilePhoneDirector:
    def __init__(self, builder):
        self.builder = builder

    def construct_android_phone(self):
        return (self.builder
                .set_screen_size('5.5-inch')
                .set_battery(3000)
                .set_ram(4)
                .build()
                )
    
    def construct_ios_phone(self):
        return (self.builder
                .set_screen_size('6-inch')
                .set_battery(4000)
                .set_ram(6)
                .build()
                )
    
# client
android_builder = AndroidPhoneBuilder()
director = MobilePhoneDirector(android_builder)
android = director.construct_android_phone()
print(android)

ios_builder = IOSPhoneBuilder()
director = MobilePhoneDirector(android_builder)
android = director.construct_android_phone()
print(android)
