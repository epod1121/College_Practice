#Lab5B

num = int(input("Please enter a value for the size: "))

print("\nThis is the requested ", num, "x", num, " box:")
for i in range(num):
  for j in range(num):
    print("*", end=" ")
  print()

print("This is the requested right-facing ", num, "x", num, " right-triangle:")
for i in range(num):
  for j in range(num):
    if (j <= i):
      print("*", end=" ")
  print()

print("This is the requested left-facing ", num, "x", num, " right-triangle:")
for i in range(num):
  for j in range(num):
    if (j < i):
      print(" ", end=" ")
    else:
      print("*", end=" ")
  print()