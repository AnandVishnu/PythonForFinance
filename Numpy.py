# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 10:57:26 2016

@author: anandvishnu
"""

import numpy as np
#import matplotlib.pyplot as plt
from numpy.random import randn

# %matplotlib inline
"""
points = np.arange(-5,5,0.01)
dx, dy = np.meshgrid(points, points)
z = (np.sin(dx) + np.sin(dy))
plt.imshow(z)
plt.colorbar()
plt.title("sin<x> + sin<y>")

A = np.array([1,2,3,4])
B = np.array([100, 200, 300, 400])
condition = np.array([True, True, False, False])

result = [(A_Val if Cond else B_Val) for A_Val, B_Val, Cond in zip(A, B, condition)]
result2 = np.where(condition, A, B)

"""

#random 

arr = randn(5, 5)
filteredValue = np.where(arr<0, 0, arr)

print(arr)
print(filteredValue)