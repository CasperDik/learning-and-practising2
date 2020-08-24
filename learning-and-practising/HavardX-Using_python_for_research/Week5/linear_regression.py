import numpy as np
import scipy.stats as ss
import matplotlib.pyplot as plt
import statsmodels.api as sm

n = 100
beta_0 = 5
beta_1 = 2
np.random.seed(1)
x = 10 * ss.uniform.rvs(size=n)
y = beta_0 + beta_1 * x + ss.norm.rvs(loc=0, scale=1, size=n)
xx = np.array([0,10])

mod = sm.OLS(y, x)
est = mod.fit()

X = sm.add_constant(x)
mod = sm.OLS(y, X)
est = mod.fit()
print(est.summary())