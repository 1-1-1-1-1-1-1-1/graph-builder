# Copied from https://www.delftstack.com/ru/tutorial/tkinter-tutorial/tkinter-combobox/.
# Codestyle of it was edited.


# Part 1
# Пример комбинированной коробки Python Tkinter

import tkinter as tk
from tkinter import ttk


app = tk.Tk() 
app.geometry('200x100')

labelTop = tk.Label(app, text="Choose your favourite month")
labelTop.grid(column=0, row=0)

comboExample = ttk.Combobox(app, 
                            values=[
                                    "January", 
                                    "February",
                                    "March",
                                    "April"])
print(dict(comboExample))  # `pprint` was edited to `print`.
comboExample.grid(column=0, row=1)
comboExample.current(1)

print(comboExample.current(), comboExample.get())

app.mainloop()


# Part 2
# Комбинированные шрифты Tkinter

import tkinter as tk
from tkinter import ttk
 
app = tk.Tk() 
app.geometry('300x100')

labelTop = tk.Label(app,
                    text = "Choose your favourite month")
labelTop.grid(column=0, row=0)

fontExample = ("Courier", 16, "bold")
comboExample = ttk.Combobox(app, 
                            values=[
                                    "January", 
                                    "February",
                                    "March",
                                    "April"],
                            font = fontExample)

app.option_add('*TCombobox*Listbox.font', fontExample)




comboExample.grid(column=0, row=1)

app.mainloop()


# Part 3
# Tkinter Combobox привязка к событию

import tkinter as tk
from tkinter import ttk

def callbackFunc(event):
     print("New Element Selected")
     
app = tk.Tk() 
app.geometry('200x100')

labelTop = tk.Label(app,
                    text = "Choose your favourite month")
labelTop.grid(column=0, row=0)

comboExample = ttk.Combobox(app, 
                            values=[
                                    "January", 
                                    "February",
                                    "March",
                                    "April"])


comboExample.grid(column=0, row=1)
comboExample.current(1)

comboExample.bind("<<ComboboxSelected>>", callbackFunc)


app.mainloop()


# Part 4
# Tkinter Combobox Динамически обновлять значения

import tkinter as tk
from tkinter import ttk

def callbackFunc(event):
     print("New Element Selected")
     
app = tk.Tk() 
app.geometry('200x100')

def changeMonth():
    comboExample["values"] = ["July",
                              "August",
                              "September",
                              "October"
                                ]

labelTop = tk.Label(app,
                    text = "Choose your favourite month")
labelTop.grid(column=0, row=0)

comboExample = ttk.Combobox(app, 
                            values=[
                                    "January", 
                                    "February",
                                    "March",
                                    "April"],
                            postcommand=changeMonth)


comboExample.grid(column=0, row=1)

app.mainloop()


# Part 5
# Tkinter Комбобокс только для чтения

import tkinter as tk
from tkinter import ttk
 
app = tk.Tk() 
app.geometry('200x100')

labelTop = tk.Label(app,
                    text = "Choose your favourite month")
labelTop.grid(column=0, row=0)

comboExample = ttk.Combobox(app, 
                            values=[
                                    "January", 
                                    "February",
                                    "March",
                                    "April"],
                            state="readonly")
# "Если вы измените состояние с readonly на disabled, то
# Комбобокс закрасится серым цветом, как показано ниже."

comboExample.grid(column=0, row=1)
comboExample.current(0)

print(comboExample.current(), comboExample.get())

app.mainloop()
