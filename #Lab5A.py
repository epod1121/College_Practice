#Lab5A

print("Please enter 10 numbers and this program will display the largest.")
largest = 0

for i in range(0, 10):
  num = int(input("Please enter number " + str(i + 1) + ": "))
  if (i == 0):
    largest = num
  else:
    if (num > largest):
      largest = num