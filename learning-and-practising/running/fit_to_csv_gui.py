from tkinter import *
from tkinter import filedialog
from fit_to_csv import fit_to_csv
from tkinter import messagebox
from sys import exit

class fit2csv(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master=master)
        self.master.title(".fit to .csv")
        self.grid(row=12, column=3, sticky=NSEW)

        # Setup buttons
        self.file_button = Button(self, text="select .fit file to .csv", command=self.select_file)
        self.output_location = Button(self, text="select location to store .csv file", command=self.output_location)
        self.convert_button = Button(self, text="convert", command=self.convert_file)
        self.filename = Entry(self, text="enter new file name here")
        # todo: edit entry layout

        # place buttons on canvas
        self.file_button.grid()
        self.output_location.grid()
        self.filename.grid()
        self.convert_button.grid()
        # todo: edit layout

    def select_file(self):
        self.file = filedialog.askopenfilename()
        if self.file[-4:] != ".fit":
            messagebox.showerror(title="Error", message="wrong file type selected.\nPlease try again with a .fit file")
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


