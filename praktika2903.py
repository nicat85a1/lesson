class Employee:

    def __init__(self, emp_id, emp_name, emp_age, emp_salary, emp_department):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_age = emp_age
        self.emp_salary = emp_salary
        self.emp_department = emp_department
    
    def print_employee_details(self):
        return self.emp_id, self.emp_name, self.emp_age, self.emp_salary, self.emp_department

    @classmethod
    def emp_assign_department(cls, emp_id_check, new_department):
        for employee in employees:
            if employee.emp_id == emp_id_check:
                employee.emp_department = new_department
                print(f"Employee id {emp_id_check} department is changed to {new_department}")
                return
        print("Employee id not found")
    
    def calculate_emp_salary(self, hours_worked):
        salary = self.emp_salary
        if hours_worked > 50:
            overtime = hours_worked - 50
            overtime_amount = (overtime * (salary / 50))
            self.emp_salary = self.emp_salary + overtime_amount
            return self.emp_salary
        else:
            return self.emp_salary

employees = [
    Employee(emp_id="E7876", emp_name=input("Enter employee name: "), emp_age=int(input("Enter employee age: ")), emp_salary=int(input("Enter employee salary: ")), emp_department="ACCOUNTING"),
    Employee(emp_id="E7499", emp_name=input("Enter employee name: "), emp_age=int(input("Enter employee age: ")), emp_salary=int(input("Enter employee salary: ")), emp_department="RESEARCH"),
    Employee(emp_id="E7900", emp_name=input("Enter employee name: "), emp_age=int(input("Enter employee age: ")), emp_salary=int(input("Enter employee salary: ")), emp_department="SALES"),
    Employee(emp_id="E7698", emp_name=input("Enter employee name: "), emp_age=int(input("Enter employee age: ")), emp_salary=int(input("Enter employee salary: ")), emp_department="OPERATIONS")
]

Employee.emp_assign_department(emp_id_check=input("Enter Employee id: "), new_department=input("Enter new Department: "))

employees[0].calculate_emp_salary(hours_worked=int(input(f"Enter hours worked {employees[0].emp_id}: ")))
employees[1].calculate_emp_salary(hours_worked=int(input(f"Enter hours worked {employees[0].emp_id}: ")))
employees[2].calculate_emp_salary(hours_worked=int(input(f"Enter hours worked {employees[0].emp_id}: ")))
employees[3].calculate_emp_salary(hours_worked=int(input(f"Enter hours worked {employees[0].emp_id}: ")))

for employee in employees:
    print(employee.print_employee_details())