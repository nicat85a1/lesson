"""class Person:
    __wheel = 4
    _Student__wheel = __wheel
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
        self.wheel = Person.__wheel

    def person_info(self):
        return f"Name: {self.firstname} {self.lastname}, Wheels: {Person.__wheel}" # Wheels: {self.__wheel}

Person_ = Person("John", "Doe")

class Student(Person):
    def student_info(self,wheel=Person.__wheel):
        self.wheel = wheel
        return f"Name: {self.firstname} {self.lastname}, Wheels: {self.wheel}"
    def student_info_3(self,wheel=Person_.wheel):
        self.wheel = wheel
        return f"Name: {self.firstname} {self.lastname}, Wheels: {self.wheel}"
    def student_info_2(self):
        return f"Name: {self.firstname} {self.lastname}, Wheels: {super().__getattribute__('_Person__wheel')}"
    def student_info_4(self):
        wheel = Person.__wheel
        return f"Wheels: {wheel}"

Student_ = Student("Mike", Person_.lastname)

print(Person_.person_info())

print(Student_.person_info())

print(Student_.student_info())

print(Student_.student_info_2())

print(Student_.student_info_3())

print(Student_.student_info_4())"""

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
    _Student__wheel = __wheel
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

Person_ = Person("John", "Doe")

class Student(Person):
    def student_info(self,wheel=Person.__wheel):
        self.wheel = wheel
        return f"Name: {self.firstname} {self.lastname}, Wheels: {self.wheel}"

Student_ = Student("Mike", Person_.lastname)

print(Student_.student_info())

# metod 3

class Person:
    __wheel = 4
    _Student__wheel = __wheel
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

Person_ = Person("John", "Doe")

class Student(Person):
    def student_info_3(self,wheel=Person_.__wheel):
        self.wheel = wheel
        return f"Name: {self.firstname} {self.lastname}, Wheels: {self.wheel}"

Student_ = Student("Mike", Person_.lastname)

print(Student_.student_info_3())

# metod 4

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

# metod 5

class Person:
    __wheel = 4
    _Student__wheel = __wheel
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

Person_ = Person("John", "Doe")

class Student(Person):
    def student_info_4(self):
        wheel = Person.__wheel
        return f"Name: {self.firstname} {self.lastname}, Wheels: {wheel}"

Student_ = Student("Mike", Person_.lastname)

print(Student_.student_info_4())

# metod 6

class Person:
    __wheel = 4
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
        self.wheel = Person.__wheel

Person_ = Person("John", "Doe")

class Student(Person):
    def student_info_6(self,wheel=Person_.wheel):
        self.wheel = wheel
        return f"Name: {self.firstname} {self.lastname}, Wheels: {self.wheel}"

Student_ = Student("Mike", Person_.lastname)

print(Student_.student_info_6())