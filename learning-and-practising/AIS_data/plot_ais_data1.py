import pandas as pd
import numpy as np
import smopy
import matplotlib.pyplot as plt
from matplotlib import colors as mcolors
from collections import Counter
from itertools import chain
import random

ais_points = pd.read_csv("data/other/validation_set_winter.csv")
harbors = pd.read_csv("data/other/ports.csv")

ais_cor = ais_points[["lon", "lat", "mmsi"]]
harbors_cor = harbors[["lat", "lon"]].dropna()
harbors_cor = harbors_cor.astype(float)
del ais_points, harbors

map = smopy.Map((min(ais_cor["lat"]), min(ais_cor["lon"]), max(ais_cor["lat"]), max(ais_cor["lon"])), z=12)
ax = map.show_mpl(figsize=(10, 10))

duplicates = list(Counter(ais_cor["mmsi"].to_list()).values())
colors = list(dict(mcolors.BASE_COLORS, **mcolors.CSS4_COLORS).keys())
random.shuffle(colors)
colors = colors[:len(duplicates)]

c = []
for i in range(len(duplicates)):
    c.append(list(np.repeat(colors[i], duplicates[i])))
c = list(chain.from_iterable(c))

# convert lats&longs to pixels
x, y = map.to_pixels(ais_cor["lat"], ais_cor["lon"])
x_har, y_har = map.to_pixels(harbors_cor["lat"], harbors_cor["lon"])

ax.scatter(x, y, s=0.1, c=c)
ax.scatter(x_har, y_har, s=15, c="k", marker="s")

plt.show()
