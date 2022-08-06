from urllib.request import urlopen
from tkinter import *
from tkinter import ttk

webpage = urlopen('http://slashdot.org/slashdot.rss').readlines()
titles = {}

for l in webpage:
    line = l.decode()
    title = ''

    if '<title>' in line:
        title_start = line.find('<title>') + 7
        title_end = line.find('</title>')
        curr_title = line[title_start:title_end]
        title = curr_title

    if '<description>' in line:
        description_start = line.find('<description>') + 13
        description_end = line.find('</description>')
        description = line[description_start: description_end]
        titles[curr_title] = description

def populate_listbox(data):
    list_box.delete(0, END)
    for element in data:
        list_box.insert(END, element)

def callback(event):
    selected = event.widget.curselection()
    if selected:
        index = selected[0]
        data = event.widget.get(index)
        text.config(text=titles[data])
    else:
        text.config(text='')

listbox_items = [title for title in titles.keys()]

main_window = Tk()
main_window.title('RSS Feed')
main_window.geometry('650x400')

main_frame = ttk.Frame(main_window)
main_frame.grid(row=0, column=0)

scrollbar = Scrollbar(main_frame, orient=VERTICAL)
scrollbar.grid(row=1, column=2, sticky='nsw')

list_box = Listbox(main_frame, width=80, height=10, yscrollcommand=scrollbar.set)
list_box.grid(row=1, column=1)

text = Label(main_frame, width=80, height=15, wraplength=500)
text.grid(row=3, column=1)

populate_listbox(listbox_items)
list_box.bind('<<ListboxSelect>>', callback)

scrollbar.config(command=list_box.yview)

main_window.mainloop()

