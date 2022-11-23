#!usr/bin/env python3
# switch
def switch(argument):
    switcher = {"a": lambda: 1, "b": lambda: 2, "c": lambda: 3, "d": lambda: 4}
    func = switcher.get(argument, "Invalid value")
    return func()


# calculate pythagoras numbers
from math import sqrt

n = input("Max number?")
n = int(n) + 1
for a in range(1, n):
    for b in range(a, n):
        c_square = a**2 + b**2
        c = int(sqrt(c_square))
        if (c_square - c**2) == 0:
            print(a, b, c)

# level function
XPPoints = 100000
XPLevel = 0
neededPoints = 1000;
while XPPoints > neededPoints:
    XPLevel += 1
    neededPoints = 1.1 * neededPoints
    print(XPLevel, neededPoints)

