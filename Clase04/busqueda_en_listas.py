# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 10:20:35 2021

@author: matye
"""

def buscar_u_elemento(lista, elemento):
    '''
    Recibe una lista y un elemento, el cual sera
    buscado dentro de esa lista.
    
    Si el elemento se encuentra, la funcion retorna
    la posicion.
    
    Sino, retorna "-1"
    '''
    
    posicion = -1
    for i, val in enumerate(lista):
        if val == elemento:
            posicion = i
            break
        
    return posicion

#TEST
print(buscar_u_elemento([1, 4, 54, 3, 0, -1], 44))

print(buscar_u_elemento([1, 4, 54, 3, 0, -1], 3))

def maximo(lista):
    '''
    Devuelve el máximo de una lista, 
    la lista debe ser no vacía y de números positivos.
    '''
    
    maximo = 0
    
    for numero in lista:
        if numero > maximo:
            maximo = numero
        
    return maximo

#TEST
print(maximo([1,2,7,2,3,4]))

print(maximo([1,2,3,4]))

print(maximo([-5,-4]))