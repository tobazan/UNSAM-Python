# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 16:45:31 2021

@author: matye

EJERCICIO 3.7

Definí una función leer_parque(nombre_archivo, parque) 
que abra el archivo indicado y devuelva una lista de 
diccionarios con la información del parque especificado.

La función debe devolver, en una lista un diccionario con
todos los datos por cada árbol del parque elegido.
"""

import csv

def leer_parque(file,parque):
    '''
    dado un archivo y el nombre de un parque
    si el parque existe, devuelve una lista
    en la que cada arbol es undiccionario
    con todos sus datos
    '''
    def parque_esta(parque):
        with open(file, 'rt', encoding='utf-8') as f:
            rows = csv.reader(f)
            headers = next(rows)
            parques = set()
            
            for n_row, row in enumerate(rows,start=1):
                record = dict(zip(headers, row))
                parques.add(record['espacio_ve'])
    
            esta =  parque in parques
            
        return esta
    
    if parque_esta(parque):
        arboles = []
        
        with open(file, 'rt', encoding='utf-8') as f:
            rows = csv.reader(f)
            headers = next(rows)
                   
            for n_row, row in enumerate(rows, start=1):
                record = dict(zip(headers, row))
                
                try:
                    if record['espacio_ve'] == parque:
                        arboles.append({
                            'Id':record['id_arbol'],
                            'Altura':record['altura_tot'],
                            'Diametro':record['diametro'],
                            'Inclinacion':record['inclinacio'],
                            'Especie': record['id_especie'],
                            'Nombre':record['nombre_com'],
                            'Nombre_cs':record['nombre_cie'],
                            'Follaje':record['tipo_folla'],
                            'Familia':record['nombre_fam'],
                            'Genero':record['nombre_gen'],
                            'Origen':record['origen']
                        })
                
                except ValueError:
                    print(f'Fila {n_row}: No pude interpretar: {row}')
        
        return arboles
    
    else: print('Ese parque no existe')

print(len
      (leer_parque('../Data/arbolado-en-espacios-verdes.csv',
                   'GENERAL PAZ'))
      )