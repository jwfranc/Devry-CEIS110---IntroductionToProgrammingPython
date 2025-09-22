# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Purpose: Create box plot for period 2 data
#Name: John Francis
#Date: 4/8/2021
import pandas as pd
import matplotlib.pyplot as plt
df2 = pd.read_csv("formatdata2.csv")
df2.boxplot(); plt.suptitle('Period 2 box plot')
plt.show()





