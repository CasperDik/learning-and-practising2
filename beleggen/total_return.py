from meesman_wereldwijd_totaal import meesman_investment
from matplotlib import pyplot as plt

class plot():
    def __init__(self, n):
        self.n = n
        self.total_return = meesman_investment().total_return()

        self.monte_carlo()
        self.effect_return()

    def monte_carlo(self):
        self.x_range = self.total_return[0]
        self.nested_list = []

        for i in range(self.n):
            x = meesman_investment().total_return()[1]
            self.nested_list.append(x)
            plt.plot(self.x_range, self.nested_list[i])

        self.linear = self.total_return[2]
        plt.plot(self.x_range,self.linear, "red")
        plt.xlabel("months")
        plt.ylabel("in euros")
        plt.show()

    def effect_return(self):
        self.effective_returns = []

        for i in range(self.n):
            x = meesman_investment().total_return()[3]
            self.effective_returns.append(x)
            plt.plot(self.x_range, self.effective_returns[i])

        plt.ylabel("return")
        plt.xlabel("months")
        plt.show()


plot(5)