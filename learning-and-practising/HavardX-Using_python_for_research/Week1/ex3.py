# a
def moving_window_average(x, n_neighbors=1):
    n = len(x)
    width = n_neighbors * 2 + 1
    x = [x[0]] * n_neighbors + x + [x[-1]] * n_neighbors

    ma_list = []
    for i in range(n):
        ma = sum(x[i:(i + width)]) / width
        ma_list.append(ma)
    return ma_list


x = [0, 10, 5, 3, 1, 5]
print(moving_window_average(x, 1))

# b
import random

random.seed(1)

R = 1000
x = [random.uniform(0,1) for i in range(R)]
Y = [x] + [moving_window_average(x, i) for i in range(1, 10)]
print(Y[5][9])
