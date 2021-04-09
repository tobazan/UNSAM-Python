# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 17:40:37 2021

@author: matye

EJERCICIO 5.25

Usando comprensión de listas y la variable arboleda podés
por ejemplo armar la lista de la altura de los árboles.
"""
import csv
import matplotlib.pyplot as plt

def leer_parque(file):

    arboleda = []
        
    with open(file, 'rt', encoding='utf-8') as f:
        rows = csv.reader(f)
        headers = next(rows)
               
        for n_row, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            
            try:
                arboleda.append({
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
    
    return arboleda

        
arboleda = leer_parque('../Data/arbolado-en-espacios-verdes.csv')

diametros = [arbol['Diametro'] for arbol in arboleda 
              if arbol['Nombre']=='Jacarandá']

alturas = [arbol['Altura'] for arbol in arboleda 
              if arbol['Nombre']=='Jacarandá']

     
plt.scatter(diametros, alturas)
plt.xlabel("diametro (cm)")
plt.ylabel("alto (m)")
plt.title("Relación diámetro-alto para Jacarandás")

