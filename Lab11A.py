# Lab11A

def allMath(num1, num2):
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2
    if num2 == 0:
        division = None
        floorDivision = None
        modulus = None
    else:
        division = num1 / num2
        floorDivision = num1 // num2
        modulus = num1 % num2

    power = num1 ** num2

    return addition, subtraction, multiplication, division, floorDivision, modulus, power


num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))

print(allMath(num1, num2))
