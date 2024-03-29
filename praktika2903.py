"""1. Write a Python class Employee with attributes like emp_id, emp_name, emp_salary, and emp_department and methods like calculate_emp_salary, emp_assign_department, and print_employee_details.
Sample Employee Data:
"ADAMS", "E7876", 50000, "ACCOUNTING"
"JONES", "E7499", 45000, "RESEARCH"
"MARTIN", "E7900", 50000, "SALES"
"SMITH", "E7698", 55000, "OPERATIONS"
Use 'assign_department' method to change the department of an employee.
Use 'print_employee_details' method to print the details of an employee.
Use 'calculate_emp_salary' method takes two arguments: salary and hours_worked, which is the number of hours worked by the employee. If the number of hours worked is more than 50, the method computes overtime and adds it to the salary. Overtime is calculated as following formula:
overtime = hours_worked - 50
Overtime amount = (overtime * (salary / 50))"""

class Employee():

    def __init__(self, emp_id, emp_name, emp_age, emp_salary, emp_department):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_age = emp_age
        self.emp_salary = emp_salary
        self.emp_department = emp_department
    
    def show(self):
        return self.emp_id, self.emp_name, self.emp_age, self.emp_salary, self.emp_department

employee1 = Employee(emp_id="E7876",emp_department="ACCOUNTING", emp_name=input("Enter employee name: "), emp_age=input("Enter employee age: "), emp_salary=input("Enter employee salary:"))
#employee2 = Employee(emp_id="E7499",emp_department="RESEARCH", emp_name=input("Enter employee name: "), emp_age=input("Enter employee age: "), emp_salary=input("Enter employee salary:"))
#employee3 = Employee(emp_id="E7900",emp_department="SALES", emp_name=input("Enter employee name: "), emp_age=input("Enter employee age: "), emp_salary=input("Enter employee salary:"))
#employee4 = Employee(emp_id="E7698",emp_department="OPERATIONS", emp_name=input("Enter employee name: "), emp_age=input("Enter employee age: "), emp_salary=input("Enter employee salary:"))

#print(employee1.show())
#print(employee2.show())
#print(employee3.show())
#print(employee4.show())

# change the department of an employee
def emp_assign_department(self=input("Enter employee id def: ")):
    if emp_assign_department == self:
        self.emp_department = input("Enter employee department: ")
        return self.emp_department
    else:
        print("Employee id not found")
emp_assign_department()
print(employee1.show())
"""
# print the details of an employee
def print_employee_details(self):
    print

def calculate_emp_salary(self,salary,hours_worked):
    if hours_worked > 50:
        overtime = hours_worked - 50
        overtime_ammount = (overtime * (salary / 50))
"""