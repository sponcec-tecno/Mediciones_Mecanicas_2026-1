import numpy as np
import matplotlib.pylab as plt

th_0 = (3*np.pi/4)

def f(a):
  th_02 = np.pow(np.cos(th_0), 2)
  th2 = np.pow(np.cos(a), 2)
  return 1.0/(np.sqrt(th_02-th2))


datos=np.genfromtxt("sol.dat")
x, y = datos[:,0], datos[:,1]

fig, ax = plt.subplots()
ax.plot(x, y, label="My")
ax.plot(x, f(x), label="Its", linestyle="--")
# plt.scatter(x, y, color='red', s=10, label="Mis datos")
# ax.set_xlabel('Ángulo(rad)')
# ax.set_ylabel('T(s)')
ax.legend()

plt.title("Solución teórica")
#plt.savefig('solution.png')
