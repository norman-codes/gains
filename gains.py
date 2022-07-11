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

        toHomeLog = tk.Button(self, text = "Go to the home page.", command = lambda: controller.show_frame("Home"))
        toHomeLog.pack()

class Data(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        dataTitle = tk.Label(self, text = "Welcome to the Data Analysis page.", font = controller.title_font)
        dataTitle.pack(side = "top", fill = "x", pady = 10)

        toHomeData = tk.Button(self, text = "Go to the home page.", command = lambda: controller.show_frame("Home"))
        toHomeData.pack()

# An Exercise class following an object-oriented design pattern: one Exercise object will encapsulate its name and the number of sets (plus relevant information per set) performed.
class Exercise:
    # Name of the exercise.
    name = ""
    # 2D array (list of lists) representing the number of sets performed (1D) and the weight and number of reps per set (2D). 
        # Ex. [[130, 12], [130, 8], [110, 12]] represents a weight of 130 lbs and 12 reps for the first set, 130 lbs and 8 reps for the second set, and 110 lbs and 12 reps for the third set.
    sets = [[]]

    # Parametrized constructor taking in a name, an array of weights used and an array of reps performed (*IN ORDER OF SETS PERFORMED!*).
    def __init__(self, _name, numSets, weightList, repList):
        self.name = _name
        self.sets = [[(i, j) for j in range(2)] for i in range(numSets)]

# A Day class following an object-oriented desgin pattern: one Day object will encapsulate the workout's date, category (ex. upper push), exercises performed, and the number of exercises performed.
class Day:
    date = "" # date format CURRENTLY UNDECIDED
    category = ""
    exercises = []
    num_exercises = 0 # incremented per addition to list of exercises; equivalent to length of exercises array.

    def __init__(self, _date, _category, _exercises):
        self.date = _date
        self.category = _category
        for e in _exercises:
            self.addExercise(e)
    
    def addExercise(self, exercise):
        self.exercises.append(exercise)
        self.num_exercises += 1
        
# root loop
if __name__ == "__main__":
    root = gains()
    test = Exercise("bob")
    print(test.sets)
    root.mainloop()

    