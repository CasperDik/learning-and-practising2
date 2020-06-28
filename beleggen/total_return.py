from meesman_wereldwijd_totaal import meesman_investment
from matplotlib import pyplot as plt
import numpy as np
import bottleneck as bn

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
            plt.plot(self.x_range, self.nested_list[i], linewidth=0.5)

        self.linear = self.total_return[2]
        plt.plot(self.x_range,self.linear, "red")
        plt.xlabel("months")
        plt.ylabel("in euros")
        plt.show()

    def effect_return(self):
        self.effective_returns = []
        mm_list = []

        for i in range(self.n):
            x = meesman_investment().total_return()[3]
            self.effective_returns.append(x)
            mm = bn.move_mean(self.effective_returns[i], window=8, min_count=1)
            mm_list.append(mm)
            plt.plot(self.x_range, mm_list[i], linewidth=0.5)

        plt.ylabel("return")
        plt.xlabel("months")
        plt.show()


plot(50)