import math
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Calculator")
root.geometry('260x150')

mainframe = ttk.Frame(root)
mainframe.grid(row=0, column=0, sticky='nsew')
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

text = Entry(mainframe, width=25)
text.grid(column=1, columnspan=3, row=2, sticky='e')


def clear():
    global current
    text.delete(0, END)
    current = ''


def register(button):
    global current
    digit = text.get()
    text.delete(0, END)
    text.insert(0, str(digit) + button)
    current = current + str(button)


def add_dot():
    global current
    text_ = text.get()
    if '.' not in str(text_):
        text.delete(0, END)
        text.insert(0, str(text_) + '.')
        current = current + '.'


def show_result():
    global current
    sum = str(eval(current))
    text.delete(0, END)
    text.insert(0, sum)
    current = sum


def factoriel():
    global current
    fact = str(math.factorial(int(text.get())))
    text.delete(0, END)
    text.insert(0, fact)
    current = fact


def get_root():
    global current
    root = str(math.sqrt(float(text.get())))
    text.delete(0, END)
    text.insert(0, root)
    current = root


def m_clear():
    memory_hold.clear()


def m_plus():
    global current
    memory_hold.append(float(current))


def m_minus():
    global current
    memory_hold.append(-float(current))


def m_recall():
    global current
    current = str(sum(memory_hold))
    text.delete(0, END)
    text.insert(0, current)


def all_clear():
    global current
    text.delete(0, END)
    current = ''
    memory_hold.clear()


memory_hold = []
current = ''

point_button = ttk.Button(mainframe, text=".", command=add_dot, width=7)
point_button.grid(column=3, row=8, sticky=E)

button_0 = ttk.Button(mainframe, text="0", command=lambda: register('0'), width=7)
button_0.grid(column=2, row=8, sticky=E)

button_1 = ttk.Button(mainframe, text="1", command=lambda: register('1'), width=7)
button_1.grid(column=1, row=7, sticky=E)

button_2 = ttk.Button(mainframe, text="2", command=lambda: register('2'), width=7)
button_2.grid(column=2, row=7, sticky=E)

button_3 = ttk.Button(mainframe, text="3", command=lambda: register('3'), width=7)
button_3.grid(column=3, row=7, sticky=E)

button_4 = ttk.Button(mainframe, text="4", command=lambda: register('4'), width=7)
button_4.grid(column=1, row=6, sticky=E)

button_5 = ttk.Button(mainframe, text="5", command=lambda: register('5'), width=7)
button_5.grid(column=2, row=6, sticky=E)

button_6 = ttk.Button(mainframe, text="6", command=lambda: register('6'), width=7)
button_6.grid(column=3, row=6, sticky=E)

button_7 = ttk.Button(mainframe, text="7", command=lambda: register('7'), width=7)
button_7.grid(column=1, row=5, sticky=E)

button_8 = ttk.Button(mainframe, text="8", command=lambda: register('8'), width=7)
button_8.grid(column=2, row=5, sticky=E)

button_9 = ttk.Button(mainframe, text="9", command=lambda: register('9'), width=7)
button_9.grid(column=3, row=5, sticky=E)

divide_button = ttk.Button(mainframe, text="÷", command=lambda: register('/'), width=7)
divide_button.grid(column=4, row=4, sticky=E)

multiply_button = ttk.Button(mainframe, text="X", command=lambda: register('*'), width=7)
multiply_button.grid(column=4, row=5, sticky=E)

minus_button = ttk.Button(mainframe, text="-", command=lambda: register('-'), width=7)
minus_button.grid(column=4, row=6, sticky=E)

plus_button = ttk.Button(mainframe, text="+", command=lambda: register('+'), width=7)
plus_button.grid(column=4, row=7, sticky=E)

equals_button = ttk.Button(mainframe, text="=", command=show_result, width=7)
equals_button.grid(column=4, row=8, sticky=E)

factoriel_button = ttk.Button(mainframe, text="!", command=factoriel, width=7)
factoriel_button.grid(column=3, row=4, sticky=E)

root_button = ttk.Button(mainframe, text="√", command=get_root, width=7)
root_button.grid(column=2, row=4, sticky=E)

clear_entry = ttk.Button(mainframe, text="CE", command=clear, width=7)
clear_entry.grid(column=4, row=2, sticky='nsew')

memory_clear = ttk.Button(mainframe, text="mc", command=m_clear, width=7)
memory_clear.grid(column=5, row=4, sticky='nsew')

memory_plus = ttk.Button(mainframe, text="m+", command=m_plus, width=7)
memory_plus.grid(column=5, row=5, sticky='nsew')

memory_minus = ttk.Button(mainframe, text="m-", command=m_minus, width=7)
memory_minus.grid(column=5, row=6, sticky='nsew')

memory_recall = ttk.Button(mainframe, text="mr", command=m_recall, width=7)
memory_recall.grid(column=5, row=7, sticky='nsew')

all_clear = ttk.Button(mainframe, text="AC", command=all_clear, width=7)
all_clear.grid(column=5, row=2, sticky='nsew')

# Empty buttons
empty1 = ttk.Button(mainframe, text=" ", width=7, state=DISABLED)
empty1.grid(column=1, row=8, sticky=E)
empty2 = ttk.Button(mainframe, text="", width=7, state=DISABLED)
empty2.grid(column=1, row=4, sticky=E)
empty3 = ttk.Button(mainframe, text="", width=7, state=DISABLED)
empty3.grid(column=5, row=8, sticky=E)

root.mainloop()
