# bbin.py
# ejercicio 6.12

def busqueda_binaria(lista, x, verbose = False):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Si el elemento esta en la lista devuelve su posicion p tal que lista[p] == x, si x está en lista
    Si el elemento NO esta, lo inserta de manera de mantener la lista ordenada y tambien retorna la posicion
    Ademas, retorna en la variable comps la cantidad de iteraciones que realizo para encontrar o no el numero
    '''
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    
    # pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    comps = 0
    
    while izq <= der:
        comps += 1
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            break           # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    
    lista.insert(medio, x)
    
    return lista, medio, comps

#TEST

print(busqueda_binaria([0,2,4,6], 3))

print(busqueda_binaria([0,2,4,6,8,11, 13, 14, 16], 9))