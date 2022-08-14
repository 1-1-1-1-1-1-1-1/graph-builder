Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def test():
	from numpy import linspace
	from tkinter import colorchooser asa tc
	
SyntaxError: invalid syntax
>>> def test():
	from numpy import linspace
	from tkinter import colorchooser as tc

	
>>> def test():
	from numpy import linspace
	# from tkinter import colorchooser as tc
	import matplotlib.pyplot as plt

	space = [0, 256, len(ys)]
	def color(i):
		return '#{0}{0}{0}'.format(space[i])
	for i in (total_len := len(ys)):
		plt.plot(ys[i], color=color(i))
	plt.show()

	
>>> test()
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    test()
  File "<pyshell#9>", line 6, in test
    space = [0, 256, len(ys)]
NameError: name 'ys' is not defined
>>> def test():
	from numpy import linspace
	# from tkinter import colorchooser as tc
	import matplotlib.pyplot as plt

	ys = [[1, 2, 3, 4, 5, 6, 7],
	      [1, 2, 3, 4, 5, 7, 6],
	      [3, 2, 1, 5, 4, 7, 6]]
	space = [0, 256, len(ys)]
	def color(i):
		return '#{0}{0}{0}'.format(space[i])
	for i in (total_len := len(ys)):
		plt.plot(ys[i], color=color(i))
	plt.show()

	
>>> test()
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    test()
  File "<pyshell#12>", line 12, in test
    for i in (total_len := len(ys)):
TypeError: 'int' object is not iterable
>>> def test():
	from numpy import linspace
	# from tkinter import colorchooser as tc
	import matplotlib.pyplot as plt

	ys = [[1, 2, 3, 4, 5, 6, 7],
	      [1, 2, 3, 4, 5, 7, 6],
	      [3, 2, 1, 5, 4, 7, 6]]
	space = [0, 256, len(ys)]
	def color(i):
		return '#{0}{0}{0}'.format(space[i])
	for i in range((total_len := len(ys))):
		plt.plot(ys[i], color=color(i))
	plt.show()

	
>>> test()

>>> def test():
	from numpy import linspace
	# from tkinter import colorchooser as tc
	import matplotlib.pyplot as plt

	ys = [[1, 2, 3, 4, 5, 6, 7],
	      [1, 2, 3, 4, 5, 7, 6],
	      [3, 2, 1, 5, 4, 7, 6]]
	space = [0, 256, len(ys)]
	def color(i):
		return '#{0}{0}{0}'.format(hex(int(space[i]))[2:].rjust('0'))
	for i in range((total_len := len(ys))):
		plt.plot(ys[i], color=color(i))
	plt.show()

	
>>> test()
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    test()
  File "<pyshell#18>", line 13, in test
    plt.plot(ys[i], color=color(i))
  File "<pyshell#18>", line 11, in color
    return '#{0}{0}{0}'.format(hex(int(space[i]))[2:].rjust('0'))
TypeError: 'str' object cannot be interpreted as an integer
>>> def test():
	from numpy import linspace
	# from tkinter import colorchooser as tc
	import matplotlib.pyplot as plt

	ys = [[1, 2, 3, 4, 5, 6, 7],
	      [1, 2, 3, 4, 5, 7, 6],
	      [3, 2, 1, 5, 4, 7, 6]]
	space = linspace(0, 256, len(ys))
	def color(i):
		return '#{0}{0}{0}'.format(hex(int(space[i]))[2:].rjust('0'))
	for i in range((total_len := len(ys))):
		plt.plot(ys[i], color=color(i))
	plt.show()

	
>>> test()
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    test()
  File "<pyshell#21>", line 13, in test
    plt.plot(ys[i], color=color(i))
  File "<pyshell#21>", line 11, in color
    return '#{0}{0}{0}'.format(hex(int(space[i]))[2:].rjust('0'))
TypeError: 'str' object cannot be interpreted as an integer
>>> hex(3)
'0x3'
>>> hex(3)[2:]
'3'
>>> hex(3)[2:].ljust()
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    hex(3)[2:].ljust()
TypeError: ljust expected at least 1 argument, got 0
>>> hex(3)[2:].ljust('0')
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    hex(3)[2:].ljust('0')
TypeError: 'str' object cannot be interpreted as an integer
>>> hex(3)[2:].ljust(0)
'3'
>>> hex(3)[2:].ljust(2)
'3 '
>>> hex(3)[2:].ljust(2, 0)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    hex(3)[2:].ljust(2, 0)
TypeError: The fill character must be a unicode character, not int
>>> def test():
	from numpy import linspace
	# from tkinter import colorchooser as tc
	import matplotlib.pyplot as plt

	ys = [[1, 2, 3, 4, 5, 6, 7],
	      [1, 2, 3, 4, 5, 7, 6],
	      [3, 2, 1, 5, 4, 7, 6]]
	space = linspace(0, 256, len(ys))
	def color(i):
		return '#{0}{0}{0}'.format(hex(int(space[i]))[2:].rjust(2, fillchar='0'))
	for i in range((total_len := len(ys))):
		plt.plot(ys[i], color=color(i))
	plt.show()

	
>>> hex(3)[2:].ljust(2, fillchar='0')
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    hex(3)[2:].ljust(2, fillchar='0')
TypeError: ljust() takes no keyword arguments
>>> hex(3)[2:].ljust(2, '0')
'30'
>>> hex(3)[2:].ljust(2, '0df')
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    hex(3)[2:].ljust(2, '0df')
TypeError: The fill character must be exactly one character long
>>> def test():
	from numpy import linspace
	# from tkinter import colorchooser as tc
	import matplotlib.pyplot as plt

	ys = [[1, 2, 3, 4, 5, 6, 7],
	      [1, 2, 3, 4, 5, 7, 6],
	      [3, 2, 1, 5, 4, 7, 6]]
	space = linspace(0, 256, len(ys))
	def color(i):
		return '#{0}{0}{0}'.format(hex(int(space[i]))[2:].rjust(2, '0'))
	for i in range((total_len := len(ys))):
		plt.plot(ys[i], color=color(i))
	plt.show()

	
>>> test()

>>> def test():
	from numpy import linspace
	# from tkinter import colorchooser as tc
	import matplotlib.pyplot as plt

	ys = [[1, 2, 3, 4, 5, 6, 7],
	      [1, 2, 3, 4, 5, 7, 6],
	      [3, 2, 1, 5, 4, 7, 6]]
	space = linspace(0, 256, len(ys))
	def color(i):
		return '#{0}{0}{0}'.format(hex(int(space[i]))[2:].rjust(1, '0'))
	for i in range((total_len := len(ys))):
		plt.plot(ys[i], color=color(i))
	plt.show()

	
>>> test()

>>> def test():
	from numpy import linspace
	# from tkinter import colorchooser as tc
	import matplotlib.pyplot as plt

	ys = [[1, 2, 3, 4, 5, 6, 7],
	      [1, 2, 3, 4, 5, 7, 6],
	      [3, 2, 1, 5, 4, 7, 6]]
	space = linspace(0, 256, len(ys))
	def color(i):
		return '#{0}{0}{0}'.format(hex(int(space[i]))[2:].rjust(1, '0'))
	for i in range((total_len := len(ys))):
		print(color(i))
		plt.plot(ys[i], color=color(i))
	plt.show()

	
>>> test()
#000
#808080
#100100100

>>> def test():
	from numpy import linspace
	# from tkinter import colorchooser as tc
	import matplotlib.pyplot as plt

	ys = [[1, 2, 3, 4, 5, 6, 7],
	      [1, 2, 3, 4, 5, 7, 6],
	      [3, 2, 1, 5, 4, 7, 6]]
	space = linspace(0, 256, len(ys))
	def color(i):
		return '#{0}{0}{0}'.format(hex(int(space[i]))[2:].ljust(2, '0'))
	for i in range((total_len := len(ys))):
		print(color(i))
		plt.plot(ys[i], color=color(i))
	plt.show()

	
>>> test()
#000000
#808080
#100100100

>>> hex(int(10))[2:].ljust(2, '0')
'a0'
>>> hex(int(3))[2:].ljust(2, '0')
'30'
>>> hex(int(3))[2:].rjust(2, '0')
'03'
>>> hex(int(10))[2:].rjust(2, '0')
'0a'
>>> hex(int(16))[2:].rjust(2, '0')
'10'
>>> hex(int(255))[2:].rjust(2, '0')
'ff'
>>> def test():
	from numpy import linspace
	# from tkinter import colorchooser as tc
	import matplotlib.pyplot as plt

	ys = [[1, 2, 3, 4, 5, 6, 7],
	      [1, 2, 3, 4, 5, 7, 6],
	      [3, 2, 1, 5, 4, 7, 6]]
	space = linspace(0, 255, len(ys))
	def color(i):
		return '#{0}{0}{0}'.format(hex(int(space[i]))[2:].ljust(2, '0'))
	for i in range((total_len := len(ys))):
		print(color(i))
		plt.plot(ys[i], color=color(i))
	plt.show()

	
>>> test()
#000000
#7f7f7f
#ffffff
>>> 
