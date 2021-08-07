import fitparse

speed = []
cadence = []
heart_rate = []
temperature = []
distance = []
altitude = []
# todo: add running characteristics?
# todo: add time, how? does it record every second?

# Load the FIT file
# todo: loop over multiple files
fitfile = fitparse.FitFile("my_activity.fit")

# Iterate over all messages of type "record"
# (other types include "device_info", "file_creator", "event", etc)
for record in fitfile.get_messages("record"):

    # Records can contain multiple pieces of data (ex: timestamp, latitude, longitude, etc)
    for data in record:

        # Print the name and value of the data (and the units if it has any)
        if data.units:
            print(" * {}: {} ({})".format(data.name, data.value, data.units))
            # todo: do this for all interesting data, make it more pythonic-->loop?
            # todo: change list to dataframe
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
        else:
            print(" * {}: {}".format(data.name, data.value))

    print("---")

print(len(speed))

# todo: store all data from dataframe as csv

