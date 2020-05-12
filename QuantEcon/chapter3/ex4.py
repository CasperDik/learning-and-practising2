import numpy as np
import matplotlib.pyplot as plt


T = 200
alpha = 0.9
x = np.empty(T+1)
x[0] = 0

for t in range(T):
    error_term = np.random.randn()
    if x[t] < 0:
        abs_x = -x[t]
    else:
        abs_x = x[t]
    x[t+1] = alpha * abs_x + error_term

plt.plot(x)
plt.show()