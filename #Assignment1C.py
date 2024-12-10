#Assignment1C

weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in centimeters: "))

height /= 100

bmi = weight / (height * height)

print("Your BMI is: ", round(bmi, 1))

if(bmi < 18.5):
  category = 1
elif(bmi >= 18.5 and bmi < 24.9):
  category = 2
elif(bmi >= 25 and bmi < 29.9):
  category = 3
else:
  category = 4

print("You are classified as: ", category, " weight")