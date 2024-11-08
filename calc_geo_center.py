"""
calculates the geographical center of coordinates
"""

import statistics

exit = False
latcoords = []
loncoords = []

print('\nInput coordinates as prompted below. Type \"exit\" when complete.\n')
while(not exit):
    latitude = input('Latitude (or exit): ')
    if latitude == "exit":
        break
    try: latcoords.append(float(latitude))
    except ValueError:
        print("Invalid latitude.\n")
        continue

    longitude = input('Longitude: ')
    if longitude == "exit":
        break
    try: loncoords.append(float(longitude))
    except ValueError:
        print("Invalid longitude. Re-enter coordinate pair.\n")
        continue

print("\nGeographical Center: " + str(statistics.mean(latcoords)) + ", " + str(statistics.mean(loncoords)) + "\n")