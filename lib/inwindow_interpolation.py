# [dev.] Some comments
# ====================
# 
# Possible for the `func`:
# ------------------------
#
#   weierstrass_function(3, 1/2, maxn='default', borders=[-2, 3])(x)
#   cos(x)+x*(-1+x+2*sin(x))  # Ilia
# 
# [dev.] Tasks
# ============
#
# * [REQUIRED] What is the best order (and way) of packing such objects? I.e. the label,
#      frame, etc.
# * [optional] Add an option to make `undo`. Possibly, make this {via /
#   and with a help of} logging all history of entry's, such as
#   entering of function, enterting of borders, and choosing the alpha.
# * Do the help message.


''' Scheme and scratch {for / of} the window:
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    
  |=== Header ==============================|
  |_________________________________________|
  |=========================================|
  |——— Function ————————————————————————————|
  | function (and var.) + xborders          |
  |—————————————————————————————————————————|
  |——— Interpolation ———————————————————————|
  | interp_by [...]                         |
  | nodes' number: `<int>`                  |
  | form_args (:str) ?+ nodes_n             |
  |—————————————————————————————————————————|
  |——— Build ———————————————————————————————|
  | build_params (as `(k=v[, <etc.>]*)?`)   |
  | build_option [...]                      |
  |       <! Button: BUILD >                |
  |=========================================|
  |——— Extra ———————————————————————————————|
? | extra_info, test_points, alpha          |
  |      <! Button: PRINT TABLE >           |
  |=========================================|
  |———— Additional —————————————————————————|
  | ?<action/console>                       |
  | <general configurations>                |
  | <!w.configuration>        FAQ <help>    |
  |      [{BUTTON: OPEN <CONFIG FILE>}]     |
  |—————————————————————————————————————————|
  |=========================================|
'''


from time import time
from tempfile import NamedTemporaryFile
from tkinter import (Tk, PanedWindow, LabelFrame, Label, Frame,
    Entry, Button, Text, Scrollbar, Scale, Checkbutton, IntVar, BooleanVar,
                     ttk)
from tkinter.constants import *  # Test
import tkinter.messagebox as mbox
from tkinter.filedialog import asksaveasfilename, askdirectory
from os import mkdir, listdir, sep as os_sep, altsep, remove
from os.path import join, splitext, split
from pathlib import Path
from datetime import datetime  # logging

from sympy import *  # Functions: sin, cos etc.
import configparser

from .interpolate import *
from .interpolate import test as _build
from .addings import weierstrass_function
from .tests.tests import whole_test as _print_table
from .config import INIT_FUNCTION, PACKAGE
from ._typing import Optional, NoReturn
from ._helpers import *
from ._helpers import c


__COPYRIGHT = "Copyright (c) The Student Mykola Heneralov, y. 2020–2022"


# Function
DEFAULT_FUNCTIONS = eval(
    c['function_defaults']['displayable'].replace("\n", ""))


DEFAULT_FUNCTION = get_default(c['function_defaults'], DEFAULT_FUNCTIONS)
DEFAULT_BORDERS = eval(c['function_defaults']['borders'])

# Interpolator
section = c['interpolation_defaults']
ALL_INTERPOLATORS = eval(section['available'].replace("\n", ""))
DEFAULT_INTERPOLATOR = get_default(section, ALL_INTERPOLATORS)
DEFAULT_NODES = int(section['nodes'])
FORM_ARGS_DEFAULT = section['form_args_as']

# Graph's building
BUILD_OPTIONS = ['both', 'func', 'interpolant']
BUILD_OPTION_DEFAULT = get_default(c['graph'], BUILD_OPTIONS,
    option='build_option_default')
GRAPH_MODES_POSSIBLE = ["Don't save", "Save always", "Ask"]
GRAPH_MODE_DEFAULT = c.get('graph', 'save_graph_mode')
BUILD_SAVE_NAME_DEFAULT = c.get('graph', 'build_save_name_default')
# Q: Best build paramaters.

# Table's printing
DEFAULT_ALPHA = eval(c['print_table']['alpha'])

# Other
section = c['general']
DEFAULT_IS_TOPMOST = eval(section['is_topmost_default'])
DEFAULT_TIMING_INFORM = eval(section['timing_inform_default'])

LOGGING_ENABLED = eval(section['logging_enabled'])
LOGGING_FILE = section['logging_file']

TMP_CONFIGS = section['tmp_configs']

KEY_BINDINGS_FILE = Path(PACKAGE) / section['key_bindings']

assert GRAPH_MODE_DEFAULT in GRAPH_MODES_POSSIBLE

assert len(ALL_INTERPOLATORS) == len(set(ALL_INTERPOLATORS))
assert len(DEFAULT_FUNCTIONS) == len(set(DEFAULT_FUNCTIONS))

del get_default, section; c.clear()


# current_approximation = ...  # Q.


def log_info(info, *, file=LOGGING_FILE):
    if not LOGGING_ENABLED:
        return
    # Ensuring the file exists:
    with open(file, 'a') as f:
        del f

    info += '\n'

    def ctime():
        return datetime.now().strftime('[%d.%m.%Y %H:%M:%S]')

    add_eol = False
    with open(file, encoding='utf-8') as f:
        if (data := f.readlines()) and data[-1][-1] != '\n':
            add_eol = True
        del data
    with open(file, 'a', encoding='utf-8') as f:
        if add_eol:
            f.write('\n')
        f.write(ctime() + ' ' + info)


def upper_first(string: str) -> str:
    """Return capitalized first letter (do not change the string).
    Example: "some TexT: words" -> "Some TexT: words".
    """
    return string[:1].capitalize() + string[1:]


def error_log(title: str, info: str) -> NoReturn:  #~
    log_info(title + info)
    mbox.showerror("Error", upper_first(info))


def key_bindings() -> dict[str, str]:
    # :result: In a form `"<binding>": "<...>"`
    import json

    with open(KEY_BINDINGS_FILE, encoding='utf-8') as f:
        return json.load(f)


WINDOW_KEY_BINDINGS = key_bindings()['window'].items()


def build():
    try:
        func = lambda x: eval(entry1.get())
    except Exception as e:
        if any(type(e) is t for t in (NameError, SyntaxError)):
            part = "error: "
        else:
            part = "unexpected error: "
        info = part + str(e)
        error_log("While building graph: ", info)
        return

    try:
        by_func = eval(interp_choose.get())
        xborders = eval(borders_entry.get())
        nodes_n = int(nodesn_entry.get())
        if by_func is newton_polynomial_forward_equidistant:
            form_args = repr((*xborders, nodes_n))
        else:
            form_args = form_args_entry.get()
        build_params = eval('dict(' + build_params_entry.get() + ')' )
        _uwith = {'borders': 1, 'times': 100}  # To make better.
        for k in _uwith:
            build_params.setdefault(k, _uwith[k])
        build_option = build_option_choose.get()
    except Exception as e:
        info = "error: " + str(e)
        error_log("While building graph: ", info)
        return

    log_info(f"""Building the graph with following parameters:
 * function: {func}
 * Defined on {xborders}
 * Using `{by_func}` for interpolating
 * Forming args as `{form_args}`
 * Build parameters: {build_params}
 * Building the graph {'of function and its interpolant' if
build_option == 'both' else 'of ' + ('interpolant' if build_option ==
'interpolant' else 'function') + ' only'}
 * Nodes' number: {nodes_n}.""")

    try:
        t0 = time()
        fig = _build(func, xborders=xborders,
                     approx_by=by_func, form_args=form_args,
                     test_in_points=None,
                     build=True, build_params=build_params,
                     build_option=build_option,
                     nodes_n=nodes_n, block=False)
        info = f"The graph was built in {time() - t0:.2f} seconds."
        log_info(info)
        if timing_inform.get():
            mbox.showinfo("Timing", info)

        if (save_graph_var := save_graph_choose.get()) == "Save always":
            save_graph_var = True, '.png'  # Q.
        elif save_graph_var == "Don't save":
            save_graph_var = False
        elif save_graph_var == "Ask":
            save_graph_var = None, '.png'
        else:
            raise Exception("~ Undefined type of `save_grapg_var`.")

        if save_graph_var:
            # Q.: best.

            path, ext = save_graph_optpath.get(), save_graph_var[1]
            head, tail = split(path)
            head = head.strip(os_sep + altsep)  # Q.
            head = "." if not head else head

            try:
                mkdir(head)
            except:
                pass

            names = filter(lambda name: name.startswith(tail),
                           listdir(head))
            names = [splitext(name) for name in names]
            
            high_index = -1
            for name in names:
                try:
                    n = int(name[0].split(tail, maxsplit=1)[1])
                    high_index = n
                except:
                    pass

            fname = tail + str(high_index + 1) + ext

            if save_graph_var[0] is True:
                _name = join(head, fname)
            if save_graph_var[0] is None:
                _name = asksaveasfilename(initialdir=head, initialfile=fname)

            if _name:
                fig.savefig(_name)
    except Exception as e:
        info = "error: " + str(e)
        error_log("While building graph: ", info)


def print_table():
    try:
        func = entry1.get()
        borders = eval(borders_entry.get())
        by_func = interp_choose.get()
        n = int(nodesn_entry.get())
        alpha = None if alpha_is_random.get() else float(alpha_choose.get())
    except Exception as e:
        error_log("While building table: ", "error: " + str(e))
        return

    log_info(f"""Building the table with following parameters:
 * Function: {func}
 * Defined on {borders}
 * Using `{by_func}` for interpolating
 * Nodes' number: {n}.
 * Alpha: {alpha}.""")
    if eval(by_func) is newton_polynomial_forward_equidistant:
        mbox.showerror("Error", "Can't build the table for \
`newton_polynomial_forward_equidistant`. \
Try to use `newton_polynomial_forward` instead.")
        return

    from io import StringIO
    import sys

    class OutputInterceptor(list):
        def __enter__(self):
            self._stdout = sys.stdout
            sys.stdout = self._stringio = StringIO()
            return self

        def __exit__(self, *args):
            self.extend(self._stringio.getvalue().splitlines())
            del self._stringio
            sys.stdout = self._stdout

    import threading
    import configparser  # ... . For tracking the table's building process.

    c = configparser.ConfigParser()
    _id = section = str(__import__("random").randint(1, int(1e10)))

    action = lambda: _print_table(borders=borders, n=n, alpha=alpha,
        func=func, tested=[by_func], _id=_id)

    def no_section_action():
        error_m = "Error: section {} wasn't found.".format(_id)
        log_info(error_m)
        mbox.showerror("Error", error_m)

    with OutputInterceptor() as output, \
         open(TMP_CONFIGS, "w", encoding='utf-8') as f:
        infow = Tk()
        infow.title("Building information")
        infow.wm_attributes('-topmost', 1)
        infow.wm_attributes('-toolwindow', True)

        label = Label(infow, text="Processing...", font=14, width=30)
        label.pack(fill='x')

        c.read(TMP_CONFIGS, encoding='utf-8')
        if not c.has_section(section):
            c.add_section(section)
        c.set(section, 'done', '0')
        c.write(f)

        interrupted = False
        finished = False
        
        def interrupt():
            nonlocal interrupted
            interrupted = True
            c[section]['interrupted'] = 'yes'
            c.write(f)
        
        def track_interrupted():
            if interrupted:
                infow.quit()
                return
            if finished:
                return
            window.after(100, track_interrupted)
    
        def update_var():
            if finished:
                return
            c.read(TMP_CONFIGS)
            sections = c.sections()
            if not section in sections:
                no_section_action()
                return
            else:
                parts_done = c.getint(section, 'done')
                var_result = 1 + 2*parts_done
                pbar.config(value=var_result)
                if parts_done == 4:
                    return
            window.after(100, update_var)

        # How do `variable` in Progressbar works?
        # It should be a `Variable` or `IntVar` object, maybe!
        # Does it work here?
        pbar = ttk.Progressbar(infow, maximum=9, value=0,  # variable=var
                               )
        pbar.pack()

        cancel = Button(infow, text="Cancel", font=14, command=interrupt)
        cancel.pack(fill='x')

        def threading_target():
            action()
            if not interrupted:
                infow.after(1_000, infow.quit)
        
        thread = threading.Thread(target=threading_target, daemon=True)
        if not (c.has_section(_id) and c[_id]['done'] == '0'):
            no_section_action()
            return
        t0 = time()
        update_var()
        thread.start()
        track_interrupted()
        infow.mainloop()

        finished = True
        if not interrupted:
            info = f"The table was built in {time() - t0:.2f} seconds."
            log_info(info)
        else:
            log_info("Build of the table was interrupted.")

        try:
            infow.destroy()
        except Exception as e:
            pass
        finally:
            c.read(TMP_CONFIGS)
            for s in c.sections():
                c.remove_section(s)            
            c.write(f)

        if interrupted:
            return

    __import__("time").sleep(1);remove(TMP_CONFIGS); print("Yes!")
    
    # Copied from https://younglinux.info/tkinter/text.php:
    root = Tk()
     
    text = Text(root, width=100, height=70, font='Consolas')
    text.insert(1.0, '\n'.join(output + [""]*2))
    text.pack(side='left')
     
    scroll = Scrollbar(root, command=text.yview)
    scroll.pack(side='left', fill='y')
     
    text.config(yscrollcommand=scroll.set)

    if timing_inform.get():
        mbox.showinfo("Timing", info, parent=root)
    root.mainloop()


def help_message():
    __k_bindings = {}
    for key, value in WINDOW_KEY_BINDINGS:
        if value in __k_bindings:
            continue
        _iter = (item[0] for item in WINDOW_KEY_BINDINGS if item[1] == value)
        __k_bindings.update({value: ', '.join(_iter)})
    _k_bindings = {value: key for key, value in \
        __k_bindings.items()}
    for key, value in _k_bindings.items():
        if value == "build()":
            _k_bindings[key] = 'build the graph'
        elif value == "print_table()":
            _k_bindings[key] = 'print table'
        elif value == "help_message()":
            _k_bindings[key] = 'help message (this)'
    k_bindings = (key + ' — ' + value for key, value in _k_bindings.items())
    s = ['◦', '•', '●'][0]
    words = """\
Here is a brief description in general about this the window.

 {s} "form args"' common help-functions: `chebyshev_nodes`, `linspace`. 
 {s} Function: in a form "function(x)".
 {s} Borders: it's defined borders, the \
interpolation may be based on their value.
 {s} Build parameters: of the form \
"key_1=value_1, key_2=value_2" etc. (May be empty.)

Initial function for the field `function`: {}

Key bindings:
{}
""".format(INIT_FUNCTION, '\n'.join(k_bindings), s=s)
    mbox.showinfo("<?Info>", words)
    '''
'<Control-b>' — build the graph
'<Control-p>' — print table
'<Control-h>', '<F1>' — help message (this)
'''


def react_interpolator_choose():
    interpolator = eval(interp_choose.get())
    if interpolator is newton_polynomial_forward_equidistant:
        form_args_entry.config(state="disabled")
    else:
        form_args_entry.config(state="normal")


window = Tk()
window.title(f"Local helper ({__COPYRIGHT})")

# Tests: config
# window.geometry('300x250')
window.minsize(600, 0)
#

pw = PanedWindow(window, sashwidth=3, sashrelief=SUNKEN, orient=VERTICAL, width=316)
pw.pack(fill="both", expand="yes")

# Function configuration:
lframe1 = LabelFrame(pw, text=' Function configs ', borderwidth=2, relief=SUNKEN, height=54)
pw.add(lframe1)

fframe1 = Frame(lframe1)
fframe2 = Frame(lframe1)
fframe1.pack(side='top', fill='x'); fframe2.pack(side='top', fill='x')

label1 = Label(fframe1, text='function:')
label1.pack(side='left')
# entry1 = Entry(fframe1, width=33)
# entry1.pack(side='left')
entry1 = ttk.Combobox(fframe1, values=DEFAULT_FUNCTIONS, state='normal',
    width=40)
entry1.pack(side='left')
if DEFAULT_FUNCTION is not None:
    entry1.set(DEFAULT_FUNCTION)

label_2 = Label(fframe2, text='borders:')
label_2.pack(side='left')
borders_entry = Entry(fframe2)
borders_entry.pack(side='left')

# Interpolation configuration:
lframe2 = LabelFrame(pw, text=" Interpolation's configuration ", borderwidth=2, relief=SUNKEN, height=54)
pw.add(lframe2)

frame21 = Frame(lframe2)
frame22 = Frame(lframe2)
frame23 = Frame(lframe2)
for local_f__ in [frame21, frame22, frame23]:
    local_f__.pack(side='top', fill='x');

label_interp = Label(frame21, text='Interpolate with')
label_interp.pack(side='left')
interp_choose = ttk.Combobox(frame21, values=ALL_INTERPOLATORS, state="readonly",
    width=40)
interp_choose.bind("<<ComboboxSelected>>", lambda _: react_interpolator_choose())
interp_choose.pack(side='left')
if DEFAULT_INTERPOLATOR is not None:
    interp_choose.set(DEFAULT_INTERPOLATOR)

label_nodesn = Label(frame22, text="Nodes' number:")
label_nodesn.pack(side='left')
nodesn_entry = Entry(frame22)  # Q.
nodesn_entry.pack(side='left')

form_args_lbl = Label(frame23, text='Form arg-s as')
form_args_lbl.pack(side='left')
form_args_entry = Entry(frame23, width=52)
form_args_entry.pack(side='left')
form_args_entry.insert(0, FORM_ARGS_DEFAULT)


copyr = Label(pw, text=__COPYRIGHT,  # | WAS WRITTEN NOT BY ME",
                   # borderwidth=2, relief=SUNKEN, height=4,
                   relief='flat', state='disabled', height=1,  #! <- tests
                   font=("Times New Roman", 14, "bold"))

# pw.add(copyr)
'''
def func():
    copyr.config(height=10)


# func()  # <- test

from time import sleep
import threading


def func_():
    func()
    sleep(1)
    func_()


def _align():
    # print(max(copyr['height'], 2))
    
    def next_height():
        current = copyr['height']
        return max(2, current)
    
    copyr.config(height=next_height())
    print(next_height())
    # copyr.config(height=max(copyr['height'], 2)*2)
    # copyr['height'] = 2
    # mbox.showinfo('"Alinged."')
    # copyr.after(10_000, _align)
    
    def show():
        def _pre():
            yield exec("_align()", globals())
        
        list(_pre())
        print('Test')
    
    copyr.after(1_000, show)
    # copyr.after(1_000, (exec("_align()", globals()) )
    # copyr.after(1_000, lambda: print(1))
    # copyr.after_idle(exec("_align()", globals()))

# _align()
# (_align := lambda: (copyr.config(height=10), copyr.after(1_000, _align)))()  # Test
'''
# copyr.after(10_000, func_)  # Or `after`, or `after_idle`?
# threading.Thread(target=func_, daemon=True).start()
# button_test = Button(pw, text='', command=func)
# pw.add(button_test)

#? get_scale_move_value = lambda pos: lblRez.configure(text=pos)
#? alpha_choose['command'] = get_scale_move_value
# getScaleValue = lambda: lblRez.configure(text=scl.get())
# btnCopyScale=Button(lfScale, bitmap="info",command=getScaleValue)

# Building graph:
graph_lframe = LabelFrame(pw, text=" Graph's building configurations ",
    borderwidth=2, relief=SUNKEN, height=54)
pw.add(graph_lframe)

frame31 = Frame(graph_lframe)
frame32 = Frame(graph_lframe)
frame33 = Frame(graph_lframe)
for f__ in [frame31, frame32, frame33]:
    f__.pack(fill='x')

buildoption_label = Label(frame31, text='build option:')
buildoption_label.pack(side='left')
build_option_choose = ttk.Combobox(frame31, values=BUILD_OPTIONS,
    state="readonly", width=40)
build_option_choose.pack(side='left')
if type(BUILD_OPTION_DEFAULT) is not None:
    build_option_choose.set(BUILD_OPTION_DEFAULT)

build_params_label = Label(frame32, text='build parameters:')
build_params_label.pack(side='left')
build_params_entry = Entry(frame32, width=70)
build_params_entry.pack(side='left')
build_params_entry.insert(0, "")

save_graph_choose_label = Label(frame33, text="Graph's saving type:")
save_graph_choose_label.pack(side='left')


def save_graph_cnf() -> NoReturn:
    if save_graph_choose.get() == "Save always":
        save_graph_optpath.configure(state='disabled')
    else:
        save_graph_optpath.configure(state='normal')


save_graph_choose = ttk.Combobox(frame33, values=GRAPH_MODES_POSSIBLE,
    state="readonly", width=40)
save_graph_choose.set(GRAPH_MODE_DEFAULT)
save_graph_choose.bind("<<ComboboxSelected>>", lambda _: save_graph_cnf())
save_graph_choose.pack(side='left')


def help_message_save_g() -> NoReturn:
    mbox.showinfo("On save's modes", """\
Here are several words about the mode to handle the graph's saving.

 ◦ Save always — always save the graph. The graph's name is formed from the \
entry beside as `that`+`number`+`extension` ('.png'?). Example: if in the \
entry is "builds/build_" and last stored there number of such files in folder \
"builds/" is 3 (even if lower numbers don't exist), then the next \
picture will be saved to folder "builds" with name "build_4.png".
 ◦ Don't save — never save the graph.
 ◦ Ask — ask, whether to save the graph. File's name is asked each time. And
the default name is formed in the same way as in "save always".

Enjoy your Program!

{0}
""".format(__COPYRIGHT)[:-1])


save_graph_info = Button(frame33, bitmap="info", command=help_message_save_g, width=20)
save_graph_info.pack(side='left')
save_graph_optpath = Entry(frame33)
save_graph_optpath.insert(0, BUILD_SAVE_NAME_DEFAULT)


def graph_save_helper() -> NoReturn:
    name = askdirectory()
    if name:
        save_graph_optpath.delete(0, 'end')
        sep = os_sep if os_sep in name else altsep
        save_graph_optpath.insert(0, name + sep + 'build_')


save_graph_path_choose = Button(frame33, text="View",
    command=graph_save_helper)
save_graph_path_choose.pack(side='right')
save_graph_optpath.pack(side='right')

build_button = Button(graph_lframe, text='Build', command=build)
build_button.pack()

# Table's printing
table_print = LabelFrame(pw, text=" Table's building configurations ",
    borderwidth=2, relief=SUNKEN, height=54)
pw.add(table_print)

alpha_group = Frame(table_print)
alpha_group.pack()

alpha_is_random = IntVar(value=1 if DEFAULT_ALPHA is None else 0)


def config_alpha_choose() -> NoReturn:  #?
    state = 'disabled' if alpha_is_random.get() else 'normal'
    alpha_choose.configure(state=state)


alpha_random = Checkbutton(alpha_group, text="alpha is random   ",
    variable=alpha_is_random, command=config_alpha_choose)
alpha_random.pack(side='left')
alpha_choose = Scale(alpha_group, orient=HORIZONTAL, length=236, from_=0, to=1,
    tickinterval=0, resolution=1e-10, relief=SUNKEN)
if DEFAULT_ALPHA is not None:
    alpha_choose.set(DEFAULT_ALPHA)
config_alpha_choose()
alpha_choose.pack(side='right')

print_table_button = Button(table_print, text='Print table',
    command=print_table)
print_table_button.pack()

# Other configurations:
configurations = LabelFrame(pw, text=' Other configurations ',
    borderwidth=2, relief=SUNKEN, height=54)
pw.add(configurations)

hm_maybe = Button(configurations, bitmap="info", command=help_message,
    width=20)
hm_maybe.pack(side='right')

help_label = Label(configurations, text=' FAQ   | Help ')
help_label.pack(side='right')


def open_cnf_file() -> NoReturn:
    from os import startfile
    
    startfile(_WINDOWCONFIG)


open_cnf_button = Button(configurations, text="Open configuration's file",
    command=open_cnf_file)
open_cnf_button.pack(pady=7, side='bottom')

timing_inform = BooleanVar(value=DEFAULT_TIMING_INFORM)
qo_notify = Checkbutton(configurations, text='Notify about timing',
    variable=timing_inform)
qo_notify.pack(side='left')

notify_help = Button(configurations, bitmap="info",
                     command=lambda: mbox.showinfo(
                         "Notify about timing: info",
                         "Whether to notify about the time, "
                         "spent on building graph and table."
    ),
    width=20)
notify_help.pack(side='left')

is_topmost = IntVar(value=int(DEFAULT_IS_TOPMOST))


def local_config() -> NoReturn:
    window.wm_attributes('-topmost', is_topmost.get())


checkbutton = Checkbutton(configurations, text='window is topmost',
    variable=is_topmost, command=local_config)
local_config()
checkbutton.pack()

# Isn't better to insert before packing?
#? entry1.insert(0, 'abs(x)')
nodesn_entry.insert(0, str(DEFAULT_NODES))
borders_entry.insert(0, repr(DEFAULT_BORDERS))

for key, action in WINDOW_KEY_BINDINGS:
    window.bind(key, eval(f"lambda event: {action}"))


window.mainloop()
