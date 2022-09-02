from tkinter import *
from tkinter.font import *


window = Tk()
window.title('Unit Convertor')
myFontLabel = Font(family='Ubuntu', size=17)
myFontEntry = Font(family='Ubuntu', size=15)
myFontListBox = Font(family='Ubuntu', size=13)
myFontButton = Font(family='Ubuntu', size=19)


labelFrom = Label(window, text='From', font=myFontLabel)
labelFrom.grid(column=0, row=0)

labelResult = Label(window, text='Result', font=myFontLabel)
labelResult.grid(column=1, row=0)

entryFrom = Entry(window, font=myFontEntry)
entryFrom.grid(column=0, row=1)

entryResult = Entry(window, font=myFontEntry)
entryResult.grid(column=1, row=1)

listBoxFrom = Listbox(window, exportselection=False, font=myFontListBox)
listBoxFrom.grid(column=0, row=2)
listBoxFrom.insert(END, 'MilliMeter')
listBoxFrom.insert(END, 'CentiMeter')
listBoxFrom.insert(END, 'Inch')
listBoxFrom.insert(END, 'KiloMeter')
listBoxFrom.insert(END, 'Feet')
listBoxFrom.insert(END, 'Yard')
listBoxFrom.insert(END, 'Miles')

listBoxTo = Listbox(window, exportselection=False, font=myFontListBox)
listBoxTo.grid(column=1, row=2)
listBoxTo.insert(END, 'MilliMeter')
listBoxTo.insert(END, 'CentiMeter')
listBoxTo.insert(END, 'Inch')
listBoxTo.insert(END, 'KiloMeter')
listBoxTo.insert(END, 'Feet')
listBoxTo.insert(END, 'Yard')
listBoxTo.insert(END, 'Miles')

calculateButton = Button(window, text='Calculate', font=myFontButton)
calculateButton.grid(column=0, row=3, columnspan=2, sticky=E+W)
