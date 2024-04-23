class Person:
    __wheel = 4
    def __init__(self, fname,lname):
        self.firstname=fname
        self.lastname=lname
        self.wheel = Person.__wheel

Person_ = Person("John", "Doe")

print(Person_.firstname, Person_.lastname)

class Student(Person):
    pass

Student_ = Student("Mike",Person_.lastname)

print(Student_.firstname, Student_.lastname, Person_.wheel)