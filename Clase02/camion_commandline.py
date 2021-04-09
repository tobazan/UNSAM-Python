# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 15:47:11 2021

@author: matye
"""

import csv
import sys 

def costo_camion(filename):
    '''
    dado un archivo csv devolvera el precio total
    multiplicando los campos 'cajones' y 'precio'
    '''
   
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        costo = 0
        fila = 1
        
        for row in rows:
                        
            try:
                cajones = int(row[1])
                precio = float(row[2])     
                costo +=  cajones * precio
                
            except:
                print(f'Fila {fila}: No pude interpretar: {row}')
            
            fila += 1
            
    return costo

if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = '../Data/camion.csv'

# costo = costo_camion(nombre_archivo)
costo = costo_camion('../Data/missing.csv')
print('Costo total:', costo)