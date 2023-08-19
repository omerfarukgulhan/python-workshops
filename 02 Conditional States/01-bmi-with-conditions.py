height = float(input("Height:"))
weight = int(input("Weight:"))

bmi = weight / (height**2)

if bmi < 18.5:
    print("Thinn")
elif bmi >= 18.5 and bmi < 25:
    print("Normal")
elif bmi >= 25 and bmi < 30:
    print("Over weight")
else:
    print("Obese")
