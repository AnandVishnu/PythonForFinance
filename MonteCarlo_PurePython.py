# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 09:37:02 2016

@author: anandvishnu
"""

from time import time
from math import exp, sqrt, log
from random import gauss, seed

seed(20000)
t0 = time()

#parameters
S0    = 100
K     = 105
T     = 1    # maturity
r     = 0.05 # risk less interest rate 
sigma = 0.2  # vol
M = 50       # number of time steps
dt = T/M     # length of time interval
I = 250000   # number of paths


#simulating I paths with M time step

S = []
for i in range(I):
    path = []
    for t in range(M + 1):
        if t == 0:
            path.append(S0)
        else:
            z = gauss(0.0, 1.0)
            St = path[t-1] * exp((r - 0.5 * sigma ** 2) * dt 
                + sigma * sqrt(dt) * z) 
            
            path.append(St)
    S.append(path)
    
C0 = exp( - r * T) * sum ([max(path[-1] - K, 0) for path in S]) / I

tpy = time() - t0
print("European Call option Value", C0)
print("Duration in Seconds", tpy)
