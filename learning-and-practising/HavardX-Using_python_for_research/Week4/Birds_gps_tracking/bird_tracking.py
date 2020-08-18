import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime

birddata = pd.read_csv("bird_tracking.csv")
bird_names = pd.unique(birddata.bird_name)

plt.figure(figsize=(7,7))
for bird_name in bird_names:
    ix = birddata.bird_name == bird_name
    x, y = birddata.longitude[ix], birddata.latitude[ix]
    plt.plot(x,y,".", label=bird_name)

plt.xlabel("Longitude")
plt.xlabel("Latitude")
plt.legend(loc="lower right")
plt.show()
