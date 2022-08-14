from tkinter import *


root = Tk()
pw = PanedWindow(root, sashwidth=3, sashrelief=SUNKEN, orient=VERTICAL, width=316)
pw.pack(fill="both", expand="yes")

lf_1 = LabelFrame(pw, text=' LabelFrame 1 ', borderwidth=2, relief=SUNKEN, height=70)
pw.add(lf_1)
...

root.mainloop()
