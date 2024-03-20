"""
# Maliyyə Sənayesi:

# "Boris","Benjamin","Cedric","Drake","Elliott","Francis","Herman","Luther","Morgan","Miles","Richard","Martel"

from students_budget import budget

students = ["Albert","Arthur"]

budget(students)

# Səhiyyə Sənayesi:

from bmi import bmi_calculator

result,status = bmi_calculator()
print(f"BMI: {result} , Status: {status}.")
"""

# Təhsil Sənayesi:

# qiyməti müəyyən etmək üçün funksiyalardan istifadə edin və qiymətləndirmə meyarları üçün if-else ifadələrini birləşdirin.

def student_grades():
    students = ["Albert", "Arthur"]
    subjects = ["English", "informatics", "math", "python"]
    grades = {student: [] for student in students}
    for student in students:
        for subject in subjects:
            grade = float(input(f"{student} {subject} grade: "))
            grades[student].append(grade)
    return grades

def student_grades_average(grades):
    averages = {}
    for student, grades_list in grades.items():
        averages[student] = sum(grades_list) / len(grades_list)
    return averages

grades = student_grades()
averages = student_grades_average(grades)
for student, average in averages.items():
    print(f"{student}'s average grade: {average}")
