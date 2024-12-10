#Lab4B
print("Welcome!")

num = int(input("Please input a number: "))

choice = int(
    input("\nWhat would you like to do to this number:" +
          "\n0) Get the additive inverse of the number" +
          "\n1) Get the reciprocal of the number" + "\n2) Square the number" +
          "\n3) Cube the number" + "\n4) Exit the program" + "\n"))

match choice:
  case 0:
    print("The additive inverse of ", num, " is ", -num)
  case 1:
    if (num != 0):
      print("The reciprocal of ", num, " is ", 1 / num)
    else:
      print("Cannot divide by 0!")
  case 2:
    print("The square of ", num, " is ", num**2)
  case 3:
    print("The cube of ", num, " is ", num**3)
  case 4:
    print("Thank you, goodbye!")
  case _:
    print("Invalid option!")