# EJERCICIO 7.10

import matplotlib.pyplot as plt
import numpy as np

def randomwalk(largo):
    pasos = np.random.randint (-1, 2, largo)    
    return pasos.cumsum()

N = 100000

walks = [randomwalk(N) for i in range(12)]

fig = plt.figure()
fig.supxlabel('pasos')
fig.supylabel('distancia')
plt.subplot(2, 1, 1, title='12 caminatas al azar') # sup
for walk in walks:
    plt.plot(walk)
plt.xticks([]), plt.ylim(-600,600)

max_dist = walks[0]
min_dist = walks[0]

for walk in walks:
    if abs(walk[N-1]) > abs(max_dist[N-1]):
        max_dist = walk
    
    if abs(walk[N-1]) < abs(min_dist[N-1]):
        min_dist = walk

plt.subplot(2, 2, 3, title='la que mas se aleja') # inf izq
plt.plot(max_dist)
plt.xticks([]), plt.ylim(-600,600)

plt.subplot(2, 2, 4, title='la que menos se aleja') # inf der
plt.plot(min_dist)
plt.xticks([]), plt.ylim(-600,600)

plt.show()