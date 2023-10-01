#BMI = weight/height**2
weight = float(input("What is your weight in kg: "))
height = float(input("What is your height in m: "))
result = weight / height ** 2
bmi = round(result , 1)
if bmi < 18.5:
    print(f"Your BMI is {bmi} , You are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi} , You have normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi} , You are overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi} , You are obese.")
else:
    print(f"Your BMI is {bmi} , You are clinically overweight.")