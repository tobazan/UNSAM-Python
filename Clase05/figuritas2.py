import random
import numpy as np
import matplotlib.pyplot as plt

def crear_album(figus_total):
    '''Recibe el tamaño del álbum y devuelve un array de 0s que
    representa el album vacio'''
    album = np.zeros(figus_total, dtype='int64')
    return album

def album_incompleto(album):
    '''Si el album esta completo retorna True, de lo contrario False'''
    return album.min() == 0

def comprar_paquete(total_figus, n):
    '''
    Parámetros
    ----------
    total_figus - (int) tamano del álbum
    n - (int) cantidad de figus que trae un paquete
    
    Retorna
    -------
    Un paquete con n figuritas al azar
    '''
    paquete = []
    for f in range(n):
        figu = random.randint(0, total_figus-1)
        paquete.append(figu)
    return paquete

def cuantas_figus(n, cant_figus):
    '''
    Parámetros
    ----------
    cant_figus - (int) cantidad de figus que trae un paquete
    n - (int) tamano del álbum
    
    Retorna
    -------
    Simula la compra de paquete hasta llenar el album y 
    devuelve la cantidad total de figus compradas (incluye repetidas)
    '''
    album = crear_album(n)
    cant_compradas = 0
    while album_incompleto(album):
        paquete = comprar_paquete(n, cant_figus)
        for a in paquete:
            if album[a] == 0:
                album[a] = 1
        cant_compradas += 1
    return cant_compradas

def n_repeticiones(repeticiones, album, cant_figus):
    '''
    Parámetros
    ----------
    repeticiones - (int) cuantos experimentos se corren
    album - (int) tamano del álbum
    cant_figus - (int) cantidad de figus que trae un paquete
    
    Retorna
    -------
    Simula la compra de paquete hasta llenar el album y 
    devuelve la cantidad total de figus compradas (incluye repetidas)
    '''
    resultados = []
    for a in range(repeticiones):
        resultados.append(cuantas_figus(album, cant_figus))
    res = np.array(resultados)
    promedio = np.mean(res)
    return res, promedio


# SIMULACION
# --------------------------------------------------------------------
repeticiones = 100
figus_total = 670
cant_figus = 1

de_a_una = n_repeticiones(repeticiones, figus_total, cant_figus)

'''El análisis realizado para un álbum de 670 figuritas, comprando de 
a 1 y corriendo 100 experimentos arroja que en promedio se compran 4684.44'''

repeticiones = 1000
figus_total = 670
cant_figus = 5

de_a_cinco = n_repeticiones(repeticiones, figus_total, cant_figus)

'''El análisis realizado para un álbum de 670 figuritas, comprando de
a 5 y corriendo 100 experimentos arroja que en promedio se compran 
963.42 paquetes = 4817.1 figuritas'''
