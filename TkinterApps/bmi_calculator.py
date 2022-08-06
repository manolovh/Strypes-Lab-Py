from tkinter import *
from tkinter import ttk

def calculate_bmi():
    wght = float(weight.get())
    hght = float(height.get()) / 100
    result.set(round(wght / hght ** 2, 1))

root = Tk()
root.title("BMI Calculator")

mainFrame = ttk.Frame(root, padding="3 3 12 12")
mainFrame.grid(row=0, column=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

weight = DoubleVar()
weight_entry = ttk.Entry(mainFrame, width=10, textvariable=weight)
weight_entry.grid(column=2, row=1, sticky='we')

height = DoubleVar()
weight_entry = ttk.Entry(mainFrame, width=10, textvariable=height)
weight_entry.grid(column=2, row=2, sticky='we')

result = StringVar()
ttk.Label(mainFrame, textvariable=result).grid(column=2, row=3, sticky=(W, E))


ttk.Button(mainFrame, text="Calculate", command=calculate_bmi).grid(column=3, row=3, sticky=W)
ttk.Label(mainFrame, text="Kilograms").grid(column=3, row=1, sticky=W)
ttk.Label(mainFrame, text="Centimeters").grid(column=3, row=2, sticky=W)


root.mainloop()