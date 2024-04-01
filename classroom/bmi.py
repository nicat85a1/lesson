def bmi_calculator():
    while True:
        try:
            weight = float(input("Enter your weight (kg): "))
            height = float(input("Enter your height (meters): "))
            if 0 <= weight <= 727 and 0 <= height <= 2.51:
                break
            else:
                print("Please enter a weight between 0 and 727")
                print("Please enter a height between 0 and 2.51")
        except ValueError:
            print("Please enter a valid number.")
    
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        status = "Underweight"
    elif bmi < 25:
        status = "Normal weight"
    elif bmi < 30:
        status = "Overweight"
    else:
        status = "Obese"

    print(f"BMI: {bmi:.2f} , Status: {status}.")