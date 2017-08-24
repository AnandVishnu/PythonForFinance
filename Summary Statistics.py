# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 19:10:19 2016

@author: anandvishnu
"""

import numpy as np
from pandas import Series, DataFrame
import pandas as pd

import pandas.io.data as pdweb
import datetime 
import seaborn as sns
import matplotlib.pyplot as plt
#create data frame
#arr = np.array([[1,2,np.nan], [np.nan,3,4]])

#dframe1 = DataFrame(arr, index=['A', 'B'], columns=['One', 'Two','Three'])
#print(dframe1)
"""
print(dframe1.sum())
print(dframe1.sum(1))
print(dframe1.min())
print(dframe1.min(1))
print(dframe1.idxmin())
"""

#print(dframe1.cumsum())

#describe method summary stat

#print(dframe1.describe())

#correlation and covariance

prices = pdweb.get_data_yahoo(['CVX', 'XOM', 'BP'], start=datetime.datetime(2010,1,1),
                              end=datetime.datetime(2013,1,1))['Adj Close']

volume = pdweb.get_data_yahoo(['CVX', 'XOM', 'BP'], start=datetime.datetime(2010,1,1),
                              end=datetime.datetime(2013,1,1))['Volume']                           
                              
rets = prices.pct_change()

#correlation

corr = rets.corr()

#prices.plot()

sns.heatmap(rets)

