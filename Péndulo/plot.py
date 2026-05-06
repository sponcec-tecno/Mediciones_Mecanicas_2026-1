import numpy as np
import matplotlib.pylab as plt

datos=np.genfromtxt("data.dat")

fig, ax = plt.subplots()
ax.plot(t, u, label="u(x)")
ax.plot(t, v, label="v(x)")
ax.set_xlabel('t')
ax.set_ylabel('u(t) y v(t)')
ax.legend()

plt.savefig('serie.pdf')
