# informe_funciones.py
import fileparse

def leer_precios(file):
    precios = fileparse.parse_csv(file, has_headers = False)
    return precios

def leer_camion(file):
    camion = fileparse.parse_csv(file, ['nombre', 'cajones', 'precio'], [str, int, float])
    return camion

precios = leer_precios('../Data/precios.csv')
camion = leer_camion('../Data/fecha_camion.csv')

def hacer_informe(camion, precios):
    balance = 0
    
    h = ['Nombre', 'Cajones', 'Precio', 'Cambio']
    print(f'{h[0]:^10s} {h[1]:^10s} {h[2]:^10s} {h[3]:^10s}')
    print('---------- ---------- ---------- ----------')

    for i in camion:
        cajones = i['cajones']
        costo_cajon = i['precio']
        precio_venta = float(precios.get(i['nombre']))
        
        balance += (cajones * (precio_venta - costo_cajon))
        
        r = [i['nombre'],cajones,costo_cajon,(precio_venta - costo_cajon)]
        print(f'{r[0]:<10s} {r[1]:^10d} ${r[2]:>9.2f} {r[3]:>9.2f}')
        
    print('---------- ---------- ---------- ----------')
    print(f'\nEl balance fue: ${balance}')

hacer_informe(camion,precios)

