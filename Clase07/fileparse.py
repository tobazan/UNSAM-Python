# EJERCICIO 7.4

def parse_csv(iterable, select = None, types = None, has_headers = True):
    '''
    Parsea un iterable, podes seleccionar sólo un subconjunto de las columnas, determinando
    el parámetro select - debera ser una lista de nombres de las columnas a considerar.
    '''

    # Lee los encabezados del archivo
    if has_headers:    
        encabezados = next(iterable).replace('\n','').split(',')

        # Si se indicó un selector de columnas, buscar los índices.
        if select:
            indices = [encabezados.index(nombre_columna) for nombre_columna in select]
            encabezados = select
        else:
            indices = []
        
        registros = []
        
        for fila in iterable:
            # Saltear filas vacías
            if not fila:    
                continue
            
            fila = fila.split(',')

            # Filtrar la fila si se especificaron columnas
            if indices:
                fila = [fila[index] for index in indices]
                
            if types:
                fila = [func(val) for func, val in zip(types, fila)]

                
            # Armar el diccionario
            registro = dict(zip(encabezados, fila))
            registros.append(registro)
            
    else:
        registros = dict(fila.split(',') for fila in iterable)
            
    return registros

# lines = ['name,cajones,precio', 'Lima,100,34.23', 'Naranja,50,91.1', 'Mburucuya,75,45.1']
# lineas = ['Lima,100', 'Naranja,50', 'Mburucuya,75', 'Tomate,121']
# print(parse_csv(lines, select=['name', 'precio'], has_headers=True))
# print(parse_csv(lineas, has_headers=False))