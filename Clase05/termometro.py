#EJERCICIO 5.5
import random
import numpy as np

temp = []

for i in range(100):
    error = random.normalvariate(0, 0.2)
    temp.append(37.5 + error)

maxima = round(max(temp), 4)
minima = round(min(temp), 4)

temps = np.array(temp)
promedio = round(np.average(temps), 4)
mediana = round(np.median(temps), 4)

print(maxima, minima, promedio, mediana)

#EJERCICIO 5.7
temp2 = []

for i in range(1000):
    error = random.normalvariate(0, 0.2)
    temp2.append(37.5 + error)

temps2 = np.array(temp2)

np.save('../Data/Temperaturas.npy', temps2)