import numpy as np
from matplotlib import pyplot as plt

class meesman_investment():
    def __init__(self):
        #yearly cost:
        self.TER = 0.005

        #composition
        self.c_world = 0.7858942
        self.c_emerging = 0.090813289
        self.c_small = 0.12329250942

        #return 3-year average
        self.r_world = 0.0864
        self.r_emerging = 0.0192
        self.r_small = 0.0204    #msci not nt

        #st. dev
        self.st_dev_world = 0.1545
        self.st_dev_emerging = 0.1599
        self.st_dev_small = 0.2082   #msci not nt

        #weighted returns and st dev
        self.sigma = self.c_world * self.st_dev_world + self.c_small * self.st_dev_small + self.c_emerging * self.st_dev_emerging
        self.mu = self.c_world * self.r_world + self.c_emerging * self.r_emerging + self.c_small * self.r_small

        #input
        self.monthly_investment = 700
        self.total_period = 35 * 12
        self.periods = 18    #months of loan
        self.interest = 0.00

        #run
        self.total_return()

    def normal_monthly(self):
        self.x = np.random.normal(self.mu/12, self.sigma/12, 1)
        return self.x[0]

    def total_return(self):
        self.total_inv = [0]
        self.x_range = [0]
        self.begin_inv = 0
        self.linear = [0]
        linear = 0
        for i in range(1, self.periods):
            r = self.normal_monthly()
            self.begin_inv = (1+r) * (self.monthly_investment + self.begin_inv)
            if i % 12:
                self.begin_inv * (1-self.TER)

            self.total_inv.append(self.begin_inv)
            self.x_range.append(i)
            linear += self.monthly_investment
            self.linear.append(linear)

        for i in range(self.periods, self.total_period):
            r = self.normal_monthly()
            self.begin_inv = (1 + r) * self.begin_inv
            if i % 12:
                self.begin_inv * (1 - self.TER)

            self.total_inv.append(self.begin_inv)
            self.x_range.append(i)
            linear = linear * ((1+self.interest)**(1/12))       #todo: aflossen, dus minder interest
            self.linear.append(linear)

        return self.x_range, self.total_inv, self.linear

    def plot_investment(self):
        plt.plot(self.x_range, self.total_inv)
        plt.plot(self.x_range, self.linear, "red")
        plt.show()
