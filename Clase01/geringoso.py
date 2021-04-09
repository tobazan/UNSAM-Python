#geringoso.py

palabra = input('tipee una palabra para traducirla a geringoso: ')

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

print(f'\n{geringoso(palabra)}')