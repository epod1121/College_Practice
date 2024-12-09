class Dog:
    def __init__(self, age, weight, name, furColor, breed):
        self.age = age
        self.weight = weight
        self.name = name
        self.furColor = furColor
        self.breed = breed

    def bark(self):
        print("Woof! Woof!")

    def rename(self, newName):
        self.name = newName

    def eat(self, foodWeight):
        self.weight += foodWeight


print("You are about to create a dog.")
age = int(input("How old is the dog: "))
weight = float(input("How much does the dog weigh: "))
name = input("What is the dog's name: ")
color = input("What color is the dog: ")
breed = input("What breed is the dog: ")

d1 = Dog(age, weight, name, color, breed)
print(d1.name + " is a " + str(d1.age) + " year old " + d1.furColor + " " + d1.breed + " that weighs " + str(d1.weight) + " lbs.")
d1.bark()
eat = float(input(d1.name + " is hungry, how much should they eat: "))
d1.eat(eat)
rename = input(d1.name + " isn't a very good name. What should they be renamed to: ")
d1.rename(rename)
print(d1.name + " is a " + str(d1.age) + " year old " + d1.furColor + " " + d1.breed + " that weighs " + str(d1.weight) + " lbs.")
