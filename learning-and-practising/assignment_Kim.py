import pandas as pd
import numpy as np
import smopy
import matplotlib.pyplot as plt
from matplotlib import colors as mcolors
from collections import Counter
from itertools import chain
import random

# import data
postcodes = pd.read_csv('data/postcodes.csv')

# create map with smopy

points = postcodes["Postcode"]
lats = postcodes["Latitude"]
longs = postcodes["Longitude"]

# create series with districts
districts = postcodes["Postcode"].str[:4]
duplicates = list(Counter(districts.to_list()).values())
districts = districts.drop_duplicates().reset_index(drop=True)

# setup map
map = smopy.Map((min(lats), min(longs), max(lats), max(longs)), z=12)
ax = map.show_mpl(figsize=(10, 10))

# convert lats&longs to pixels
x, y = map.to_pixels(lats, longs)

# get different colors
colors = list(dict(mcolors.BASE_COLORS, **mcolors.CSS4_COLORS).keys())
random.shuffle(colors)
colors = colors[:len(districts)]

c = []
for i in range(len(duplicates)):
    c.append(list(np.repeat(colors[i], duplicates[i])))
c = list(chain.from_iterable(c))

# plot the points
ax.scatter(x, y, s=3, c=c)
#plt.show()


# 1.3
# additional imports
from elasticsearch import Elasticsearch
from datetime import datetime, date
import holidays

# import data
deliveries = pd.read_csv('data/deliveries.csv')

# get nl public holidays
nl_holidays = list(holidays.Netherlands(years=2020).keys())

# todo: setup elastic search
es = Elasticsearch([{'host': 'localhost', 'port': 9200}]).ping()
print (es)


# todo: remove holidays
# todo: daily average deliveries for each location
# todo: total daily average deliveries for each district
# todo: Plot total average deliveries for each district on a bar chart.

#Gro_PC_distance = pd.read_csv('data/groningenPostcodeDistances.csv')