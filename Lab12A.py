class Chair:
    def __init__(self, numOfLegs = 4, rolling = False, material = "plastic"):
        self.numOfLegs = numOfLegs
        self.rolling = rolling
        self.material = material


print("You are about to create a chair.")
numLegs = int(input("How many legs does your chair have: "))

rolling = input("Is your chair rolling (true/false): ")
if rolling.lower() == "true": rolling = True
else: rolling = False

material = input("What is your chair made of: ")

c1 = Chair(numLegs, rolling, material)

if c1.rolling: c1.rolling = "rolling"
else: c1.rolling = "not rolling"

print("Your chair has " + str(c1.numOfLegs) + " legs, is " + c1.rolling + ", and is made of " + c1.material + ".")
print("This program is going to change that.")

c1 = Chair()

if c1.rolling: c1.rolling = "rolling"
else: c1.rolling = "not rolling"

print("Your chair has " + str(c1.numOfLegs) + " legs, is " + c1.rolling + ", and is made of " + c1.material + ".")
