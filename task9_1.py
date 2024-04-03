class Employee:

    def __init__(self, emp_id, emp_name, emp_age, emp_salary, emp_department):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_age = emp_age
        self.emp_salary = emp_salary
        self.emp_department = emp_department
    
    def print_employee_details(self):
        return self.emp_id, self.emp_name, self.emp_age, self.emp_salary, self.emp_department
    
    def calculate_emp_salary(self, salary,hours_worked):
        salary = self.emp_salary
        if hours_worked > 50:
            overtime = hours_worked - 50
            overtime_amount = (overtime * (self.emp_salary / 50))
            self.emp_salary += overtime_amount
        return self.emp_salary

    def emp_assign_department(self, new_department):
        self.emp_department = new_department
        print(f"Employee id {self.emp_id} department is changed to {new_department}")

def input_age(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 120 or value < 0:
                print("Please enter a value greater than 0 and less than 120.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter numbers only.")

def input_salary(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Please enter a positive value.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter numbers only.")

employees = [
    Employee(emp_id="E7876", emp_name="Alice", emp_age=input_age("Enter employee age: "), emp_salary=input_salary("Enter employee salary: "), emp_department="ACCOUNTING"),
    Employee(emp_id="E7499", emp_name="Bob", emp_age=input_age("Enter employee age: "), emp_salary=input_salary("Enter employee salary: "), emp_department="RESEARCH"),
    Employee(emp_id="E7900", emp_name="Charlie", emp_age=input_age("Enter employee age: "), emp_salary=input_salary("Enter employee salary: "), emp_department="SALES"),
    Employee(emp_id="E7698", emp_name="Diana", emp_age=input_age("Enter employee age: "), emp_salary=input_salary("Enter employee salary: "), emp_department="OPERATIONS")
]

for employee in employees:
    print(employee.print_employee_details())

"""def emp_assign_department(self, new_department):
        self.emp_department = new_department
        print(f"Employee id {self.emp_id} department is changed to {new_department}")"""

emp_id_check = input("Enter Employee id: ")
new_department = input("Enter new Department: ")
for employee in employees:
    if employee.emp_id == emp_id_check:
        employee.emp_assign_department(new_department)
        break
else:
    print("Employee id not found")

for employee in employees:
    employee.calculate_emp_salary(employee.emp_salary,hours_worked=int(input(f"Enter hours worked for {employee.emp_id}: ")))

for employee in employees:
    print(employee.print_employee_details())