import random
import matplotlib.pyplot as plt
import numpy as np

N = 10000
inleg = 1
p_succes = 4/37
multiplier_ifsucces = 9
x1 = np.arange(0,N+1)

for i in range(20):
    running_total = 0
    draw_running_total = []
    for i in range(1,N+2):
        draw = random.uniform(0,1)
        if draw <= p_succes:
            winst = inleg * multiplier_ifsucces - inleg
            running_total += winst
        else:
            running_total += -inleg
        draw_running_total.append(running_total/i)
    print(draw_running_total[N])
    plt.plot(x1, draw_running_total, alpha=0.3)

plt.hlines(0, 0, N, alpha=1)
plt.show()

