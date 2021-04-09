# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 10:33:41 2021

@author: matye
"""

def invertir_lista(lista):
    invertida = []
    
    for e in lista: # Recorro la lista
        invertida.insert(0, e)
        
    return invertida


#TEST
lista1 = [1, 2, 3, 4, 5]
lista2 =['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel']

print(invertir_lista(lista1))
print(invertir_lista(lista2))

