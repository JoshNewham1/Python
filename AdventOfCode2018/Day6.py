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
# Creates an array with the 'Manhattan Distance' between each point
closest_origin = np.argmin(cityblock, axis=0)
# Filter out points with competing closest IDs though
min_distances = np.min(cityblock, axis=0)
competing_locations_filter = (cityblock == min_distances).sum(axis=0) > 1
# Note, integers in numpy don't support NaN (Not a Number), so make the ID higher than
# the possible point ID
closest_origin[competing_locations_filter] = len(points) + 1

closest_origin = closest_origin.reshape(xgrid.shape)
infinite_ids = np.unique(np.vstack([  # Infinite items are on the edge of the grid
    closest_origin[0],
    closest_origin[-1],
    closest_origin[:, 0],
    closest_origin[:, -1]
]))
closest_origin[np.isin(closest_origin, infinite_ids)] = len(points) + 1

# and because we know the id of the "null" data is guaranteed to be last
# in the array (it's highest) we can index it out before getting the max
# region size
print(np.max(np.bincount(closest_origin.ravel())[:-1]))