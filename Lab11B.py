# Lab11B

def letterPosition(string, character):
    string = string.lower()
    character = character.lower()
    positions = []

    index = 0

    for letter in string:
        if letter == character:
            positions.append(index)
        index += 1


    return tuple(positions)


phrase = input("Enter your phrase: ")
letter = input("Enter a letter: ")

print(letterPosition(phrase, letter))
