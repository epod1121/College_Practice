#Assignment2B

mammals = ["dog", "cat", "human", "elephant", "whale"]
birds = ["eagle", "parrot", "penguin", "sparrow"]
reptiles = ["snake", "lizard", "crocodile", "turtle"]
fish = ["salmon", "goldfish", "shark", "tuna"]
amphibians = ["frog", "toad", "salamander", "newt"]

animal = input("Enter the name of an animal: ").lower()

if animal in mammals:
    print("The animal is a Mammal.")
elif animal in birds:
    print("The animal is a Bird.")
elif animal in reptiles:
    print("The animal is a Reptile.")
elif animal in fish:
    print("The animal is a Fish.")
elif animal in amphibians:
    print("The animal is an Amphibian.")
else:
    print("Unknown category.")