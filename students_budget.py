def budget(students):
    students_budget = []
    for student in students:
        income_scholarship = int(input(f"Enter {student} scholarship income: "))
        income_part_time = int(input(f"Enter {student} part time income: "))
        income_pocket_money = int(input(f"Enter {student} pocket money: "))
        income_freelancer = int(input(f"Enter {student} freelance income: "))
        incomes = income_scholarship + income_part_time + income_pocket_money + income_freelancer
        expenses_school = int(input(f"Enter {student} school expense: "))
        expenses_food = int(input(f"Enter {student} food expense: "))
        expenses_clothes = int(input(f"Enter {student} clothes expense: "))
        expenses_entertainment = int(input(f"Enter {student} entertainment expense: "))
        expenses_transport = int(input(f"Enter {student} transport expense: "))
        expenses_other = int(input(f"Enter {student} other expense: "))
        expenses = expenses_school + expenses_food + expenses_clothes + expenses_entertainment + expenses_transport + expenses_other
        budget = incomes - expenses
        students_budget.append(f"{student}'s budget: {budget}")
    for line in students_budget:
        print(line)