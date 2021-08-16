from tkinter import *
from tkinter import filedialog
from fit_to_csv import fit_to_csv
from tkinter import messagebox
from sys import exit

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


