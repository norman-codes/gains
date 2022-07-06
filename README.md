# gains
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
