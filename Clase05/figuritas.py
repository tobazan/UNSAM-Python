# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 18:02:39 2021

@author: matye
"""
import random
import numpy as np

def crear_album(figus_total):
    album = [0 for i in range(figus_total)]
    return album

def album_incompleto(lista):
    if 0 in lista:
        return True
    return False

def comprar_figu(figus_total):
    return random.randint(0, figus_total-1)

def cuantas_figus(figus_total):
    album = crear_album(figus_total)
    total = 0
    
    while album_incompleto(album):
        
        figu = comprar_figu(figus_total)
        total += 1
        
        if album[figu] == 0:
            album[figu] = 1
        
        else: album[figu] += 1
    
    return total
        
#TEST
figus_total = 670
n_reps = 100

R = np.array([cuantas_figus(figus_total) for i in range(n_reps)])
avg = np.average(R)

print(avg)
