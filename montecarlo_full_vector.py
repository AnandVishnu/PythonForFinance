# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 15:53:10 2016

@author: anandvishnu
"""

import math
from numpy import *
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
s = S0 * exp(cumsum((r - 0.5 * sigma ** 2) * dt 
             + sigma * math.sqrt(dt)
                     * random.standard_normal((M + 1, I)), axis=0))
s[0] = S0

C0 = math.exp(-r * T) * sum(maximum(s[-1] - K, 0)) / I

#result output
tnp1 = time() - t0
print("European Call option Value", C0)
print("Duration in Seconds", tnp1)  

import matplotlib.pyplot as plt
plt.plot(s[:, :10])
plt.grid(True)
plt.xlabel('time step')
plt.ylabel('index label')        

plt.hist(s[-1], bins=50)  
plt.grid(True)  
plt.xlabel('index label')
plt.ylabel('frequency')    

plt.hist(np.maximum(s[-1] - K, 0), bins=50)  
plt.grid(True)  
plt.xlabel('Option Value')
plt.ylabel('frequency') 
plt.ylim(0, 50000) 
    