Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import tkinter
>>> tkinter.Canvas
<class 'tkinter.Canvas'>
>>> tkinter.Canvas().create_text((10, 5), text=)
SyntaxError: invalid syntax
>>> root = tkinter.Tk()
>>> canvas = tkinter.Canvas()
>>> canvas.grid()
>>> canvas.create_text((10, 5), text="\n".join('Test'))
1
>>> canvas.create_text((10, 5), text="\n".join('Test'), anchor='nw')
2
>>> canvas.create_text((10, 5), text="\n".join('Test'), anchor='w')
3
>>> canvas.create_text((30, 5), text="\n".join('Test'), anchor='w')
4
>>> canvas.create_text(30, 5, text="\n".join('Test'), anchor='w')
5
>>> canvas.create_text(5, 5, text="\n".join('Test'), anchor='w', angle=90)
6
>>> canvas.create_text(50, 5, text="\n".join('Test'), anchor='w', angle=90)
7
>>> canvas.create_text(50, 20, text="\n".join('Test'), anchor='w', angle=90)
8
>>> canvas.create_text(50, 20, text="\n".join('Test'), anchor='w', angle=30)
9
>>> canvas.create_text(100, 20, text="\n".join('Test'), anchor='w', angle=30)
10
>>> canvas.create_text(300, 100, text="\n".join('Test'), anchor='w', angle=30)
11
>>> canvas.create_text(300, 100, text="(c) Copyright the student of M-131", anchor='w', angle=30)
12
>>> canvas.create_text(300, 100, text="(c) Copyright the student of M-131", anchor='w', angle=30 fontsize=10)
SyntaxError: invalid syntax
>>> canvas.create_text(300, 100, text="(c) Copyright the student of M-131", anchor='w', angle=30, fontsize=10)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    canvas.create_text(300, 100, text="(c) Copyright the student of M-131", anchor='w', angle=30, fontsize=10)
  File "C:\Users\hp\AppData\Local\Programs\Python\Python38\lib\tkinter\__init__.py", line 2805, in create_text
    return self._create('text', args, kw)
  File "C:\Users\hp\AppData\Local\Programs\Python\Python38\lib\tkinter\__init__.py", line 2771, in _create
    return self.tk.getint(self.tk.call(
_tkinter.TclError: unknown option "-fontsize"
>>> canvas.create_text(300, 100, text="(c) Copyright the student of M-131", anchor='w', angle=30, font=10)
14
>>> canvas.create_text(50, 200, text="(c) Copyright the student of M-131", anchor='w', angle=30, font=10, )
15
>>> canvas.create_text(50, 200, text="(c) Copyright the student of M-131 ", anchor='w', angle=30, font=10, )
16
>>> canvas.create_text(50, 200, text="(c) Copyright the student of M-131 ", anchor='w', angle=30, font=("Times New Roman", 10))
17
>>> canvas.create_text(50, 200, text="(c) Copyright the student of M-131 ", anchor='w', angle=30, font=("Times New Roman", 14))
18
>>> canvas.create_text(50, 250, text="(c) Copyright the student of M-131 ", anchor='w', angle=30, font=("Times New Roman", 14))
19
>>> 
canvas.create_text(50, 250, text="(c) Copyright the student of M-131 ", anchor='w', angle=30, font=("Times New Roman", 14))
20
>>> canvas.create_text(30, 250, text="(c) Copyright the student of M-131 ", anchor='w', angle=30, font=("Times New Roman", 14))
21
>>> canvas.create_text((10, 5), text="\n".join('Test'))
22
>>> 
