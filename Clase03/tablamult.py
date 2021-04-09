# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 10:46:52 2021

@author: matye
"""

uno = list(range(0,10,1))
cero = list('0' * 10)


print(f'{" ":1s} {uno[0]:2d} {uno[1]:2d} {uno[2]:2d} {uno[3]:2d} {uno[4]:2d} {uno[5]:2d} {uno[6]:2d} {uno[7]:2d} {uno[8]:2d} {uno[9]:2d}')
print('-' * 32)
for i in uno: 
    print(f'{i}: {cero[i]} {i:2d} {i*2:2d} {i*3:2d} {i*4:2d} {i*5:2d} {i*6:2d} {i*7:2d} {i*8:2d} {i*9:2d}')
