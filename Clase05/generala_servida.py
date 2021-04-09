# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 16:32:34 2021

@author: matye
"""
import random

def tirar():
    tirada = []
    while len(tirada) < 5:
        tirada.append(random.randint(1,6))
        
    return tirada

def es_generala(tirada):
    numero = tirada[0]
    
    for i in tirada:
        
        if i != numero:
            return False
        
        else: pass
    
    return True

N = 1 * 10**6

G = sum([es_generala(tirar()) for i in range(N)])
prob = G/N

print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}.')
