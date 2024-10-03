# Write a function that takes two tuples representing coordinates (x1, y1) and (x2, y2) 
# and returns the distance between them using the distance formula.

######### SOLUTION #########

import math

def points_distance(point1, point2):
    delta_x = point2[0] - point1[0]
    delta_y = point2[1] - point1[1]

    distance = math.sqrt((delta_x)**2 + (delta_y)**2)

    return round(distance, 2)

test1 = points_distance((3, 3), (5, 5))
print(test1)

test2 = points_distance((10, 1), (7, 8))
print(test2)

test3 = points_distance((0, 3), (4, 4))
print(test3)