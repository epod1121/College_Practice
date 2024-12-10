#Lab3C

small = int(input("Enter the number of small sandwhiches: "))
medium = int(input("Enter the number of medium sandwhiches: "))
large = int(input("Enter the number of large sandwhiches: "))
xLarge = int(input("Enter the number of extra-large sandwhiches: "))

print("\nYou've entered: ", small, "small sandwhiches")
print("You've entered: ", medium, "medium sandwhiches")
print("You've entered: ", large, "large sandwhiches")
print("You've entered: ", xLarge, "extra-large sandwhiches")

smallTime = 30
mediumTime = 60
largeTime = 75
xLargeTime = 135

totalTime = (small * smallTime) + (medium * mediumTime) + (
    large * largeTime) + (xLarge * xLargeTime)

print("\nTotal cooking time is: ", totalTime // 60, "minutes and",
      totalTime % 60, "seconds")