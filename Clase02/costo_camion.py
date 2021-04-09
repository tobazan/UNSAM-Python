# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 14:47:31 2021

@author: matye
"""

# EJERCICIO 2.9
#--------------------------------------------------------
import csv

def costo_camion(filename):
    '''
    dado un archivo csv devolvera el precio total
    multiplicando los campos 'cajones' y 'precio'
    '''
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        
        costo = 0
        
        for row in rows:
            cajones = int(row[1])
            precio = float(row[2])     
            costo +=  cajones * precio
    
    return costo    

costo = costo_camion('../Data/camion.csv')
print('Costo total:', costo)        