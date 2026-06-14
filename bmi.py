height = float(input("enter your heigh in cm: "))
weight = float(input("enter your weight in kg: "))
bmi = weight / (height / 100) **2
print("your bmi is", round(bmi,2))
if bmi <= 18.4:
    print("you are underweight")
elif bmi <= 24.9:
    print("you are healthy.")
elif bmi <= 29.9:
    print("youare overweight.")
elif bmi <= 34.9:
    print("you are serverely over weight.")
elif bmi <= 39.9: 
    print("you are obese.")
else:
    print("you are severely obese.")

