import numpy as np

serial = 5093  # Serial number given by challenge


def powerlevel(xCoord, yCoord):
    rackID = (xCoord + 1) + 10  # Need to add one as coordinates START at 1
    powerLevel = rackID * (yCoord + 1) # Need to add one as coordinates START at 1
    powerLevel += serial
    powerLevel = powerLevel * rackID
    hundredths = (powerLevel // 100) % 10  # '//' does a floor division
    powerLevel = hundredths
    powerLevel -= 5

    return powerLevel


grid = np.fromfunction(powerlevel, (300, 300))

width = 3  # Looking for a 3x3 box
# Add up all of the power levels in 3x3 grid and store it in a numpy array
powerInGrid = sum(grid[x:x - width + 1 or None, y:y - width + 1 or None] for x in range(width) for y in range(width))
maximum = int(powerInGrid.max())  # Get the maximum power level
location = np.where(powerInGrid == maximum)  # Find the coordinates of the maximum power level
print(width, maximum, location[0][0] + 1, location[1][0] + 1)  # Print width, max power and coords
