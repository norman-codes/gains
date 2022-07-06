'''
GAINS

An applet that takes in user input for daily exercises and exports it into a .csv file ("daily.csv").
    INPUT: simple interactive menu
    FORMAT: one day is one line.
        METADATA: date, category, # of exercises
        DATA PER EXERCISE: weight, reps

Capable of reading in data (from the .csv file) over a certain time range and showing trends using data visualization library.
    EVOLUTION over time per CATEGORY or EXERCISE.
    graphs, charts, etc. - need to look at what's possible before making decisions.

Helper features:
    - program learns from input
        all exercises inputted by the user are stored in a .csv file ("enames.csv", or exercise names)
        FORMAT: one category is one line.
            METADATA: category
            DATA: exercise name
'''

# LIBRARIES
# tkinter: used for gui
import tkinter as tk
from tkinter import font as tkfont
# matplotlib: used for data analysis & visualization
# import matplotlib as mp
# csv: used for dealing with file I/O
import csv

# GUI
# code structure (specifically switching between stacked frames) inspired by this post on StackOverflow:
# https://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter

class gains(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # Choosing the default font.
        self.title_font = tkfont.Font(family = 'Helvetica', size = 18, weight = "bold", slant = "italic")

        # The frame stack will function as a container for the three main frames
        # of the GUI; the user will call the one they wish to see to the top via buttons.
        framestack = tk.Frame(self)
        framestack.pack(side = "top", fill = "both", expand = True)
        framestack.grid_rowconfigure(0, weight = 1)
        framestack.grid_columnconfigure(0, weight = 1)

        self.frames = {}
        # Iterating through each page (each being a separate class)
        # and creating a frame for each one.
        for page in (Home, Log, Data):
            page_name = page.__name__
            frame = page(parent=framestack, controller=self)
            self.frames[page_name] = frame
            
            # Positioning the frames to be in the exact same location.
            frame.grid(row = 0, column = 0, sticky = "nsew")
        
        # Setting the default page as "Home".
        self.show_frame("Home")
    
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

class Home(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        homeTitle = tk.Label(self, text = "This is the home page.", font = controller.title_font)
        homeTitle.pack(side = "top", fill = "x", pady = 10)

        toLog = tk.Button(self, text = "Go to Exercise Logger.", command = lambda: controller.show_frame("Log"))
        toLog.pack()

        toData = tk.Button(self, text = "Go to Data Analysis.", command = lambda: controller.show_frame("Data"))
        toData.pack()

class Log(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        logTitle = tk.Label(self, text = "Welcome to the Exercise Log.", font = controller.title_font)
        logTitle.pack(side = "top", fill = "x", pady = 10)

        toHome = tk.Button(self, text = "Go to the home page.", command = lambda: controller.show_frame("Home"))
        toHome.pack()

class Data(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        dataTitle = tk.Label(self, text = "Welcome to the Data Analysis page.", font = controller.title_font)
        dataTitle.pack(side = "top", fill = "x", pady = 10)

        toHome = tk.Button(self, text = "Go to the home page.", command = lambda: controller.show_frame("Home"))
        toHome.pack()

class Day:
    date = ""
    category = ""
    num_exercises = 0
    exercises = {}

    def __init__(self, _date, _category, _num_exercises):
        self.date = _date
        self.category = _category
        self.num_exercises = _num_exercises
    
    # dict<string, list[list]]>
    # ex. Chin-Ups : [[52.5, 12], [52.5, 9], [59, 12]]
    def updateExercises(self, exercise_name, weightsList, repsList):
        
        combinedSet = [[weightsList, repsList]]
        self.exercises.update({exercise_name, combinedSet})

# root loop
if __name__ == "__main__":
    root = gains()
    root.mainloop()