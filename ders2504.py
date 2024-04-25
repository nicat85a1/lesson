from abc import ABC, abstractmethod

class shape:
    __wheel = 4
    def __init__(self,width,height):
        self.width=width
        self.height=height

    @abstractmethod
    def sell_by(self):
        return "By Kia Motors"
    

class Toyota(shape):
    def __init__(self,width,height):
        self.width=width
        self.height=height

kia=shape(10,20)

kia2=Toyota(10,20)

print(kia.sell_by())

print(kia2.__getattribute__('_shape__wheel'))

print(kia2.sell_by())

# encapulation

"""class RegisterCourse:
    def __init__(self):
        self.names="Nicat"
        self.surname="Huseynov"
        self.__exam1 = 74
        self.exam2 = 85

register = RegisterCourse()

print(register.names)
print(register.surname)
print(register.__getattribute__('_RegisterCourse__exam1'))
print(register.exam2)"""

# polymorphism

"""class Cae:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def move(self):
        print("drive")

class Boat:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def move(self):
        print("swim")

class Plane:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
        
    def move(self):
        print("fly")

car = Cae("BMW","X5")
boat = Boat("BMW","X5")
plane = Plane("BMW","X5")

for x in [car,boat,plane]:
    x.move()
"""

# inheritance polymorphism

"""class Vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def move(self):
        print("drive")

class Car(Vehicle):
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def move(self):
        print("mdrive")

        
class Boat(Vehicle):
    pass


car = Car("BMW","X5")
boat = Boat("BMW","X5")
vehicle = Vehicle("BMW","X5")


for x in [car,boat,vehicle]:
    x.move()"""