#Lab3A

owed = float(input("Amount owed: "))
apr = float(input("APR: "))

minPayment = ((owed * apr) / 12) / 100
monthlyRate = apr / 12
print("\nMonthly percentage rate: ", round(monthlyRate, 3))
print("Minimum payment: $", round(minPayment, 2))