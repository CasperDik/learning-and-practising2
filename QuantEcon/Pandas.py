import pandas as pd
import numpy as np


np.random.seed(1234)

data = np.random.randn(5,2)
dates  = pd.date_range("28/12/2018", periods=5)

df = pd.DataFrame(data, columns=("price", "weight"), index=dates)
print(df)
print(df.mean())
