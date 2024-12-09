#Assignment6B
import random

width = int(input("Enter dungeon width: "))
height = int(input("Enter dungeon height: "))

board = []

numTreasures = 0

for _ in range(width):
    row = []
    for _ in range(height):
        if random.random() >= 0.7:
            row.append('T')
            numTreasures += 1
        else:
            row.append('O')
    board.append(row)

print("Treasures are hidden in ", numTreasures, " locations.\n")

while numTreasures > 0:
    rowGuess = int(input("Enter row to check (0-" + str(width-1) + "): "))
    colGuess = int(input(f"Enter column to check (0-" + str(height-1) + "): "))

    if board[rowGuess][colGuess] == 'T':
        print("You found a treasure at (", rowGuess, ", ", colGuess, ")!")
        board[rowGuess][colGuess] = 'X'
        numTreasures -= 1
    else:
        print("No treasure found at (", rowGuess, ", ", colGuess, ")")

print("\nAll treasures found! Final board:")
for row in board:
    print(*row, sep=" ")
