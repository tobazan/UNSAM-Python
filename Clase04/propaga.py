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


#
lista_1 = [ 0, 0, 0, 1, 0, 0]
lista_2 = [ 0, 0, 0, 0, 0, -1]
lista_3 = [ 0, 0, 0, 0, 0, 1]
lista_4 = []
lista_5 = [ 0 for _ in range(1000) ] + [1]
lista_6 = [1] + [ 0 for _ in range(1000) ]
lista_7 = [ (i% 6)//2-1 for i in range(200) ]
lista_8 = [ -1*((i% 6)//2-1) for i in range(60) ]
#

propagar(lista_8)