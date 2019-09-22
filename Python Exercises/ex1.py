import numpy as np


def printWithoutPoint(num):
    s = str(num)
    print((s.replace('.', '')))


for i in np.arange(0, 5, 0.1):
    printWithoutPoint(round(i, 2))
