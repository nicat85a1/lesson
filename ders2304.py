# metod 1

class Person:
    __wheel = 4
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def person_info(self):
        return f"Name: {self.firstname} {self.lastname}, Wheels: {self.__wheel}"

Person_ = Person("John", "Doe")

class Student(Person):
    pass

Student_ = Student("Mike", Person_.lastname)

print(Student_.person_info())

# metod 2

class Person:
    __wheel = 4
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

Person_ = Person("John", "Doe")

class Student(Person):
    def student_info_2(self):
        return f"Name: {self.firstname} {self.lastname}, Wheels: {super().__getattribute__('_Person__wheel')}"

Student_ = Student("Mike", Person_.lastname)

print(Student_.student_info_2())

# metod 3

class Person:
    __wheel = 4
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
        self.wheel = Person.__wheel

Person_ = Person("John", "Doe")

class Student(Person):
    def student_info_3(self,wheel=Person_.wheel):
        self.wheel = wheel
        return f"Name: {self.firstname} {self.lastname}, Wheels: {self.wheel}"

Student_ = Student("Mike", Person_.lastname)

print(Student_.student_info_3())

# metod 4

class Person:
    __wheel = 4
    _Student__wheel = __wheel
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

Person_ = Person("John", "Doe")

class Student(Person):
    def student_info_4(self): # wheel=Person_.__wheel or # Person.__wheel
        wheel = Person_.__wheel # self.wheel = wheel
        return f"Name: {self.firstname} {self.lastname}, Wheels: {wheel}" # self.wheel

Student_ = Student("Mike", Person_.lastname)

print(Student_.student_info_4())