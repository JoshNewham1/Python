import numpy as np

filename = "Day3Input.txt"
textfile = open(filename, "r")
puzzle_input = textfile.readlines()
claims = []


# Typical entry: #1 @ 126,902: 29x28
def splitinput(line):  # Splits the input into separate variables
    words = line.split(' ')
    id = int(words[0].replace('#', ''))
    coordinates = words[2].split(',')
    xcoord = int(coordinates[0])
    ycoord = int(coordinates[1].replace(':', ''))
    sizes = words[3].split('x')
    width = int(sizes[0])
    height = int(sizes[1])

    return id, xcoord, ycoord, width, height


def overlapping(claims):
    grid = np.zeros((1000, 1000))  # Creates a 1000x1000 'grid' of 0s
    for claim in claims:  # Loops through all of the claims from elves
        id = claim[0]  # Extracts the id
        xcoord = claim[1]  # Extracts the x coordinate of the rectangle
        ycoord = claim[2]  # Extracts the y coordinate of the rectangle
        width = claim[3]  # Extracts the width of the rectangle
        height = claim[4]  # Extracts the height of the rectangle

        grid[xcoord:xcoord + width, ycoord:ycoord + height] += 1
    return np.size(np.where(grid >= 2)[0])


for entry in puzzle_input:
    rect_data = splitinput(entry)
    claims.append(rect_data)

print(overlapping(claims))
