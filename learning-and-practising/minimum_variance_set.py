import matplotlib.pyplot as plt
import numpy as np


def expected_return_portfolio(w1,w2,r1,r2):
    E_p = w1 * r1 + w2 * r2
    return E_p

def st_dev_portfolio(w1, w2, var1, var2, ro):
    st_portf = (w1 ** 2 * var1 ** 2 + w2 ** 2 * var2 ** 2 + 2 * w1 * w2 * var2 * var1 * ro) ** 0.5
    return st_portf

ro = 0.5
r1 = 0.04
r2 = 0.08
var1 = 0.2
var2 = 0.3

w1 = np.linspace(0,1,100)
E_r = []
port_st_dev = []

for i in w1:
    w2 = 1 - i
    E_r.append(expected_return_portfolio(i,w2,r1,r2))
    port_st_dev.append(st_dev_portfolio(i, w2, var1, var2, ro))

plt.plot(port_st_dev, E_r)
plt.xlabel("Standard deviation")
plt.ylabel("Expected return")
plt.show()