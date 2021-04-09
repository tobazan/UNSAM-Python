# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 16:23:49 2021

@author: matye
"""

# pre EJ 3.4
#--------------------------------------------------------
import csv

def costo_camion(filename):
    '''
    dado un archivo csv devolvera el precio total
    multiplicando los campos 'cajones' y 'precio'
    '''
    with open(filename, 'rt') as f:
        filas = csv.reader(f)
        encabezados = next(filas)
        
        costo_total = 0
                   
        for n_fila, fila in enumerate(filas, start=1):
            record = dict(zip(encabezados, fila))
            try:
                ncajones = int(record['cajones'])
                precio = float(record['precio'])
                costo_total += ncajones * precio
            
            except ValueError:
                print(f'Fila {n_fila}: No pude interpretar: {fila}')
                
    return costo_total 

costo = costo_camion('../Data/fecha_camion.csv')
print('Costo total:', costo)    