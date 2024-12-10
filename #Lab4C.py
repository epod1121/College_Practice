#Lab4C
print("Welcome!\nYou have $1000 in your account.")
money = 1000
YorN = True

while (YorN):
  print("\nMenu\n0) Make a deposit\n1) Make a withdrawal\n2) Display account value")
  choice = int(input("\nPlease make a selection: "))

  match choice:
    case 0:
      deposit = int(input("How much would you like to deposit? "))
      money += deposit
      print("Your current balance is $", money)

      YorN = input("\nWould you like to return to the main menu (Y/N)? ")

      if (YorN.lower() == "n"):
        YorN = False
    case 1:
      withdraw = int(input("How much would you like to withdraw? "))
      if (withdraw > money):
        print(
            "Not enough balance. Withdrawal cancelled. \nYour current balance is $",
            money)
      else:
        money -= withdraw
        print("Your current balance is $", money)

      YorN = input("\nWould you like to return to the main menu (Y/N)? ")

      if (YorN.lower() == "n"):
        YorN = False
    case 2:
      print("Your current balance is $", money)
      YorN = input("\nWould you like to return to the main menu (Y/N)? ")

      if (YorN.lower() == "n"):
        YorN = False

print("\nThank you for banking with us!")