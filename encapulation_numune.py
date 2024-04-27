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
print(register.__getattribute__("_RegisterCourse__exam1"))
print(register.get_exam1())
print(register.exam2)"""

class RegisterCourse:
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
print(register.exam2)