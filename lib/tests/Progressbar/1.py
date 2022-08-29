from tkinter import *
from tkinter import ttk
from time import sleep

import threading


def exit(): raise SystemExit


root = Tk()
root.geometry('100x200+300+300')
# root.wm_attributes('-fullscreen', True)

label = Label(root, text="Here is label.")
label.pack()

i = 0

bar = ttk.Progressbar(root, variable=i, mode='determinate')
bar.pack()


def action():
	global i
	while True:
		print(i)
		i += 1
		if i == 110:
			exit()
		bar['value'] = i
		sleep(0.1)


# root.after(0, action)
threading.Thread(target=action).start()
    # See https://ru.stackoverflow.com/questions/697308/%D0%9A%D0%B0%D0%BA-%D1%81%D0%B4%D0%B5%D0%BB%D0%B0%D1%82%D1%8C-%D0%BF%D1%80%D0%B0%D0%B2%D0%B8%D0%BB%D1%8C%D0%BD%D0%BE-progressbar-%D0%B2-tkinter

# root.after(1_000, action)
# action()

root.mainloop()
