"""class Car:
    def __init__(self, brand, model, speed):
        self.brand = brand
        self.model = model
        self.speed = speed
    
    def show(self):
        return self.brand, self.speed
    
obj = Car("BMW", "X5", 200)
print(obj.show())"""

"""max_ = int(input("Введите максимальную скорость: "))
km_ = int(input("Введите пробег: "))

class Vehicle:
    def __init__(self, max_speed, km):
        self.max_speed = max_speed
        self.km = km
    def times(self):
        return self.km // self.max_speed
    
obj = Vehicle(max_, km_)
print(obj.times())"""

class BusSystem:
    gedis = 1
    def __init__(self, category=input("Введите категорию: "), age=int(input("Введите возраст: ")), cash=float(input("Введите сумму: "))):
        self.category = category
        self.age = age
        self.cash = cash

    def access(self):
        if self.age < 18:
            self.cash = self.cash - (self.gedis * 0.2)
            return self.cash
        elif self.age < 18 and self.category == "student":
            self.cash = self.cash - (self.gedis * 0.05)
            return self.cash
        elif 18 < self.age < 50:
            self.cash = self.cash - (self.gedis * 0.4)
            return self.cash
        elif 18 < self.age < 50 and self.category == "qazi":
            self.cash = self.cash - (self.gedis * 0.1)
            return self.cash
        else:
            return self.cash
        
bus = BusSystem()

print(bus.access())