import numpy as np
import matplotlib.pylab as plt

datos=np.genfromtxt("data.dat")

fig, ax = plt.subplots()
ax.plot(datos[:,0], datos[:,1], label="my")
ax.plot(datos[:,0], np.cos(datos[:,0]), label="its", linestyle="--")
ax.set_xlabel('t(s)')
ax.set_ylabel('cos(t)')
ax.legend()

plt.savefig('compare.pdf')
