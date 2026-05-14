name = input("Enter your name: ")
weight = float(input("Enter your weight: "))
height = float(input("Enter your height: "))

bmi = weight / (height ** 2)
bmi = round(bmi, 2)

print(f"\n--- BMI Report for {name} ---")
print(f"BMI: {bmi}")

if bmi < 18.5:
    print("Category: Underweight")
elif bmi < 25:
    print("Category: Normal weight")
elif bmi < 30:
    print("Category: Overweight")
else:
    print("Category: Obese")
