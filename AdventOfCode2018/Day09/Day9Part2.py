from collections import defaultdict, deque

filename = "Day9Input.txt"
textfile = open(filename, "r")
puzzle_input = textfile.read().strip().split()
numberOfPlayers = int(puzzle_input[0])
lastMarble = int(puzzle_input[6]) * 100  # Part 2 only needed a minor modification here

elvesScores = defaultdict(int)
# Define a blank 'deque' (double-ended queue) to store marbles
# This allows the entire queue (list) to be 'rotated' which makes it perfect for this problem
circle = deque([0])  # Starts at 0 (before any player's turn)

for marble in range(1, lastMarble + 1):
    if marble % 23 == 0:  # If the marble is a multiple of 23
        circle.rotate(7)
        # The marble the player would've placed is added to their score
        # Along with the marble 7 marbles counter-clockwise to it
        # Which is then deleted (circle.pop) afterwards
        elvesScores[marble % numberOfPlayers] += marble + circle.pop()
        # The marble immediately clockwise becomes the current marble
        circle.rotate(-1)
    else:  # If the marble isn't a multiple of 23
        # The marble immediately clockwise becomes the new, current marble
        circle.rotate(-1)
        # The new, current marble is added to the end of the 'circle'
        circle.append(marble)

# Print the best elf's score
print(max(elvesScores.values()))
