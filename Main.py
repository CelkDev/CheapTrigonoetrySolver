#!usr/bin/python3

import re
import numpy as np


def reverseCosCalc(a, b, c):
    Angle = np.arccos((a**2-b**2-c**2)/(0-(2*b*c)))
    return Angle


def reverseCos(a, b, c):
    angles = []
    angles.insert(0, (reverseCosCalc(a, b, c)))
    angles.insert(1, (reverseCosCalc(b, c, a)))
    angles.insert(2, (reverseCosCalc(c, a, b)))
    return angles


def pythagCalc(a, b,):
    return np.sqrt(a**2+b**2)


def pythagManager(a, b, c):
    side1 = pythagCalc(abs(a[0]-b[0]), abs(a[1]-b[1]))
    side2 = pythagCalc(abs(b[0]-c[0]), abs(b[1]-c[1]))
    side3 = pythagCalc(abs(c[0]-a[0]), abs(c[1]-a[1]))
    return [side1, side2, side3]


# -----------------------------------------------------------------------------------------------------------------------------------------------------#
# Have fun figuring this shit out later mate.
# No comments for you you fuckin idiot.
# -----------------------------------------------------------------------------------------------------------------------------------------------------#


if (__name__ == "__main__"):
    objPoints = "(23.7, 2)-(19.17, 7)-(11.11, 13)"
    objPoints = objPoints.split("-")
    dataVars = [list(map(float, (re.sub("\(|\)|\ ", "", objPoints[x]).split(",")))) for x in range(len(objPoints))]  # Jesus fucking christ what the fuck did i just make? # noqa
    locationData = dataVars
    dataVars = pythagManager(dataVars[0], dataVars[1], dataVars[2])
    dataVars = [locationData, dataVars, (reverseCos(dataVars[0], dataVars[1], dataVars[2]))] # noqa
    print(dataVars)
