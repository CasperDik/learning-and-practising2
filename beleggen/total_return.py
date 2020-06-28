from meesman_wereldwijd_totaal import meesman_investment
from matplotlib import pyplot as plt

def monte_carlo(n,m):
    x_range = meesman_investment().total_return()[0]
    nested_list = []

    for i in range(n):
        x = meesman_investment().total_return()[1]
        nested_list.append(x)
        plt.plot(x_range, nested_list[i])

    linear = meesman_investment().total_return()[2]
    plt.plot(x_range,linear, "red")
    plt.ylim(0, (nested_list[0][m]*2))
    plt.xlim(0, m)
    plt.xlabel("months")
    plt.ylabel("in euros")
    plt.show()

def effective_returns(n):
    x_range = meesman_investment().total_return()[0]
    x_range.pop(0)
    effective_returns = []

    for i in range(n):
        x = meesman_investment().total_return()[3]
        effective_returns.append(x)
        plt.plot(x_range, effective_returns[i])

    plt.show()

monte_carlo(50,420)
effective_returns(2)