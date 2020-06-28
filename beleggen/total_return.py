from meesman_wereldwijd_totaal import meesman_investment
from matplotlib import pyplot as plt


def monte_carlo(n):
    x_range = meesman_investment().total_return()[0]
    nested_list = []

    for i in range(n):
        x = meesman_investment().total_return()[1]
        nested_list.append(x)
        plt.plot(x_range, nested_list[i])

    linear = meesman_investment().total_return()[2]
    plt.plot(x_range,linear, "red")

    plt.show()

monte_carlo(5)