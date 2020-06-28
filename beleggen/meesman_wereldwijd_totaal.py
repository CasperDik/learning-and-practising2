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
        self.monthly_investment = 750
        self.max_loan_period = 35*12
        self.loan_period = 18
        self.total_period = self.loan_period + self.max_loan_period
        self.interest = 0.00
        self.transaction_cost = 0.0025
        self.eff_r = [1]

    def normal_monthly(self):
        self.x = np.random.normal(self.mu/12, self.sigma/12, 1)
        return self.x[0]

    def total_return(self):
        self.total_inv = [0]
        self.x_range = [0]
        self.begin_inv = 0
        self.linear = [0]
        linear = 0
        for i in range(1, self.loan_period):
            r = self.normal_monthly()
            self.begin_inv = (1+r) * ((self.monthly_investment*(1-self.transaction_cost)) + self.begin_inv)
            if i % 12:
                self.begin_inv * (1-self.TER)

            self.total_inv.append(self.begin_inv)
            self.x_range.append(i)
            linear += self.monthly_investment
            self.linear.append(linear)

        for i in range(self.loan_period, self.total_period):
            r = self.normal_monthly()
            self.begin_inv = (1 + r) * self.begin_inv
            if i % 12:
                self.begin_inv * (1 - self.TER)

            self.total_inv.append(self.begin_inv)
            self.x_range.append(i)
            linear = linear * ((1+self.interest)**(1/12))
            self.linear.append(linear)

        if len(self.eff_r) == 1:
            self.effective_return()

        return self.x_range, self.total_inv, self.linear, self.eff_r

    def plot_investment(self):
        plt.plot(self.x_range, self.total_inv)
        plt.plot(self.x_range, self.linear, "red")
        plt.show()

    def effective_return(self):
        self.P = self.monthly_investment * self.loan_period
        self.r = self.interest/12 +0.00000000001
        self.annuity = self.P/ ((1-(1+self.r)**(-self.max_loan_period))/self.r)

        for j in range(2, self.total_period):
            if j == 2:
                r1 = ((self.total_inv[j] - self.monthly_investment - self.total_inv[j-1])/self.total_inv[j-1]) + 1
                r11 = r1* self.eff_r[j-2]
                self.eff_r.append(r11)
            if j > self.loan_period:
                r2 = ((self.total_inv[j] - self.annuity - self.total_inv[j-1])/self.total_inv[j-1]) + 1
                r22 = r2 * self.eff_r[j-2]
                self.eff_r.append(r22)
            else:
                r3 = ((self.total_inv[j] - self.monthly_investment - self.total_inv[j-1])/self.total_inv[j-1]) + 1
                r33 = r3 * self.eff_r[j-2]
                self.eff_r.append(r33)
