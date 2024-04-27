"""from abc import ABC, abstractmethod

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

print(kia2.sell_by())"""

"""from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class StripePaymentProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Stripe ile {amount} tutarında ödeme işleniyor.")

class PaypalPaymentProcessor(PaymentProcessor):
    def process_paymentt(self, amount):
        print(f"Paypal ile {amount} tutarında ödeme işleniyor.")

Stripe = StripePaymentProcessor()

Paypal = PaypalPaymentProcessor()

print(Stripe.process_payment(100))

print(Paypal.process_paymentt(100))"""

"""class PaymentProcessor:
    def process_payment(self, amount):
        raise NotImplementedError("Her alt sınıfın bu metodu uygulaması gerekiyor.")

class StripePaymentProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Stripe ile {amount} tutarında ödeme işleniyor.")

class PaypalPaymentProcessor(PaymentProcessor):
    def process_paymentt(self, amount):
        print(f"Paypal ile {amount} tutarında ödeme işleniyor.")

Stripe = StripePaymentProcessor()

Paypal = PaypalPaymentProcessor()

print(Stripe.process_payment(100))

print(Paypal.process_paymentt(100))"""

# encapulation

"""class RegisterCourse:
    def __init__(self):
        self.names="Nicat"
        self.surname="Huseynov"
        self.__exam1 = 74
        self.exam2 = 85

register = RegisterCourse()

register.__exam1 = 90

print(register.names)
print(register.surname)
print(register.__getattribute__('_RegisterCourse__exam1'))
print(register.exam2)"""

"""class RegisterCourse:
    def __init__(self):
        self.names = "Nicat"
        self.surname = "Huseynov"
        self.__exam1 = 74
        self.exam2 = 85

register = RegisterCourse()

register._RegisterCourse__exam1 = 90

register2 = RegisterCourse()

print(register2.__getattribute__('_RegisterCourse__exam1'))

print(register.names)
print(register.surname)
print(register._RegisterCourse__exam1)
print(register.__getattribute__('_RegisterCourse__exam1'))
print(register.exam2)"""

"""class RegisterCourse:
    def __init__(self):
        self.names = "Nicat"
        self.surname = "Huseynov"
        self.__exam1 = 74
        self.exam2 = 85
    
    def get_exam1(self):
        return self.__exam1
    def change_exam1(self, new_exam1):
        self.__exam1 = new_exam1

register = RegisterCourse()
register.change_exam1(90)

register2 = RegisterCourse()

print(register2.get_exam1())

print(register.names)
print(register.surname)
print(register._RegisterCourse__exam1)
print(register.get_exam1())
print(register.exam2)"""

# polymorphism

"""class Cae:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def move(self):
        print("drive")

class Boat(Cae):

    def move(self):
        print("swim")

class Plane(Cae):
        
    def move(self):
        print("fly")

car = Cae("BMW","X5")
boat = Boat("BMW","X5")
plane = Plane("BMW","X5")

for x in [car,boat,plane]:
    x.move()"""

# inheritance polymorphism

class Vehicle:
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
    x.move()