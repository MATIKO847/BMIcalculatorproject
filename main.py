print("WELCOME TO THE BMI CALCULATOR")
height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

new_height = float(height)

new_weight = int(weight)

BMI = (new_weight) /(new_height**2)

print(int(BMI))