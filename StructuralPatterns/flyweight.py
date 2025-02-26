# Flyweight design pattern

class ComplexCars:
    def __init__(self):
        pass

    def cars(self, car_name):
        return f'ComplexPattern[{car_name}]'
    
class CarFamilies:
    car_family = {}

    def __new__(cls, name, car_family_id):
        try:
            id = cls.car_family[car_family_id]
        except KeyError:
            id = object.__new__(cls)
            cls.car_family[car_family_id] = id
        return id
    
    def set_car_info(self, car_info):
        cg = ComplexCars()
        self.car_info = cg.cars(car_info)

    def get_car_info(self):
        return self.car_info
    

car_data = (('a', 1, 'Audi'), ('a', 2, 'Ferrari'), ('b', 1, 'Audi'))
car_family_objects = []
for i in car_data:
        obj = CarFamilies(i[0], i[1])
        obj.set_car_info(i[2])
        car_family_objects.append(obj)

for i in car_family_objects:
    print('id = '+str(id(i)))
    print(i.get_car_info())
