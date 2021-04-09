# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 15:35:31 2021

@author: matye
"""

def propagar(lista):
    #haciendo uso de la recursividad
    
    for i, v in enumerate(lista):
        if v == 1 and lista[i-1] == 0:
            lista.pop(i-1)
            lista.insert(i-1, 1)
            return propagar(lista)
        
        else:
            try:
                if v == 1 and lista[i+1] == 0:
                    lista.pop(i+1)
                    lista.insert(i+1, 1)
                    return propagar(lista)
            
            except: pass
                
    return lista


print(propagar([ 0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0]))

print(propagar([ 0, 0, 0, 1, 0, 0]))

print(propagar([ -1, 0, 0, 1, 0, -1]))

print(propagar([ 0, -1, 0, 1, 0, 0]))