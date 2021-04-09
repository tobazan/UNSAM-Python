# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 17:59:00 2021

@author: matye
"""

#EJERCICIO 5.8
import matplotlib.pyplot as plt
import numpy as np

temps = np.load('../Data/Temperaturas.npy')

plt.hist(temps,bins=15)