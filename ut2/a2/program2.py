from math import sqrt
import sys

x1 = int(sys.argv[1])
y1 = int(sys.argv[2])
x2 = int(sys.argv[3])
y2 = int(sys.argv[1])
x3 = int(sys.argv[2])
y3 = int(sys.argv[3])

d1 = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
d2 = sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)

if d1 > d2:
	print("El punto más cercano a(", x1, ",", y1, ") es (", x3, ",", y3, ") y está a una distancia de:", d2)
if d1 < d2:
	print("El punto más cercano a(", x1, ",", y1, ") es (", x2, ",", y2, ") y está a una distancia de:", d1)
