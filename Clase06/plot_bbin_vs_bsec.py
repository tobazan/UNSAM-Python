# plot_bbin_vs_bsec.py
import random
import matplotlib.pyplot as plt
import numpy as np
from bbin import busqueda_binaria

def busqueda_secuencial_(lista, x):
    '''Si x está en la lista devuelve el índice de su 
    primer aparición, de lo contrario devuelve -1.
    '''
    comps = 0 # inicializo en cero la cantidad de comparaciones
    pos = -1
    for i,z in enumerate(lista):
        comps += 1 # sumo la comparación que estoy por hacer
        if z == x:
            pos = i
            break
    return pos, comps

def generar_lista(n, m):
    l = random.sample(range(m), k = n)
    l.sort()
    return l

def generar_elemento(m):
    return random.randint(0, m-1)

def experimento_secuencial_promedio(lista, m, k):
    comps_tot = 0
    for i in range(k):
        x = generar_elemento(m)
        comps_tot += busqueda_secuencial_(lista,x)[1]

    comps_prom = comps_tot / k
    return comps_prom

def experimento_binario_promedio(lista, m, k):
    comps_tot = 0
    for i in range(k):
        x = generar_elemento(m)
        comps_tot += busqueda_binaria(lista,x)[2]

    comps_prom = comps_tot / k
    return comps_prom
    
m = 10000
n = 100
k = 1000
lista = generar_lista(n, m)

largos = np.arange(256) + 1 # estos son los largos de listas que voy a usar
prom_comps_sec = np.zeros(256) # aca guardo el promedio de comparaciones sobre una lista de largo i, para i entre 1 y 256.
prom_comps_bin = np.zeros(256) # aca guardo el promedio de comparaciones sobre una lista de largo i, para i entre 1 y 256.

for i, n in enumerate(largos):
    lista = generar_lista(n, m) # genero lista de largo n
    prom_comps_sec[i] = experimento_secuencial_promedio(lista, m, k)
    prom_comps_bin[i] = experimento_binario_promedio(lista, m, k)

# ahora grafico largos de listas contra operaciones promedio de búsqueda.
fig = plt.figure()
ax = fig.add_subplot(111)
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

ax.set_title('Complejidad de la Búsqueda')
ax.axis('off')

ax1.plot(largos,prom_comps_bin,color='seagreen',label='B Binaria')
ax1.set_xlabel("Largo de la lista")
ax1.set_ylabel("Cantidad de comparaiciones")
ax1.legend()

ax2.plot(largos,prom_comps_sec,color='blue',label='B Secuencial')
ax2.set_xlabel("Largo de la lista")
ax2.legend()