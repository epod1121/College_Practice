#Assignment2A

age = int(input("Enter your age: "))

ticketPrice = 0

if (age < 12):
  ticketPrice = 8
elif (age >= 12 and age <= 17 or age >= 65):
  ticketPrice = 10
else:
  club = input("Are you a member of the cinema club (yes or no)? ")
  if (club == "no"):
    ticketPrice = 15
  else:
    ticketPrice = 12

print("Your ticket price is: $" + str(ticketPrice))