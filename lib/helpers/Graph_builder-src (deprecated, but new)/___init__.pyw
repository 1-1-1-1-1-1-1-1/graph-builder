"""__doc__"""

if __name__ == '__main__':
    t0 = __import__('time').time()

'''
Tasks:
1. Learn to see if the var is legal.
2. Is it great to show here the current configs of x_function etc. on the label? # Are there still such?
3. Imports — to realise them in a great form.
4. Reliase an option of cleaning the info, stored in data.json.
   Probably it should exist as a part of block of managing that file's content.

5. With the module ``f``:
    * Correct the code, especially parts with
        transforming [an appropriate] ``str`` to a function,
        definition of a function, wich provides a function to integrate
        and a part with curve's displaying on the screen.
    * Make the code simple and clear.

! 6. Which was a part of a project's tasks:
    * Add an option of saving a graph's picture to the file,
    * Add an option of displaying/hiding the axes. — As I see, it's done.
    Maybe:
      * Provide the graphic's building in the window.
'''


from f import ffs, CurveOnTheScreen
from f import wdd

import numpy, sympy # To let advanced functions in the output of "x" and "y".

import tkinter
X = 'x' # from tkinter import X

import tkinter.messagebox as mbox
import tkinter.simpledialog as dialog

import tkinter.filedialog as fd # Currently just ``asksaveasfilename`` is used here.

import json


c = __import__('configparser').ConfigParser()
DATA_FOLDER = 'data'
c.read(f'{DATA_FOLDER}\\configs.ini', encoding = 'utf-8')

# Should it be?
x_function, y_function, borders, kwargs = 't', 't', (1,2), {'linewidth': 3, 'color': 'red', 'times': 100}

def try_it(function):
	def wrapper(*args, **kwargs):
		try:
			return function(*args, **kwargs)
		except Exception as e: print(e)
	return wrapper

def iterate(obj):
	try:
		return {i: iterate(obj[i]) for i in obj.keys()}
	except:
		return obj

def get_kwargs(**temp_kws):
    return temp_kws

window = tkinter.Tk()
window.title('MLP (my little project)')
window.geometry('+40+180')

BASIC_MONOSPACED = ('Consolas', 10)

################################################### End of preperations. ##################################################
###########################################################################################################################
######################################################### Version 3. ######################################################

m1 = tkinter.LabelFrame(text = ' Main configs ')
m2 = tkinter.LabelFrame(text = ' Other ')

f1 = tkinter.Frame(m1)
f2 = tkinter.Frame(m1)
f3 = tkinter.Frame(m1)
graphic = tkinter.Frame(m1)
m_buttons = tkinter.Frame(m1)

label_x1 = tkinter.Label(f1, text = '      x =', font = BASIC_MONOSPACED)
label_x3 = tkinter.Label(f1, text = f'Cur. value: {x_function}') #? — Same to similar.
entry_x = tkinter.Entry(f1)
label_y1 = tkinter.Label(f2, text = '      y =', font = BASIC_MONOSPACED)
label_y3 = tkinter.Label(f2, text = f'Cur. value: {y_function}')
entry_y = tkinter.Entry(f2)
label_b1 = tkinter.Label(f3, text = 'borders =', font = BASIC_MONOSPACED)
label_b3 = tkinter.Label(f3, text = f'Cur. value: {borders}')
entry_b = tkinter.Entry(f3)

a_f = tkinter.Frame(m2)
a_buttons = tkinter.Frame(m2)

label_k1 = tkinter.Label(a_f, text = 'kws =')
label_k3 = tkinter.Label(a_f, text = f'Cur. value: {kwargs}')
entry_k = tkinter.Entry(a_f)


# This is used later (and currently is a bit out of code):
grid_var = tkinter.BooleanVar(a_buttons, c.getboolean('build', 'grid_it')) # The default value is defined here (in the configs), mind it.


@try_it
def get_cdata(): # No labels updates still. # CDATA - current data.
    global x_function, y_function, borders, kwargs
    if entry_x.get() != str():
        x_function = entry_x.get()
    if entry_y.get() != str():
        y_function = entry_y.get()
    if entry_b.get() != str():
        borders = eval(entry_b.get())
    if entry_k.get() != str():
        kwargs = eval(f'get_kwargs({entry_k.get()})')


from f import plt; from f import * #t, to delete

def action_v3(): # No labels updates still. # Undone currently!.
    """Beta (aimed for the (current data update) & graphics building)."""
    get_cdata()

    obj = CurveOnTheScreen(x_function, y_function, borders = borders)
    obj.display(grid_it = grid_var.get(), **kwargs)

    '''figc = __import__('matplotlib').backends.backend_tkagg.FigureCanvasTkAgg # To import
    
    # #? obj = CurveOnTheScreen(x_function, y_function, borders = borders)
    figure = plt.figure()
    what_is_it = figure.add_subplot(191)
    times = 50; bs = borders; space = numpy.linspace(bs[0], bs[1], times)
    x, y = map(lambda function: (sympy.lambdify(sympy.symbols('t'), function, 'numpy'))(space), (x_function, y_function))
    what_is_it.plot(x, y)
    why_is_it_needed = figc(figure, graphic)
    plsno = why_is_it_needed.get_tk_widget()
    plsno.pack()'''


    #t #? print(f'Displayed with x_function = {x_function}, y_function = {y_function}, borders = {borders}, kwargs = {kwargs}')

# MARK 2

action = action_v3


for i in [eval(f'entry_{o}') for o in ('x', 'y', 'b', 'k')]:
    i.bind('<Return>', lambda event: action())

# Packing.
m1.pack(ipadx = 4, pady = 10) # Which order of packing them is the best?
m2.pack(padx = 4, pady = 3)
f1.pack(); f2.pack(); f3.pack(); graphic.pack(ipadx = 10, ipady = 10); m_buttons.pack()
a_f.pack(); a_buttons.pack()

for o_left, o_right, o_middle in [eval(f'(label_{s}1, label_{s}3, entry_{s})') for s in ['x', 'y', 'b', 'k']]: # [(label_x1, label_x3, entry_x), (label_y1, label_y3, entry_y), (label_b1, label_x3, entry_x)]:
    o_left.pack(side = 'left'); # o_right.pack(side = 'right'); 
    o_middle.pack(side = 'right', fill = X, padx = 5)


# Width's configuration.
#?
f1.configure(width = 100)
m1.configure(width = 100)
m2['width'] = 100

entry_x.configure(width = 40); label_x3.configure(width = 42)
entry_y.configure(width = 40); label_y3.configure(width = 42)
entry_b.configure(width = 40); label_b3.configure(width = 42)
entry_k['width'] = 60; label_k3.configure(width = 30)

# Other.
def json_load(filename = f'{DATA_FOLDER}\\data.json'):
    """Load a json data from the file "filename"."""
    try:
        with open(filename, 'rt', encoding = 'utf-8') as f:
            text = f.read()
        assert text != str()
        data = json.loads(text)
    except AssertionError:
        data = dict()
    except Exception as e:
        raise e

    return data

def json_dump(data, *, filename = f'{DATA_FOLDER}\\data.json'):
    """Dump a json data to the "filename"."""
    with open(filename, 'wt', encoding = 'utf-8') as f:
        #t print(f'I am going to dump data {data}.')
        json.dump(data, f, ensure_ascii = False, indent = 4)


def load_configs(obj = 'Похожее на сердце'):
    """Helps to load the wanted from the data configs."""
    d = json_load()[obj]
    # MARK 3
    global x_function, y_function, borders, kwargs; # print('D:', d, 'obj:', obj);
    x_function, y_function, borders, kwargs = d['x'], d['y'], eval(d['b']), eval(d['k'])

    for i in [eval(f'entry_{o}') for o in ('x', 'y', 'k', 'b')]:
        i.delete(0, 'end')

    entry_x.insert(0, x_function)
    entry_y.insert(0, y_function)
    entry_b.insert(0, str(borders) )
    entry_k.insert(0, ', '.join([f'{key} = {kwargs[key]!r}' for key in kwargs])) # MARK 1

load_configs(c.get('build', 'default'))

def dump_configs(dict_object):
    """Update the graphics's configs with a ``dict_object``."""
    data = json_load()
    data.update(dict_object)
    json_dump(data)

def h_load():
    w_load = tkinter.Tk()
    data = json_load() # Is used twice: to set a geometry of ``w_load``, as a buttons' text.
    w_load.geometry('320x{}'.format(50 + 26*len(data)))
    w_load.title('Загрузка другого графика') # 'Загрузка других [настроек]')
    
    assert not 'var' in globals()
    var = tkinter.IntVar(w_load, 1)

    cb = tkinter.Checkbutton(w_load, text = 'Build the graph', variable = var)
    cb.pack(side = 'bottom', ipadx = 30, padx = 70, pady = 10)

    class Buttons:
        def pack_with(text):
            def temporary_cmd():
                load_configs(text); w_load.destroy()
                if var.get():
                    action()
            button = tkinter.Button(w_load, text = text, command = temporary_cmd)
            button.pack(fill = 'x')

    for j in data:
        Buttons.pack_with(j)
    
    w_load.mainloop()

load_b = tkinter.Button(m_buttons, text = 'Load', command = h_load)

build_b = tkinter.Button(m_buttons, text = 'Build', command = action)

def h_save():
    mbox.showerror('Warning', 'This part is currently undone.\nNothing will happen after chosing a filename here, if you do it just now.') # To delete finally
    name = fd.asksaveasfilename()
    pass

save_b = tkinter.Button(m_buttons, text = 'Save this graph to <...>', command = h_save)

def h_dump():
    get_cdata()
    names = json_load().keys()
    def ask_name(): return dialog.askstring('Ввод имени', 'Имя конструкции:')
    name = ask_name()
    while name in names or not name:
        if name == str(): # Case of an empty input.
            mbox.showerror('Error', "Name can't be empty.")
        elif name is None:
            return # End the function's active work in case of the click on "Cancel".
        elif mbox.askyesno('Error', 'This name already exists. Do you want to rewrite it?', default = 'no'):
            break
        name = ask_name()

    del names
    dump_configs({name: {'x': x_function, 'y': y_function, 'b': str(borders), 'k': str(kwargs)}})
    mbox.showinfo('Done', 'Записано в файл.')

dump_b = tkinter.Button(m_buttons, text = 'Сохранить настройки', command = h_dump)

@wdd
def h_additional_v0():
    text = __import__('matplotlib').pyplot.plot.__doc__.split('\n')
    text_test = [str(n) for n in range(1, 128)]
    # mbox.showinfo('<Заглавие>', '<Не дописано>')

    def pages(info = text):
        LINES_ON_PAGE = 42
        while info:
            yield '\n'.join(info[:LINES_ON_PAGE]); info = info[LINES_ON_PAGE:]

    pages = list(pages())
    w_info = tkinter.Tk()
    # w.info.geometry()
    global page_number
    page_number = 0
    info_label = tkinter.Label(w_info, text = pages[page_number]); info_label.pack()
    frame = tkinter.LabelFrame(w_info, text = ''); frame.pack(side = 'bottom')
    prev_page = tkinter.Button(frame, text = 'Prev. page')
    next_page = tkinter.Button(frame, text = 'Next page')
    # print('111111:', page_number)
    def h_next():
        global page_number
        # print('2222222:', page_number)
        if page_number != len(pages) - 1:
            page_number += 1; info_label['text'] = pages[page_number]
    def h_prev():
        global page_number
        if page_number != 0:
            page_number -= 1; info_label['text'] = pages[page_number]
    prev_page['command'] = h_prev; next_page['command'] = h_next
    next_page.pack(side = 'right'); prev_page.pack(side = 'right')
    w_info.mainloop()
    del page_

    for j in pages:
        mbox.showinfo("None", j)
    # for j in range(6):
        # mbox.showinfo('<Заглавие>', '\n'.join(text[48*j : 48*j + 49])) 

def h_additional():
    text = __import__('matplotlib').pyplot.plot.__doc__.split('\n')
    lens = list(map(len, text)); lens.sort(); _max = lens[-1]; del lens; # print(_max, '\n') # Once: 115.
    text = list(map(lambda line: line.ljust(_max), text)); del _max
    text = [(str(j+1) if j % 10 == 0 else str()).ljust(3 + 1) + text[j] for j in range(len(text))] # 3 — local.
    # text_test = [str(n) for n in range(1, 128)]

    LINES_ON_PAGE = 42
    global SCROLL_BY
    SCROLL_BY = 3

    def page(i = 0, *, info = text):
        _n = SCROLL_BY * i # Here the ``i`` value strictly shouldn't be negative. (*)
        return '\n'.join(info[_n : _n + LINES_ON_PAGE])

    # pages = list(pages())
    w_info = tkinter.Tk()
    w_info.title('Official documentation to the ``matplotlib.pyplot.plot()`` — a function, which is currently used here for building graphs')
    buttons = tkinter.LabelFrame(w_info)
    global i; i = 0
    info_label = tkinter.Label(w_info, text = page(0), font = ('Consolas', 10))
    info_label.pack()
    frame = tkinter.LabelFrame(w_info, text = '')
    frame.pack(side = 'bottom')
    next_page = tkinter.Button(frame, text = 'Scroll up')
    prev_page = tkinter.Button(frame, text = 'Scroll down')

    scroll_by_label = tkinter.Label(frame, text = 'Scroll by:')

    scroll_by_entry = tkinter.Entry(frame, width = 4)
    scroll_by_entry.insert(0, str(SCROLL_BY)) # Task: this can be done as a spinbox:
    # sc_by_n = tkinter.Spinbox(frame, from_ = 0, to = 100)

    def lhf(): # "Little help-function"
        global SCROLL_BY
        try:
            pre_SCROLL_BY = int(scroll_by_entry.get())
            # assert type(pre_SCROLL_BY) is int
            assert pre_SCROLL_BY > 0
            SCROLL_BY = pre_SCROLL_BY
        except Exception as e:
            mbox.showerror('Error', str(e))

    # scroll_by_entry.bind('<Return>', lambda event: lhf()) # What is an ``event`` actually?

    def h_next():
        lhf()
        global i
        if SCROLL_BY * (i + 10) < len(text): # What is better to be here, where a 10 states now?
            i += 1; info_label['text'] = page(i = i)
    def h_prev():
        lhf()
        global i
        if i > 0: # Providing of (*)
            i -= 1; info_label['text'] = page(i = i)
    prev_page['command'] = h_prev; next_page['command'] = h_next

    scroll_by_label.pack(side = 'left')
    scroll_by_entry.pack(side = 'left', pady = 10)
    next_page.pack(side = 'right'); prev_page.pack(side = 'right')

    w_info.mainloop()

    try: del SCROLL_BY
    except: None

    try: del i
    except: None

    return

    # for j in pages: mbox.showinfo("None", j)
    # for j in range(6):
        # mbox.showinfo('<Заглавие>', '\n'.join(text[48*j : 48*j + 49])) 


WORDS_LH = """
*             Kind of "about" and a "help message" here.              *

  This program is a project, which is written 1-ly as a course work
for the student of group M-121 of Karazin N.U. (H.M., course 2).
"All rights reserved..." (joke, currently no license is provided here).

  Read the about part to view some info about this program. View the
official doc. (below) to get an info about the library, which is used
here for building 2-D parametrical curves.
———————————————————————————————————————————————————————————————————————
To draw a graph of y = f(x), a such action could be done: enter `t` at
a place of x and `f(t)` at a place of y.
"""
WORDS_LH = WORDS_LH.split('\n'); _max = max(map(len, WORDS_LH)); WORDS_LH = '\n'.join(line.ljust(_max) for line in WORDS_LH)


def h_help():
    help_w = tkinter.Tk()
    help_w.title('Some words, little help for the program')

    def h_about():
        about_text = "This program is aimed for building 2-dimensional parametric curves."
        mbox.showinfo('About the program', about_text, parent = help_w)

    words_lh = tkinter.LabelFrame(help_w, text = ' Some words about ')
    label_help = tkinter.Label(words_lh, text = WORDS_LH, font = ('Consolas', 12))
    hwf = tkinter.Frame(help_w)
    additional_b = tkinter.Button(hwf, text = 'Official doc. for some graphics buildings\' module', command = h_additional)
    
    about = tkinter.Button(hwf, text = 'About', command = h_about)
    local_exit = tkinter.Button(hwf, text = 'Close this window', command = help_w.destroy)

    words_lh.pack(pady = 3, expand = 1, padx = 10)
    hwf.pack(side = 'bottom')
    label_help.pack()
    local_exit.pack(side = 'left')
    additional_b.pack(side = 'left')
    about.pack(side = 'left')

    help_w.mainloop()

help_b = tkinter.Button(a_buttons, text = 'Help', command = h_help)

# It could be named as an "exit", but I am not sure that it doesn't conflict with the build-in function.
exit_b = tkinter.Button(a_buttons, text = 'Close the program', command = window.destroy)

# Still a test:
grid_it = tkinter.Checkbutton(a_buttons, text = 'Grid the plot', variable = grid_var)


load_b.pack(side = 'left')
build_b.pack(side = 'left')
save_b.pack(side = 'left')
dump_b.pack(side = 'left')

grid_it.pack(side = 'left', padx = 3)
help_b.pack(side = 'left')
exit_b.pack(side = 'left')


if __name__ == '__main__':
    if c.getboolean('build', 'build on loading'):
        action()
    mbox.showinfo('Info', 'Launched in {:.2} seconds.'.format(__import__('time').time() - t0)); del t0
    window.mainloop()

# Notes ####################################################################################
# See "comments.txt" for it.