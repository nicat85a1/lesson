def budget(students):
    if not isinstance(students, (list, dict, tuple)):
        print("The 'students' parameter must be a list, dictionary, or tuple.")
        return
    if not all(isinstance(student, str) for student in students):
        print("Please enter a student name.")
        return
    students_budget = []
    for student in students:
        income_scholarship = get_valid_input(f"Enter {student} scholarship income: ")
        income_part_time = get_valid_input(f"Enter {student} part time income: ")
        income_pocket_money = get_valid_input(f"Enter {student} pocket money: ")
        income_freelancer = get_valid_input(f"Enter {student} freelance income: ")
        incomes = income_scholarship + income_part_time + income_pocket_money + income_freelancer

        expenses_school = get_valid_input(f"Enter {student} school expense: ")
        expenses_food = get_valid_input(f"Enter {student} food expense: ")
        expenses_clothes = get_valid_input(f"Enter {student} clothes expense: ")
        expenses_entertainment = get_valid_input(f"Enter {student} entertainment expense: ")
        expenses_transport = get_valid_input(f"Enter {student} transport expense: ")
        expenses_other = get_valid_input(f"Enter {student} other expense: ")
        expenses = expenses_school + expenses_food + expenses_clothes + expenses_entertainment + expenses_transport + expenses_other

        budget = incomes - expenses
        students_budget.append(f"{student}'s budget: {budget}")
    
    for line in students_budget:
        print(line)

def get_valid_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Please enter a value greater than 0.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter numbers only.")
