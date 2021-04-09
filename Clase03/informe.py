# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 16:18:19 2021

@author: matye

Ejercicio 3.4: Balances

Vamos calcular el balance del negocio: usando 
las funciones leer_camion() y leer_precios()

Pero esta vez con una modificacion en la funcion leer_camion()
de manera que pueda leer el CSV fecha_camion.

¿Hubo ganancia o pérdida? El programa debe imprimir por
pantalla un balance con estos datos.
"""

import csv

def leer_precios(file):
    with open(file, 'rt') as f:
        rows = csv.reader(f)
        precios = {}
        for row in rows:
            try:
                precios[row[0]] = float(row[1])
                
            except: 
                pass
            
    return precios

def leer_camion(file):
    with open(file, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        camion = []
        
        for n_row, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
                camion.append({
                    'nombre': record['nombre'],
                    'cajones': int(record['cajones']),
                    'precio': float(record['precio'])
                    })
            
            except:
                print(f'Fila {n_row}: No pude interpretar: {row}')
            
    return camion

precios = leer_precios('../Data/precios.csv')
camion = leer_camion('../Data/fecha_camion.csv')

balance = 0

for i in camion:
    # parcial -> cajones * (precio de venta - costo)
    # balance -> acummuldo de parciales por cada linea de camion
    parcial = i['cajones'] * (precios[i['nombre']]  - i['precio'])
    balance += parcial

print(f'El balance entre el costo total y la recaudacion fue: ${balance}')
