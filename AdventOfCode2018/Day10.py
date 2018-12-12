# This problem requires human validation (or computer vision)
# to decide which one of the possible solutions contains letters
# My solution contains code for Part 1 and Part 2 as Part 2 only requires the time printing
# (something I had done out of curiosity during Part 1)
import re  # Import regular expressions (regex)

filename = "Day10Input.txt"
textfile = open(filename, "r")
puzzle_input = textfile.readlines()
coords = []
boxWidth = 100  # Arbitrary binding box width


for line in puzzle_input:
    # \-?\d+ is the regex pattern for any integer, positive or negative integer
    # https://stackoverflow.com/questions/6508043/regular-expression-to-find-any-number-in-a-string
    x, y, velocityX, velocityY = map(int, re.findall('\-?\d+', line))  # Split x, y and velocity values from each line
    coords.append([x, y, velocityX, velocityY])  # Append them to a list

for time in range(200000):  # Loop over 200,000 times (any large, arbitrary value will be fine)
    # Find the min and max x and y values to determine if any values lie on the edge of a 'binding box'
    # If any points are on the edge of a binding box, it is possible that a word is being displayed...
    # This is an assumption that has to be made to solve this problem without the use of AI

    minimumX = min([x for x, y, _, _ in coords])  # '_' is used to ignore the velocity values
    minimumY = min([y for x, y, _, _ in coords])
    maximumX = max([x for x, y, _, _ in coords])
    maximumY = max([y for x, y, _, _ in coords])

    # If there are points on the edge of the binding box
    if (minimumX + boxWidth) >= maximumX and (minimumY + boxWidth) >= maximumY:
        print(str(time) + " seconds")  # Output the time

        # Loop through the smallest possible binding box for these values
        # and plot them with '#' characters
        for y in range(minimumY, maximumY+1):
            for x in range(minimumX, maximumX+1):
                if (x, y) in [(xCoord, yCoord) for xCoord, yCoord, _, _ in coords]:  # If a coordinate has been reached
                    print('#', end='')  # Print a '#'
                else:
                    print('.', end='')  # Print a placeholder '.'
            print()  # Print a new line

    for item in coords:  # Loop through every coordinate (advance the coordinates by a second)
        item[0] += item[2]  # Apply velocity to the X value
        item[1] += item[3]  # Apply velocity to the Y value
