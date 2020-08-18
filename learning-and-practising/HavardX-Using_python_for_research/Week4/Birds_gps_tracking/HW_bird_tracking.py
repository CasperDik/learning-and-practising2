import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

birddata = pd.read_csv("https://courses.edx.org/asset-v1:HarvardX+PH526x+2T2019+type@asset+block@bird_tracking.csv", index_col=0)

grouped_birds = birddata.groupby("bird_name")
mean_speeds = grouped_birds["speed_2d"].mean()
mean_altitudes = grouped_birds["altitude"].mean()

birddata.date_time = pd.to_datetime(birddata.date_time)
birddata["date"] = birddata.date_time.dt.date
grouped_bydates = birddata.groupby("date")
mean_altitudes_perday = grouped_bydates.altitude.mean()

grouped_birdday = birddata.groupby(["bird_name", "date"])
mean_altitudes_perday1 = grouped_birdday.altitude.mean()

eric_daily_speed = grouped_birdday.speed_2d.mean()["Eric"]
nico_daily_speed = grouped_birdday.speed_2d.mean()["Nico"]
sanne_daily_speed = grouped_birdday.speed_2d.mean()["Sanne"]

eric_daily_speed.plot(label="Eric")
sanne_daily_speed.plot(label="Sanne")
nico_daily_speed.plot(label="Nico")
plt.legend(loc="upper left")
plt.show()