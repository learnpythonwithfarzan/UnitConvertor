from tkinter import *
from tkinter.font import *


window = Tk()
window.title('Unit Convertor')
myFontLabel = Font(family='Ubuntu', size=17)
myFontEntry = Font(family='Ubuntu', size=15)
myFontListBox = Font(family='Ubuntu', size=13)
myFontButton = Font(family='Ubuntu', size=19)
labelForeground = 'yellow'
windowBackground = '#100720'
entryBackground = '#31087B'
textColor = '#FA2FB5'
entryTextColor = '#FFC23C'

window.config(background=windowBackground)


labelFrom = Label(window, text='From', font=myFontLabel, background=windowBackground, foreground=textColor)
labelFrom.grid(column=0, row=0)

labelResult = Label(window, text='Result', font=myFontLabel, background=windowBackground, foreground=textColor)
labelResult.grid(column=1, row=0)

entryFrom = Entry(window, font=myFontEntry, background=entryBackground, foreground=entryTextColor)
entryFrom.grid(column=0, row=1, padx=20, pady=10, sticky=E+W)

entryResult = Entry(window, font=myFontEntry, background=entryBackground, foreground=entryTextColor)
entryResult.grid(column=1, row=1, padx=20, pady=10, sticky=E+W)

listBoxFrom = Listbox(window, exportselection=False, font=myFontListBox)
listBoxFrom.config(background=entryBackground, foreground=textColor)
listBoxFrom.grid(column=0, row=2, padx=20, pady=10, sticky=E+W)
listBoxFrom.insert(END, 'MilliMeter')
listBoxFrom.insert(END, 'CentiMeter')
listBoxFrom.insert(END, 'Inch')
listBoxFrom.insert(END, 'KiloMeter')
listBoxFrom.insert(END, 'Feet')
listBoxFrom.insert(END, 'Yard')
listBoxFrom.insert(END, 'Miles')

listBoxTo = Listbox(window, exportselection=False, font=myFontListBox)
listBoxTo.config(background=entryBackground, foreground=textColor)
listBoxTo.grid(column=1, row=2, padx=20, pady=10, sticky=E+W)
listBoxTo.insert(END, 'MilliMeter')
listBoxTo.insert(END, 'CentiMeter')
listBoxTo.insert(END, 'Inch')
listBoxTo.insert(END, 'KiloMeter')
listBoxTo.insert(END, 'Feet')
listBoxTo.insert(END, 'Yard')
listBoxTo.insert(END, 'Miles')

calculateButton = Button(window, text='Calculate', font=myFontButton, fg=textColor, bg=entryBackground)
calculateButton.grid(column=0, row=3, columnspan=2, sticky=E+W)

window.mainloop()
