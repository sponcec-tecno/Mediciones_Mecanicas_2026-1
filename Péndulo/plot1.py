import numpy as np
import matplotlib.pylab as plt

th_0 = (3*np.pi/4)

def f(a):
  th_02 = np.pow(np.cos(th_0), 2)
  th2 = np.pow(np.cos(a), 2)
  return 1.0/(np.sqrt(th_02-th2))


datos=np.genfromtxt("sol.dat")
x, y = datos[:,0], datos[:,1]
f_i = f(x)

fig, ax = plt.subplots()
ax.plot(x, y, label="Numéricamente")
ax.plot(x, f_i, label="Teóricamente", linestyle="--")
# plt.scatter(x, y, color='red', s=10, label="Mis datos")
ax.set_xlabel(r'$\vartheta$(rad)')
ax.set_ylabel(r'f($\vartheta$)')
ax.legend()

plt.title("Función a integrar")
#plt.savefig('compare2.png')

#Voy a integrar
def simp(x_i, f_t):
  fst = f_t[1]
  lst = f_t[-1]
  mid = f_t[1:-1]
  h = x_i[1]-x_i[0]
  pair = mid[::2]
  odd = mid[1::2]

  aux_3 = fst*h/3
  aux_4 = lst*h/3

  return aux_3+(np.sum(pair)*(4*h/3))+(np.sum(odd)*(2*h/3))+aux_4

n = len(x)

t = np.zeros(n-3)
a_x = x[0]
b_x = x[-1]
a_y = y[0]
b_y = y[-1]

for i in range(n-3):
  t[i] = simp(x[:i+3], y[:i+3])

x_xp = [0.262, 0.524, 0.785, 1.047]
y_xp = [0.879, 0.889, 0.904, 0.926]

g = 9.7754427
l = 0.15

t *= 1/2*np.sqrt(l/g)

fig, ax = plt.subplots()
ax.plot(x[2:-1], t, label="Numéricamente")
plt.scatter(x_xp, y_xp, color='red', s=10, label="Mis datos")
ax.set_xlabel(r'$\vartheta$(rad)')
ax.set_ylabel(r'F($\vartheta$)')
ax.legend()

plt.title("Función integrada")