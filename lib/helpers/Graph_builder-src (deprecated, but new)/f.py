"""Some helpers. Useful for the main here program. (Main — currently undone.)"""

# __all__ = ['isvar', 'ffs', '_to_integrate', 'CurveParametric', 'CurveOnTheScreen']


from scipy.integrate import quad
import numpy
import sympy

from sympy import cos, sin #t


# PASS is_gridded = __import__('configparser').ConfigParser() # Used just ones.


# ~~~~~~~~~~~~~~~~~~~ ----  Several helpful functions  --- ~~~~~~~~~~~~~~~~~~~ #

def wdd(any_function): # wdd - "warning deprecation" decorator
    def dw(*args, **kwargs): # dw - deprecation warning
        raise DeprecationWarning
    return dw

maybe_deprecated = deprecated = wdd


@maybe_deprecated
def isvar(s, *, version=1):
    SUPPORTED_ISVAR_VERSIONS = (1, 2) # If not deprecating this function and letting it exist, this should be in a global.
    import re
    assert any(map(lambda x: x is version, SUPPORTED_ISVAR_VERSIONS))
    res = re.fullmatch('\w*', s)

    try:
        if version == 1:
            res = re.fullmatch('\D.*', res.string)
            assert not res.string is None
            return True

        elif version == 2:
            assert not True in [res.string.startswith(str(i)) for i in range(10)]
            return True

        else:
            # assert all(map(lambda x: not x is version, SUPPORTED_ISVAR_VERSIONS))
            return False

    except:
        return False

@deprecated
def ffs_v1(_string_, *, ensure_in_smth = True):
    import re
    """Get a sympy-function from a string.

    Example:
        <pass>"""
    try:
        return sympy.S(eval(_string_)) # Case of a constant function.
    except:
        None

    _vars = re.findall('[A-Za-z_]*', _string_); _vars = list(filter(lambda s: s != str(), _vars)); var = _vars[0]

    t = sympy.symbols('t')
    try:
        if ensure_in_smth: #...
            assert _vars == [var]*len(_vars)
            assert isvar(var)
        _string_ = _string_.replace(var, 't') # Maybe not perfect, but it works in case of a clever user (i.e. who doesn't try to crush the program).

        return eval(_string_)
    except:
        return eval(_string_)


# bla, t = sympy.symbols('bla t')
def ffs_v2(_string_, *, max_vars_number = 1): # Does it work corectly? # Seems 2 be like it... but ``symbols`` object shouldn't be at globals.
    # t = sympy.symbols('t')
    attempts = 0; global active_args; #?
    active_args = []

    in_space = globals(), None  # in_space = globals(), locals()

    to_return = None

    while attempts <= max_vars_number:
        attempts += 1
        args = map(eval, active_args) if active_args else (sympy.symbols('t'),)
        try:
            args = list(args)
            # print('TEST:', type(_string_), _string_)
            eval(_string_)
            function = sympy.lambdify(args, _string_, 'numpy')

            # to_return = function
            to_return = eval(_string_)
            break
        except NameError as e:
            var = str(e).split("'")[1] #!
            # print(var)
            active_args.append(var)
            exec("{0} = sympy.symbols({0!r})".format(var), *in_space) # Is it correct?
        except Exception as e:
            raise e

    # print(active_args) #...

    for i in active_args:
        exec("del {}".format(i), globals())
    
    del active_args

    # for i in active_args: exec("del {}".format(i), globals())
    
    if to_return is None:
        raise Exception("An unexpected error occured")

    return to_return


ffs = ffs_v2

# test_function = ffs('bla**2 + bla - cos(bla**2 + 7)/t', max_vars_number = 2)
# print(test_function.__doc__)
# for i in list(range(1, 14)) + [-1, -2, -3]: print(f'   {i}   {test_function(i, 1)}')


def _to_integrate(from_s, *, map_ffs = False, **kwargs):
    """Returns a function to integrate (to find a length of a parametric curve).

    Parameters
    ----------
    from_s : list of functions.
    
    map_ffs : whether to map ``ffs`` to ``from_s`` or not.
    Here ``map_ffs`` should be True, if functions in ``from_s`` are represented as strings.
    In case of an already sympy representation it should be False.
    """
    # Formula to perform:
    r'''  __________________
    _    / ___             |
     \  /  \   
      \/   /__ (x_i(t)')**2
            i
    '''
    if map_ffs:
        from_s = map(lambda obj: ffs(obj, **kwargs), from_s)
    
    t = sympy.symbols('t')
    function = sympy.sqrt(sum([s.diff(t)**2 for s in from_s]))
    return sympy.lambdify(t, function, 'numpy')

class CurveParametric:
    """This object represents a parametric curve."""
    def __init__(self, *fs, borders):
        self.functions = tuple(map(ffs, fs)) # FFS - function format string # FS - functions # Maybe the ``list`` should be here.
        self.borders = borders

    def dimension(self):
        """Get the dimension of a space, where the curve is situated."""
        return len(self.functions)

    def length(self, **kwargs):
        """Get the curve's length.

        Mark: it firstly asserts that all given functions do really represent polinoms (see ``ffs``).
        Currenly kwargs is just ``ensure_in_smth``."""
        try: return quad(_to_integrate(self.functions, **kwargs), *self.borders)
        except Exception as e: print(e)


import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg as figc

# ``function`` and ``g`` are still a testing issue part.
def function(master = None, x = [1,2,3,4,5,6,7], y = [1,0,4,3,5,6,10], *, pack = True, **kwargs):
    figure = plt.figure()
    what_is_it = figure.add_subplot(141)
    what_is_it.plot(x, y, **kwargs)
    why_is_it_needed = figc(figure, master)
    plsno = why_is_it_needed.get_tk_widget()
    plsno.pack()
def g(master = None, x = [1,2,3,4,5,6,7], y = [1,0,4,3,5,6,10], is_first_build = True, **kwargs):
    if is_first_build:
        figure = plt.figure()
        global what_is_it
        what_is_it = figure.add_subplot(999)
    
    what_is_it.plot(x, y, **kwargs)
    is_it_really_needed = figc(figure, master)
    plsno = is_it_really_needed.get_tk_widget()
    plsno.pack()

class CurveOnTheScreen(CurveParametric):
    """Class like a CurveParametric, but with a method ``display``."""
    def __init__(self, *fs, borders):
        super().__init__(*fs, borders = borders)
        
    def display(self, times = 50, in_window = None, grid_it = None, **kwargs):
        """Useful for displaying a 2-D parametric curve."""
        if self.dimension() == 2:
            assert type(grid_it) is bool # Preparation

            # Example of updating the value of `kwargs`:
            # if not 'linewidth' in kwargs:
            #     kwargs['linewidth'] = 3
            bs = self.borders
            space = numpy.linspace(bs[0], bs[1], times)
            x, y = map(lambda function: (sympy.lambdify(sympy.symbols('t'), function, 'numpy'))(space), self.functions)

            if in_window != None:
                return g(master = in_window, x = x, y = y, **kwargs)
            else:
                plt.plot(x, y, **kwargs)
                plt.grid(grid_it); plt.show()
        else:
            raise Exception("2-dimentional space hasn't been found here.")


if __name__ == '__main__':
    test_window = __import__('tkinter').Tk()
    CurveOnTheScreen('t', 't**2', borders = (-4, 3)).display(in_window = test_window, grid_it = True, color = 'red')
    test_window.mainloop()
