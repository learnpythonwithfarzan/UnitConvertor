from tkinter import *
from tkinter.font import *
from Commands import *


def calculate_unit():
    entry_from = int(entryFrom.get())
    list_box_from = listBoxFrom.get(ACTIVE)
    list_box_to = listBoxTo.get(ACTIVE)

    my_commands = Commands(entry_from, list_box_from, list_box_to)
    my_commands.units()
    entryResult.delete(0, END)
    entryResult.insert(END, my_commands.units())


window = Tk()
# change window title
window.title('Unit Convertor')
# make font variables
myFontLabel = Font(family='Ubuntu', size=17)
myFontEntry = Font(family='Ubuntu', size=15)
myFontListBox = Font(family='Ubuntu', size=13)
myFontButton = Font(family='Ubuntu', size=19)
# make foreground color variable
windowBackground = '#100720'
entryBackground = '#31087B'
textColor = '#FA2FB5'
entryTextColor = '#FFC23C'

# set window background
window.config(background=windowBackground)

# make from and result label and config it
labelFrom = Label(window, text='From', font=myFontLabel, background=windowBackground, foreground=textColor)
labelFrom.grid(column=0, row=0)

labelResult = Label(window, text='Result', font=myFontLabel, background=windowBackground, foreground=textColor)
labelResult.grid(column=1, row=0)

# make from and result entry and config it
entryFrom = Entry(window, font=myFontEntry, background=entryBackground, foreground=entryTextColor)
entryFrom.grid(column=0, row=1, padx=10, pady=10, sticky=E+W)

entryResult = Entry(window, font=myFontEntry, background=entryBackground, foreground=entryTextColor)
entryResult.grid(column=1, row=1, padx=10, pady=10, sticky=E+W)

# make listbox, config it and insert item
listBoxFrom = Listbox(window, exportselection=False, font=myFontListBox)
listBoxFrom.config(background=entryBackground, foreground=textColor)
listBoxFrom.grid(column=0, row=2, padx=10, pady=10, sticky=E+W)
listBoxFrom.insert(END, 'MilliMeter')
listBoxFrom.insert(END, 'CentiMeter')
listBoxFrom.insert(END, 'Inch')
listBoxFrom.insert(END, 'Feet')
listBoxFrom.insert(END, 'Yard')
listBoxFrom.insert(END, 'Meter')
listBoxFrom.insert(END, 'KiloMeter')
listBoxFrom.insert(END, 'Mile')

listBoxTo = Listbox(window, exportselection=False, font=myFontListBox)
listBoxTo.config(background=entryBackground, foreground=textColor)
listBoxTo.grid(column=1, row=2, padx=10, pady=10, sticky=E+W)
listBoxTo.insert(END, 'MilliMeter')
listBoxTo.insert(END, 'CentiMeter')
listBoxTo.insert(END, 'Inch')
listBoxTo.insert(END, 'Feet')
listBoxTo.insert(END, 'Yard')
listBoxTo.insert(END, 'Meter')
listBoxTo.insert(END, 'KiloMeter')
listBoxTo.insert(END, 'Mile')


# make calculate button and config it
calculateButton = Button(window, text='Calculate', font=myFontButton)
calculateButton.config(fg=textColor, bg=entryBackground, command=calculate_unit)
calculateButton.grid(column=0, row=3, columnspan=2, padx=10, pady=10, sticky=E+W)

window.mainloop()
