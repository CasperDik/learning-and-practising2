from tkinter import *
from tkinter import filedialog
from fit_to_csv import fit_to_csv
from tkinter import messagebox
from sys import exit
import fitparse
import pandas as pd

"""
notes:
coverted the .py file to .exe by:
-adding python to path in windows
-pip install pyinstaller & some packages (in this case pandas and fitparse) --> PIP install in command prompt!!
-code to generate .exe:
cd C:\Users\Casper Dik\PycharmProjects\learning-and-practising\running
pyinstaller --onefile --noconsole fit2csv_gui.py

https://datatofish.com/executable-pyinstaller/
"""


class fit2csv(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master=master)
        self.master.title(".fit to .csv")
        self.grid()

        # frame 1
        frame1 = Frame(self)
        frame1.pack(fill="x")

        self.L_file_button = Label(frame1, text="select file", width=12, anchor="w")
        self.file_button = Button(frame1, text="select", command=self.select_file)

        self.L_file_button.pack(side=LEFT, padx=5, pady=5)
        self.file_button.pack(fill=X, padx=5, expand=True)

        # frame 2
        frame2 = Frame(self)
        frame2.pack(fill="x")

        self.L_output_location = Label(frame2, text="output location", width=12, anchor="w")
        self.output_location = Button(frame2, text="select", command=self.output_location)

        self.L_output_location.pack(side=LEFT, padx=5, pady=5)
        self.output_location.pack(fill=X, padx=5, expand=True)

        # frame 3
        frame3 = Frame(self)
        frame3.pack(fill="x")

        self.L_entry = Label(frame3, text="new filename", width=12, anchor="w")
        self.filename = Entry(frame3)

        self.L_entry.pack(side=LEFT, padx=5, pady=5)
        self.filename.pack(fill=X, padx=5, expand=True)

        # frame 4
        frame4 = Frame(self)
        frame4.pack(fill="x")

        self.convert_button = Button(frame4, text="convert", command=self.convert_file)

        self.convert_button.pack(padx=70, fill="x")


    def select_file(self):
        self.file = filedialog.askopenfilename()
        if self.file[-4:] != ".fit":
            messagebox.showerror(title="Error", message="No file or wrong file type selected.\nPlease try again with a .fit file")
            exit()

    def output_location(self):
        self.output = filedialog.askdirectory()

    def convert_file(self):
        try:
            fit_to_csv(self.file, self.output, self.filename.get())
            messagebox.showinfo(title="Message", message=".fit file converted to .csv")
            exit()
        except AttributeError:
            messagebox.showerror(title="Error", message="No output location and/or file selected.\nPlease try again")
            exit()

    def fit_to_csv(self, file_location, output_location, filename):
        time = []
        speed = []
        cadence = []
        heart_rate = []
        temperature = []
        distance = []
        altitude = []
        stance_time = []
        stance_time_balance = []  # on left foot
        step_length = []
        vertical_oscillation = []
        vertical_ratio = []

        inputs = ["time", "speed", "cadence", "heart_rate", "temperature", "distance", "altitude", "stance_time",
                  "stance_time_balance", "step_length", "vertical_oscillation", "vertical_ratio"]
        df = pd.DataFrame(columns=inputs)

        fitfile = fitparse.FitFile(file_location)

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

        file_type = ".csv"
        df.to_csv(output_location + "/" + filename + file_type)


root = Tk()
x = fit2csv(root)

root.mainloop()


