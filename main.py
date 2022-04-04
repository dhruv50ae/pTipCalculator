height = input("Enter your height in meters: ")
weight = input("Enter your weight in kilograms: ")
bmi = int(weight) / round(float(height), 2) ** 2
print(f"Your BMI is {bmi}")
