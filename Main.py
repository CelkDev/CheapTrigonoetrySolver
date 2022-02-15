#!usr/bin/python3
from uniplot import plot as plot
import re
import numpy as np
import os


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

os.system("clear")
objPoints = input(
    "The points on your triangle please(format as \"(x1,y1)-(x2,y2)-(x3,y3)\"): ")  # noqa
objPoints = objPoints.split("-")
dataVars = [list(map(float, (re.sub("\(|\)|\ ", "", objPoints[x]).split(",")))) for x in range(len(objPoints))]  # noqa Jesus fucking christ what the fuck did i just make?
locationData = dataVars
dataVars = pythagManager(dataVars[0], dataVars[1], dataVars[2])
dataVars = [locationData, dataVars, (reverseCos(dataVars[0], dataVars[1], dataVars[2]))]  # noqa

line1y = [dataVars[0][1], dataVars[1][1]]
line1x = [dataVars[0][0], dataVars[1][0]]
line2y = [dataVars[1][1], dataVars[2][1]]
line2x = [dataVars[1][0], dataVars[2][0]]

plot([line1y,line2y], [line1x,line2x], lines=True)

print(dataVars)
