import random
import math

points = int(input("Anna arvottavien pisteiden lukumäärä: "))
points2 = points

isInside = float(0)

while points2 > 0:

    x = random.random()
    y = random.random()

    if x**2+y**2<1:
        isInside += 1

    points2 -= 1

print("Pii:n likiarvo on: " + str(4 * isInside / points))
