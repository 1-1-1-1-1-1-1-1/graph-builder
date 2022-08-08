Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def generate_password(size=40,
                      alphabet=string.ascii_letters + string.digits+".",
                      choice=secrets.choice):
    return ''.join([choice(alphabet) for _ in range(size)])

Traceback (most recent call last):
  File "<pyshell#0>", line 2, in <module>
    alphabet=string.ascii_letters + string.digits+".",
NameError: name 'string' is not defined
>>> import string
>>> import secrets
>>> from tkinter import BOTH, END, HORIZONTAL, Tk, scrolledtext, ttk
>>> scrolledtext
<module 'tkinter.scrolledtext' from 'C:\\Users\\hp\\AppData\\Local\\Programs\\Python\\Python38\\lib\\tkinter\\scrolledtext.py'>
>>> help(scrolledtext)

>>> __import__("tkinter").ScrolledText
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    __import__("tkinter").ScrolledText
AttributeError: module 'tkinter' has no attribute 'ScrolledText'
>>> def generate_password(size=40,
                      alphabet=string.ascii_letters + string.digits+".",
                      choice=secrets.choice):
    return ''.join([choice(alphabet) for _ in range(size)])

>>> def show_new_password():
    console.configure(state='normal')  # enable insert
    console.insert(END, generate_password() + '\n')
    console.yview(END)  # autoscroll
    console.configure(state='disabled')  # disable editing

    
>>> exec("""
root = Tk()
root.title("Simple Password Generator")
root.geometry("400x300")
ttk.Button(root, text='Generate', command=show_new_password).pack()
ttk.Separator(root, orient=HORIZONTAL).pack(fill=BOTH)  # line in-between
console = scrolledtext.ScrolledText(root, state='disable')
console.pack()
root.mainloop()""")

>>> 
