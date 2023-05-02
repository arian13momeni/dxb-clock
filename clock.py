from tkinter import *
from tkinter.ttk import *

from time import strftime

# creating window
window = Tk()
window.title('Clock')

# create label
lbl = Label(window, font=('calibri', 50, 'bold'),
            background='black',
            foreground='green1')

lbl.pack()


def displayTime():
    time = strftime('%H:%M:%S %p')
    lbl.config(text=time)
    lbl.after(1000, displayTime)


displayTime()
mainloop()