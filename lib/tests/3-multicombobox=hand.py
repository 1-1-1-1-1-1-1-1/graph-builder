# Copied from https://stackoverrun.com/ru/q/9310410.
# Edited in a sense of codestyle.


from tkinter import *

top = Tk()

mb = Menubutton(top, text="CheckComboBox", relief=RAISED)
mb.pack()  # <- Was edited: mb.grid()
mb.menu = Menu(mb, tearoff=0)
mb["menu"] = mb.menu

item0 = IntVar()
item1 = IntVar()
item2 = IntVar()

mb.menu.add_checkbutton(label="item0", variable=item0)
mb.menu.add_checkbutton(label="item1", variable=item1)
mb.menu.add_checkbutton(label="item2", variable=item2)


# This part is only for testing
def item_test():
    if item0.get() == True:
        print("item0 True")
    elif item0.get() == False:
        print("item0 False")
    else:
        print(item0.get())
     
    if item1.get() == True:
        print("item1 True")
    elif item1.get() == False:
        print("item1 False")
    else:
        print(item1.get())

    if item2.get() == True:
        print("item2 True")
    elif item2.get() == False:
        print("item2 False")
    else:
        print(item2.get())

button1 = Button(top, text="item True/False Test", command=item_test)
button1.pack()


mb.pack()
top.mainloop()
