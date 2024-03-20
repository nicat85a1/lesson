# evaluation.py dosyasında

def student_grades(students, subjects):
    grades = {student: [] for student in students}
    for student in students:
        for subject in subjects:
            while True:
                try:
                    grade = float(input(f"{student} {subject} grade: "))
                    if 0 <= grade <= 100:
                        break
                    else:
                        print("Please enter a grade between 0 and 100.")
                except ValueError:
                    print("Please enter a valid number.")
            grades[student].append(grade)
    return grades

def student_grades_averages(students, subjects):
    grades = student_grades(students, subjects)
    averages = {}
    for student, grades_list in grades.items():
        averages[student] = sum(grades_list) / len(grades_list)
    return averages

def student_evaluation(students, subjects):
    averages = student_grades_averages(students, subjects)
    for student, average in averages.items():
        if average < 51:
            print(f"{student}'s average grade: {average:.0f} 'F'")
        elif average >= 51 and average < 61:
            print(f"{student}'s average grade: {average:.0f} 'E'")
        elif average >= 61 and average < 71:
            print(f"{student}'s average grade: {average:.0f} 'D'")
        elif average >= 71 and average < 81:
            print(f"{student}'s average grade: {average:.0f} 'C'")
        elif average >= 81 and average < 91:
            print(f"{student}'s average grade: {average:.0f} 'B'")
        elif average >= 91 and average <= 100: 
            print(f"{student}'s average grade: {average:.0f} 'A'")