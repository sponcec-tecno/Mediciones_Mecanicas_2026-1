import numpy as np
import matplotlib.pylab as plt

datos=np.genfromtxt("sol.dat")
x = [0.262, 0.524, 0.785, 1.047]
y = [0.879, 0.889, 0.904, 0.926]

fig, ax = plt.subplots()
ax.plot(datos[:,0], datos[:,1], label="Curva teórica")
plt.scatter(x, y, color='red', s=10, label="Mis datos") 
ax.set_xlabel('Ángulo(rad)')
ax.set_ylabel('T(s)')
ax.legend()

plt.title("Solución teórica")
plt.savefig('solution.png')
