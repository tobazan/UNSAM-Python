from informe_funciones import leer_camion

def costo_camion(filename):
    camion = leer_camion(filename)
    
    costo = 0
    
    for i in camion:
        costo += i['cajones'] * i['precio']
    
    return costo

costo_camion('../Data/camion.csv')    