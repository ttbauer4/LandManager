"""
calculates the geographical center of the convex hull of coordinates
"""

import statistics
import numpy as np
from scipy.spatial import ConvexHull
from matplotlib.path import Path

exit = False
coords = np.empty((0, 2))
convex_hull = False

# retrieve user algorithm selection
algo = input('\nPlease indicate your desired algorithm. Type\n(1) for Center of Convex Hull\n(2) for Center of Extrema\n')
while(algo != '1' and algo != '2'):
    print(algo)
    algo = input('Improper selection. Try again: ')

if (algo == '1'): convex_hull = True

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

if convex_hull:
    # calculate the convex hull of points
    hull = ConvexHull(coords)
    # create a path object from the hull vertices
    hull_path = Path(coords[hull.vertices])
    print("\nGeographical Center of \"Convex Hull\": " + str(np.mean(hull_path.vertices[:,0])) + ", " + str(np.mean(hull_path.vertices[:,1])) + "\n")
else:
    # calculate means of maximum/minimum latitude/longitude
    maxima = np.max(coords, axis=0)
    minima = np.min(coords, axis=0)
    print("\nGeographical Center of \"Extrema\": " + str(statistics.mean([maxima[0], minima[0]])) + ", " + str(statistics.mean([maxima[1], minima[1]])) + "\n")
