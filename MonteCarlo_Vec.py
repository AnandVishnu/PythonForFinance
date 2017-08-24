# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 14:43:49 2016

@author: anandvishnu
"""

import math
import numpy as np
from time import time

np.random.seed(20000)
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


#simulating I Paths with m time steps
s = np.zeros((M + 1, I))
s[0] = S0
for t in range(1, M + 1):
    z = np.random.standard_normal(I) #random shock
    s[t] = s[t -1] * np.exp((r - 0.5 * sigma ** 2 ) * dt
                            + sigma * math.sqrt(dt) * z)

C0 = math.exp(-r * T) * np.sum(np.maximum(s[-1] - K, 0)) / I

#result output
tnp1 = time() - t0
print(s[-1])
print("European Call option Value", C0)
print("Duration in Seconds", tnp1)