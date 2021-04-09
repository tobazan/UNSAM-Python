# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 16:32:34 2021

@author: matye
"""
import random

def generala_3tiros():
    # PRIMER TIRADA
    tirada = []
    while len(tirada) < 5:
        tirada.append(random.randint(1,6))
    
    numero = tirada[0]
    ocurrencias = 1
    
    for i in tirada.copy():
        if tirada.count(i) > ocurrencias:
            numero = i
            ocurrencias = tirada.count(numero)
    
    if ocurrencias == 5:
        return True
    
    # SEGUNDA TIRADA
    tiro2 = []
    while len(tiro2) < (5-ocurrencias):
        tiro2.append(random.randint(1,6))
        
    for i in tiro2:
        if i != numero:
            #TERCER TIRO
            tiro3 = []
            while len(tiro3) < (5-ocurrencias):
                tiro3.append(random.randint(1,6))
            
            for i in tiro3:
                if i != numero:
                    return False
        
    return True
    

N = 1 * 10**6

G = sum([generala_3tiros() for i in range(N)])
prob = G/N

print(f'Tiré {N} veces, de las cuales {G} saqué generala.')
print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}.')
