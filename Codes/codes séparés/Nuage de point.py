
import os
#import numpy as np
#import pyvista as pv
#from pyvista import examples
import array
from math import *
from matplotlib import pyplot
results = [2550, 2700, 2000, 2500, 3000, 3100, 2400, 2950]
vectorx = []
vectory = []

for i in range(0,8):
    a = results[i]*cos((pi*i)/4)
    b = results[i]*sin((pi*i)/4)
    vectorx.append(int(a))
    vectory.append(int(b))

#print(vector)
print(vectorx)
print(vectory)
pyplot.scatter(vectorx, vectory)
pyplot.show()
pyplot.savefig('mapping.png')