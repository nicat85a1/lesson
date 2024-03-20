def bmi_calculator(*args):
    weight = float(input("Enter your weight (kg): "))
    height = float(input("Enter your height (meters): "))
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        return f"{bmi:.2f}","Underweight"
    elif bmi < 25:
        return f"{bmi:.2f}","Normal weight"
    elif bmi < 30:
        return f"{bmi:.2f}","Overweight"
    else:
        return f"{bmi:.2f}","Obese"