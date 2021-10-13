import pandas as pd
import smopy
import matplotlib.pyplot as plt
import numpy as np

#ais_points = pd.read_csv("data/DMA/raw/aisdk_20170623.csv")
#ais_cor = ais_points[["Longitude", "Latitude", "MMSI"]]
#ais_cor = ais_cor.rename(columns={"Longitude": "lon", "Latitude": "lat", "MMSI": "mmsi"})
#ais_cor.dropna(inplace=True)
#ais_cor.to_csv("data/DMA/processed/DMA1.csv", index=False)
#del ais_points

ais_cor = pd.read_csv("data/DMA/processed/DMA1.csv")
ais_points = pd.read_csv("data/other/validation_set_winter.csv")
ais_cor2 = ais_points[["lon", "lat", "mmsi"]]
map = smopy.Map((min(ais_cor2["lat"]), min(ais_cor2["lon"]), max(ais_cor2["lat"]), max(ais_cor2["lon"])), z=5)
ax = map.show_mpl(figsize=(10, 10))

# convert lats&longs to pixels
x, y = map.to_pixels(ais_cor["lat"], ais_cor["lon"])

ax.scatter(x, y, s=0.1)
plt.show()
