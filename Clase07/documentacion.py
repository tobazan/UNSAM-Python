# EJERCICIO 7.8

#%%
def valor_absoluto(n):
    '''
    Pre: recibe un numero
    Pos: retorna el valor absoluto de dicho numero
    '''
    if n >= 0:
        return n
    else:
        return -n

#%%
def suma_pares(l):
    '''
    Pre: recibe una lista de numeros
    Pos: devuelve la suma acumulada de los elementos pares
    '''
    res = 0
    for e in l:
        if e % 2 == 0:
            res += e
        else:
            res += 0

    return res

#%%
def veces(a, b):
    ''' 
    Parameters
    ----------
    a : TYPE number
    b : TYPE number

    Returns
    -------
    res : TYPE number
        DESCRIPTION producto de a por b
    '''
    res = 0
    nb = b
    while nb != 0:
        #print(nb * a + res)
        res += a
        nb -= 1
    return res

#%%
def collatz(n):
    '''
    Devuelve la cantidad de pasos de la sucesion para la conjetura de Collatz de n
    '''
    res = 1

    while n!=1:
        if n % 2 == 0:
            n = n//2
        else:
            n = 3 * n + 1
        print(n)
        res += 1

    return res