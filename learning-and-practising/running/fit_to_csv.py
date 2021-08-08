import fitparse
import pandas as pd

time = []
speed = []
cadence = []
heart_rate = []
temperature = []
distance = []
altitude = []
stance_time = []
stance_time_balance = []        # on left foot
step_length = []
vertical_oscillation = []
vertical_ratio = []

df = pd.DataFrame(columns=["time", "speed", "cadence", "heart_rate", "temperature", "distance", "altitude", "stance_time", "stance_time_balance", "step_length", "vertical_oscillation", "vertical_ratio"])

# Load the FIT file
fitfile = fitparse.FitFile("my_activity8.fit")

# Iterate over all messages of type "record"
# (other types include "device_info", "file_creator", "event", etc)
for record in fitfile.get_messages("record"):

    # Records can contain multiple pieces of data (ex: timestamp, latitude, longitude, etc)
    for data in record:

        # Print the name and value of the data (and the units if it has any)
        if data.units:
            # print(" * {}: {} ({})".format(data.name, data.value, data.units))
            if data.name == "speed":
                speed.append(data.value)
            if data.name == "cadence":
                cadence.append(data.value)
            if data.name == "heart_rate":
                heart_rate.append(data.value)
            if data.name == "temperature":
                temperature.append(data.value)
            if data.name == "altitude":
                altitude.append(data.value)
            if data.name == "distance":
                distance.append(data.value)
            if data.name == "stance_time":
                stance_time.append(data.value)
            if data.name == "stance_time_balance":
                stance_time_balance.append(data.value)
            if data.name == "step_length":
                step_length.append(data.value)
            if data.name == "vertical_oscillation":
                vertical_oscillation.append(data.value)
            if data.name == "vertical_ratio":
                vertical_ratio.append(data.value)
        else:
            if data.name == "timestamp":
                t = str(data.value)
                time.append(t[-8:])

# lists to dataframe
df["time"] = time
df["speed"] = speed
df["cadence"] = cadence
df["heart_rate"] = heart_rate
df["temperature"] = temperature
df["distance"] = distance
df["altitude"] = altitude
if len(stance_time) > 0:
    df["stance_time"] = stance_time
    df["stance_time_balance"] = stance_time_balance
    df["step_length"] = step_length
    df["vertical_oscillation"] = vertical_oscillation
    df["vertical_ratio"] = vertical_ratio

df.to_csv("running_raw_data8.csv")