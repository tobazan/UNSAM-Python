# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 16:20:20 2021

@author: matye
"""

def buscar_precio(fruta):
    '''
    dada una fruta buscara en el archivo su precio
    si la encuentra lo retorna, sino devuelve un mensaje
    diciendo que dicha fruta no esta en la lista de precios
    '''
    with open('../Data/precios.csv', 'rt') as f:
        headers = next(f)
        
        try:
            for line in f:
                row = line.split(',')
                
                if row[0].upper() == fruta.upper():
                    precio = float(row[1])
                elif row[0].lower() == fruta.lower():
                    precio = float(row[1])
                else: pass
            
            print(f'El precio de un cajon de {fruta} vale {precio}')
        
        except: print(f'{fruta} no aparece en el listado de precios')
        
    return

buscar_precio('frambuesa')
buscar_precio('kale')