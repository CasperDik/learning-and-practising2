import numpy as np
import matplotlib.pyplot as plt


T = 200
alphas = [0, 0.8, 0.98]
x = np.empty(T+1)
x[0] = 0

for alpha in alphas:
    for t in range(T):
        error_term = np.random.randn()
        x[t+1] = alpha * x[t] + error_term
    plt.plot(x, label= "alpha = " + str(alpha))

plt.legend()
plt.show()