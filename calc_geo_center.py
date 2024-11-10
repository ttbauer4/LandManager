"""
calculates the geographical center of the convex hull of coordinates
"""

import numpy as np
from scipy.spatial import ConvexHull
from matplotlib.path import Path

exit = False
coords = np.empty((0, 2))

# retrieve coordinates from user
print('\nInput coordinates as prompted below. Type \"exit\" when complete.\n')
while(not exit):
    latitude = input('Latitude (or exit): ')
    if latitude == "exit":
        break
    try: float(latitude)
    except ValueError:
        print("Invalid latitude.\n")
        continue

    longitude = input('Longitude: ')
    if longitude == "exit":
        break
    try: float(longitude)
    except ValueError:
        print("Invalid longitude. Re-enter coordinate pair.\n")
        continue
    coords = np.append(coords, np.array([[float(latitude), float(longitude)]]), axis=0)

# calculate the convex hull of points
hull = ConvexHull(coords)

# create a path object from the hull vertices
hull_path = Path(coords[hull.vertices])

print("\nGeographical Center of \"Convex Hull\": " + str(np.mean(hull_path.vertices[:,0])) + ", " + str(np.mean(hull_path.vertices[:,1])) + "\n")