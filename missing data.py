# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 19:59:49 2016

@author: anandvishnu
"""

import numpy as np
from pandas import Series, DataFrame
import pandas as pd

import pandas.io.data as pdweb
import datetime 
import seaborn as sns
import matplotlib.pyplot as plt

"""

data = Series(['One', 'Two', np.nan, 'Four'])

print(data.isnull())
print(data.dropna())

"""

dframe = DataFrame([[1,2,3], [np.nan, 5,6], [7,np.nan, 9], [np.nan, np.nan, np.nan]])

clean_frame = dframe.dropna()

#print(dframe)
#print(clean_frame)