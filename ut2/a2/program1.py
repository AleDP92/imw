from math import sqrt

import sys


a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

if a == 0:
    print("x =", -c / b)

if b**2 - 4 * a * c < 0:
    print("no hay solución real")

else:
    print("x =", (-b + sqrt(b**2 - 4 * a * c) / 2 * a))
    print("x =", (-b - sqrt(b**2 - 4 * a * c) / 2 * a))
