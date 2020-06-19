from Black_and_Scholes.BS_model import euro_vanilla, euro_vanilla_dividend
from matplotlib import pyplot as plt

X = 100
T = 1
r = 0.05
d = 0.01
sigma = 0.25
option = "call"
values = []
x_range = []



for s in range(1,100):
    value = euro_vanilla_dividend(s, X, T, r, d, sigma, option=option)
    x_range.append(s)
    values.append(value)

plt.plot(x_range, values)

plt.xlabel("spot price")
plt.ylabel("value of the " + option + " option")
plt.show()