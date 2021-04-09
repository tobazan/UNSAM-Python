# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 16:15:03 2021

@author: matye

Ejercicio 2.14: Diccionario geringoso.
Construí una función que, a partir de una lista de palabras,
devuelva un diccionario geringoso. Las claves del diccionario
deben las palabras de la lista y los valores deben ser sus 
traducciones al geringoso (como en el Ejercicio 1.18). Probá 
tu función para la lista ['banana', 'manzana', 'mandarina']. 
Guardá este ejercicio en un archivo diccionario_geringoso.py 
para entregar al final de la clase.
"""
def geringoso(palabra):
	'''
	funcion que toma como input una palabra y devuelve
	la misma en "geringoso", osea, que luego de cada 
	vocal agregara las silabas 'pa', 'pe', 'pi', 'po',
	o 'pu' segun dicha vocal
	'''
	palabra = palabra.lower()
	geringosa = []

	for c in palabra:
		if c not in ['a','e','i','o','u']:
			geringosa.append(str(c))

		else:
			geringosa.append(str(c) +'p' + str(c))

	sep = ''

	return sep.join(geringosa)

lista = ['banana', 'manzana', 'mandarina']

def dic_geringoso(l):
    '''
    recibe una lista de palabras
    devuelve un diccionario donde 
        llave = palabra original
        valor = palabra traducida al geringoso
    '''
    g_dic = {}
    
    for palabra in l:
        g_dic[palabra] = geringoso(palabra)
    
    return g_dic

dic_geringoso(lista)