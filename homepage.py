from tkinter import *
# Table class
class Table:
    # Initialize a constructor
    def __init__(self, gui):

        # An approach for creating the table
        for i in range(total_rows):
            for j in range(total_columns):
                print(i)
                if i ==0:
                    self.entry = Entry(gui, width=20, bg='LightSteelBlue',fg='Black',
                                       font=('Arial', 16, 'bold'))
                else:
                    self.entry = Entry(gui, width=20, fg='blue',
                               font=('Arial', 16, ''))

                self.entry.grid(row=i, column=j)
                self.entry.insert(END, list[i][j])


# take the data
list = [('S.NO', 'Size', 'Prize', 'EMI'),
        (1, '32 Sq ft','2500','12 month'),
       (2, '56 Sq ft','4500', ' 36 month'),
       ]

# find total number of rows and
# columns in list
total_rows = len(list)
total_columns = len(list[0])

# create root window
gui = Tk()
gui.title("Home page")
gui.geometry("900x300")

table = Table(gui)
gui.mainloop()