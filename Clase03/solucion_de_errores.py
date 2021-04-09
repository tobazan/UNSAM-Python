# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 11:10:22 2021
@author: matye

SOLUCION DE ERRORES -DEBUGGING
"""
#%%
#EJERCICIO 3.1
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        else:
            return False
        i += 1

#%%
#el problema esta en el uso del return, solo vamos a chequear
#la primera letra del string de esta manera
#y ademas, solo encontraria a minuscula
#asi corregiria la funcion

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    tiene = False
    while i<n:
        if expresion[i] == 'a':
            tiene = True
        elif expresion[i] == 'A':
            tiene = True
        else:
            pass
        i += 1
    return tiene

#%%
#EJERCICIO 3.2
def tiene_a(expresion)
    n = len(expresion)
    i = 0
    while i<n
        if expresion[i] = 'a'
            return True
        i += 1
    return Falso

#en este caso 1ro que faltan los : al condicional, a la def y al while
#2do que la comparacion es con 2 signos =
#3ro puso falso en espanol cuando el ope es False
#4to que tampoco encontraria la A mayuscula

#%%lo corregiria asi

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a' or expresion[i] == 'A' :
            return True
        i += 1
    return False

#%%
#EJERCICIO 3.3
def tiene_uno(expresion):
    n = len(expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene

#en este caso el problema es que va a encontrar los 1 tipo string
#pero cuando la expresion es integer o float salta TypeError

#%%lo arreglaria asi
def tiene_uno(expresion):
    
    expresion = str(expresion)
    
    n = len(expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene

#la solucion facil seria pasar toda expresion con el metodo str()

#%%
#EJERCICIO 3.4
def suma(a,b):
    c = a + b

a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")

#el problema es que esta mal definida la funcion suma
#le falta retornar algo, por eso c es None

#%%
#lo arreglaria asi

def suma(a,b):
    c = a + b
    return c

a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")

#%%
#EJERCICIO 3.5
import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    registro={}
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion

camion = leer_camion('../Data/camion.csv')
pprint(camion)

#El problema es que agrega el primer regitro de naranjas
#a la lista camion. Nunca reasigna/sobreescribe si bien itera
