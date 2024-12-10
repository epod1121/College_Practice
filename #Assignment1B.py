#Assignment1B

loanAmount = float(input("Enter the loan amount: "))
interest = float(input("Enter the annual interest rate (in %): "))
term = int(input("Enter the loan term (in years): "))

monthlyInterest = interest / 1200
termInMonths = term * 12
monthlyPayment = (loanAmount * monthlyInterest * (1 + monthlyInterest)**termInMonths 
  / ((1 + monthlyInterest)**termInMonths - 1))

print("Your monthly payment is: $", round(monthlyPayment, 2))