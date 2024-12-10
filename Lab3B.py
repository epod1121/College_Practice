#Lab3B

hours = 0
qualityPoints = 0

for i in range(0, 4):
  num = int(input("Course " + str(i + 1) + " hours: "))
  hours += num
  qualityPoints += int(input("Grade for course " + str(i + 1) + ": ")) * num

print("\nTotal hours: ", hours)
print("Total quality points: ", qualityPoints)
print("Your GPA for this semester is ", round(qualityPoints / hours, 2))