import numpy as np
from scipy.spatial import distance  # Supports manhattan distance (don't have to write a method)

# read the data using scipy
points = np.loadtxt('Day6Input.txt', delimiter=', ')

# build a grid of the appropriate size - note the -1 and +2 to ensure all points
# are within the grid
xmin, ymin = points.min(axis=0) - 1
xmax, ymax = points.max(axis=0) + 2

# and use meshgrid to build the target coordinates
xgrid, ygrid = np.meshgrid(np.arange(xmin, xmax), np.arange(xmin, xmax))
targets = np.dstack([xgrid, ygrid]).reshape(-1, 2)

# Manhattan distance = cityblock in scipy
cityblock = distance.cdist(points, targets, metric='cityblock')
# Turns out Part 2 is much easier than Part 1
# Add (sum) the distances of each possible grid location
distances = cityblock.sum(axis=0)
# Assign the value of 1 to appropriate distances, with the rest as 0
acceptedRegion = np.where(distances < 10000, 1, 0)
# The sum is the result
print(acceptedRegion.sum())
