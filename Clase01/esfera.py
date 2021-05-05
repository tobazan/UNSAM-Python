import numpy as np

def vol_esfera(r):
    vol = (4/3) * np.pi * (r**3)
    return round(vol, 4)

radio = float(input('Por favor ingrese el valor del radio de la esfera: '))

print(f'El volumen de la esfera es de {vol_esfera(radio)}')