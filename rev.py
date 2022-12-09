from matplotlib.pyplot import *
from matplotlib.widgets import *
from math import *
from random import *
from numpy import *
from tkinter import *
import tkinter
root = tkinter.Tk()
root.title("Welcome to Selection of Unit Test")
root.geometry('350x200')
lbl = Label(root, text = "Please select the unit")
lbl.grid()
CheckVar1 = IntVar()
CheckVar2 = IntVar()
C1 = Checkbutton(root, text = "Unit1", variable = CheckVar1, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20)
C2 = Checkbutton(root, text = "unit2", variable = CheckVar2, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20)

C1.pack()
C2.pack()
root.mainloop()
