Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from tkinter import *
>>> infow = Tk()
>>> ttk.Progressbar(infow,  # variable=tests.parts_done,
                               variable=var,
                               maximum=9, value=0, mode='determinate')
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    ttk.Progressbar(infow,  # variable=tests.parts_done,
NameError: name 'ttk' is not defined
>>> from tkinter import ttk
>>> pbar = ttk.Progressbar(infow,  # variable=tests.parts_done,
                               variable=var,
                               maximum=9, value=0, mode='determinate')
Traceback (most recent call last):
  File "<pyshell#4>", line 2, in <module>
    variable=var,
NameError: name 'var' is not defined
>>> var = 0
>>> pbar = ttk.Progressbar(infow,  # variable=tests.parts_done,
                               variable=var,
                               maximum=9, value=0, mode='determinate')
>>> pbar.pack()
>>> var=1
>>> infow.state
<bound method Wm.wm_state of <tkinter.Tk object .>>
>>> infow.state()
'normal'
>>> infow.state('disabled')
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    infow.state('disabled')
  File "C:\Users\hp\AppData\Local\Programs\Python\Python38\lib\tkinter\__init__.py", line 2211, in wm_state
    return self.tk.call('wm', 'state', self._w, newstate)
_tkinter.TclError: bad argument "disabled": must be normal, iconic, withdrawn, or zoomed
>>> infow.state('zoomed')
''
>>> infow.state('normal')
''
>>> infow.state('iconic')
''
>>> infow.state('withdrawn')
''
>>> infow.state('normal')
''
>>> infow.after(1_000, infow.quit()); infow.mainloop()
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    infow.after(1_000, infow.quit()); infow.mainloop()
  File "C:\Users\hp\AppData\Local\Programs\Python\Python38\lib\tkinter\__init__.py", line 1420, in mainloop
    self.tk.mainloop(n)
KeyboardInterrupt

>>> infow.after(1_000, infow.quit); infow.mainloop()
'after#0'
>>> 
>>> var
1
>>> var = 2
>>> from tkinter import Variable
>>> var = Variable(value=0)
>>> pbar
<tkinter.ttk.Progressbar object .!progressbar>
>>> pbar['variable'] = variable
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    pbar['variable'] = variable
NameError: name 'variable' is not defined
>>> pbar['variable'] = var
>>> var+=1
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    var+=1
TypeError: unsupported operand type(s) for +=: 'Variable' and 'int'
>>> var.set(var.get() + 1)
>>> 
