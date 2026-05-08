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

a = [0.0175248, 0.00937745, 0.0223765, 0.872178]

def p(b):
  return (a[0]*(b**3))+(a[1]*(b*b))+(a[2]*(b))+a[3]

pol = p(x)

err1 = (abs((pol[2:-1]-0.9)-t)/(pol[2:-1]-0.9))*100
#err2 = (abs(t-((pol[2:-1])-0.9))/t)*100
fig, ax = plt.subplots()
#ax.plot(x[2:-1], t, label="Numéricamente")
#plt.scatter(x_xp, y_xp, color='red', s=10, label="Experimentales")
#ax.plot(x, pol-0.9, label="Ajuste polinómico")
ax.plot(x[2:-1]-1.0, err1)

ax.set_xlabel(r'$\theta(rad)$')
ax.set_ylabel(r'Error(%)')
#ax.legend()

plt.title("Comparación métodos (error del numérico frente al ajuste)")
plt.savefig("TF2.png")
