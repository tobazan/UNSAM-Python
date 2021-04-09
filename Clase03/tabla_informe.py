# -*- coding: utf-8 -*-
"""
EJERCICIO 3.19

Generar informe en formato de tabla
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
        dic = {}
        
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

def hacer_informe(camion, precios):
    balance = 0
    
    h = ['Nombre', 'Cajones', 'Precio', 'Cambio']
    print(f'{h[0]:^10s} {h[1]:^10s} {h[2]:^10s} {h[3]:^10s}')
    print('---------- ---------- ---------- ----------')

    for i in camion:
        # parcial -> cajones * (precio de venta - costo)
        # balance -> acummuldo de parciales por cada linea de camion
        parcial = i['cajones'] * (precios[i['nombre']]  - i['precio'])
        balance += parcial
        
        r = [i['nombre'],i['cajones'],i['precio'],(precios[i['nombre']]  - i['precio'])]
        print(f'{r[0]:<10s} {r[1]:^10d} ${r[2]:>9.2f} {r[3]:>9.2f}')
        
    print('---------- ---------- ---------- ----------')
    print(f'\nEl balance fue: ${balance}')

hacer_informe(camion,precios)