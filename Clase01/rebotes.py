# rebotes.py
# Archivo de ejemplo
# Ejercicio

if __name__ == '__main__':

	altura_inicial = 100

	for rebote in range(10):
		altura_inicial = altura_inicial * 0.6
		print(round(altura_inicial, 4))