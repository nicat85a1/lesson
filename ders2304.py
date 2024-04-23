class Person:
    __wheel = 4
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
        self.wheel = Person.__wheel

    def person_info(self):
        return f"Name: {self.firstname} {self.lastname}, Wheels: {Person.__wheel}" # Wheels: {self.__wheel}

Person_ = Person("John", "Doe")

class Student(Person):
    def student_info(self,wheel=Person_.wheel):
        self.wheel = wheel
        return f"Name: {self.firstname} {self.lastname}, Wheels: {self.wheel}"

Student_ = Student("Mike", Person_.lastname)

print(Person_.person_info())

print(Student_.person_info())

print(Student_.student_info())