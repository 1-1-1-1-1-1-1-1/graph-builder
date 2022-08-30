################################################################################
###########################  !~~~ TO READ ~~~!  ################################
##            ~    ~        ~ ~~           ~~ ~         ~ ~                   ##
## This file was earlier at the root (there were also: the __init__.py, the   ##
## ;__main__.py, the functions.py. Then the root (that folder) has been       ##
## transformed to the package, and no longer the need of saving this exact    ##
## file at that folder exist. This file's interpreting may normally be not    ##
## supported by Python [3+] since the fact the dot notation may be broken     ##
## when running from __main__, but this should be run from the __main__ only. ##
## This file was moved to the folder ./test with a respect to that folder.    ##
## The respective folder test/ had already existed before.                    ##
################################################################################
################################################################################

# Should these be?: single_test, local_test, null_test.


from math import *

from numpy import linspace
from sympy import lambdify, symbols

from ..interpolate.spline import cubic_spline
from ..interpolate import *
from ..linalg.tdma import *
from .._helpers import *
from ..graph_builder import main, main_mod
from ..config import INIT_FUNCTION


ALL_TESTED = [("lagrange_polynomial", "LAGRANGE POLYNOMIAL"),
              ("newton_polynomial_forward", "NEWTON FORWARD POLYNOMIAL"),
              ("cubic_spline", "NATURAL CUBIC SPLINE")
              ]


# Earlier was at `__init__.py`:
def inittest_table(_func, x_points, *, by_func="lagrange_polynomial",
                   extra_info=None, test_points=None, alpha=None):
    print("                    ",
          "--- Running test ---", sep='\n')
    header = ['x', 'f(x)', 'P(x)', 'abs(P(x) - f(x))']

    print(f"#  Interpolation for the `{_func}` using `{by_func}`")
    func = lambda x: eval(_func)

    print("#  Test points: ", end='')
    if test_points is None:
        test_points = x_points
        print("initial.")
    elif test_points is displaced_nodes:
        tmp_kwargs = {}
        if alpha is not None:
            tmp_kwargs.update({"alpha": alpha})
        test_points = displaced_nodes(x_points, **tmp_kwargs)
        print("displaced. alpha: {}.".format(
                   alpha if alpha is not None else "random"))
    else:
        print("input.")

    if extra_info is not None:
        print(extra_info)

    print()

    approx = eval(by_func)(func, x_points)
    lines = [(point,
              func(point),
              approx(point),
              abs(approx(point) - func(point))
              )
             for point in test_points
             ]

    print("\n".join(table(
                          lines, header=tuple(header)
                          )))


# Earlier was at `__init__.py`:
def single_test(number):
    def single_test_1(func=sin):
        print(lagrange_polynomial(func, linspace(0, pi, 11))(0.1))

        approx = newton_polynomial_forward_equidistant(func, 0, pi, 7)
        print(approx(0.1), '='*30, sep='\n')

        lines = [(i, func(i), approx(i)) for i in linspace(0, pi, 100+1)]
        # print(*lines, sep='\n')
        print(*table(lines, header=None), sep='\n')

        raise SystemExit

    def single_test_2(nodes=chebyshev_nodes(-10, 10, 10), alpha=None, func=INIT_FUNCTION):
        """Single test. Is it needed?"""
        inittest_table(func, nodes, by_func="lagrange_polynomial",
            test_points=displaced_nodes, alpha=alpha)

    return eval('single_test_' + str(number))()


# Earlier was at `__init__.py`:
def whole_test(borders=(-10, 10), n: int = 30, alpha=0.5,
               func: str = INIT_FUNCTION,
               tested=ALL_TESTED, _id=None):
    """`borders` : an iterable of length to unpack, borders.
    `n`: number of points, based on which the interpolation should
         be done.
    `alpha` : either a number from 0 to 1, `callable`, which returns
              such number or "None". Is used to build displaced nodes.
    `tested` : iterable, each item is either `str` or
               (<object to eval (function)>, `str`)
    """
    if _id is None:
        _id = 0  # Making a dummy variable not to cause an error.
    # print(func)  # Test
    # print()
    n += 1  # Tested points: x_0, ..., x_n.
    # Fixed:
    space1 = linspace(*borders, n)
    space2 = chebyshev_nodes(*borders, n)

    phrase1 = '#  Using equidistant nodes.'
    phrase2 = '#  Using Chebyshev nodes.'

    def one_test(header, by_func):
        c = __import__("configparser").ConfigParser()  # ... . For the action in `inwindow`.
        c2 = __import__("configparser").ConfigParser()  # <Comment>
        c.read('tmp_configs.ini')
        section = _id
        with open(TMP_CONFIGS, 'w') as f:
            c.write(f)

        def ini_set(value):  # Q.: May `section` be absent?
            # Only one exact config. is here, so reading is not required
            # each time. That config. is modified only here, in theory.
            # c.read('tmp_configs.ini')
            c[section]['done'] = str(value)
            with open(TMP_CONFIGS, 'w') as f:
                c.write(f)

        def is_interrupted():
            c2.read('tmp_configs.ini')
            try:
                return c2.getboolean(section, 'interrupted')
            except:
                return False
        parts_done = 0
        print()
        print(mktitle(header, 72, row=True))

        if is_interrupted(): return
        inittest_table(func, space1, by_func=by_func,
                       extra_info=phrase1, test_points=None)
        parts_done += 1; ini_set(parts_done)

        if is_interrupted(): return
        inittest_table(func, space1, by_func=by_func, extra_info=phrase1,
                       test_points=displaced_nodes, alpha=alpha)
        parts_done += 1; ini_set(parts_done)

        if is_interrupted(): return
        inittest_table(func, space2, by_func=by_func,
                       extra_info=phrase2, test_points=None)
        parts_done += 1; ini_set(parts_done)

        if is_interrupted(): return
        inittest_table(func, space2, by_func=by_func, extra_info=phrase2,
                       test_points=displaced_nodes, alpha=alpha)
        parts_done += 1; ini_set(parts_done)

    for i, item in enumerate(tested):
        if type(item) is str:
            tested[i] = item, item
    for func_, _header in tested:
        header = 'INTERPOLATING WITH ' + _header
        one_test(header, func_)


def compare_build_speed():
    # Test 1 - to test with lamdified function (`approx`).
    # Test 2 - to test with list and init function.
    # Test 3 - to test with list and approximation function.
    import matplotlib.pyplot as plt

    borders = (-10, 10)
    nodes = chebyshev_nodes(*expand(borders, 1), 10)
    approx = lambda x: lagrange_polynomial(lambda x: eval(INIT_FUNCTION), nodes)(x)

    times = 100_000

    x = linspace(*borders, times)

    # Test 1
    print("Starting test 1.")
    t = symbols('t')
    y = lambdify(t, approx(t), 'numpy')(x)
    plt.plot(x, y)
    plt.show()

    # Test 2
    print("Starting test 2.")
    plt.plot(x, [(lambda x: eval(INIT_FUNCTION))(_x) for _x in x])
    plt.show()

    # Test 3
    print("Starting test 3.")
    y2 = [approx(_x) for _x in x]
    plt.plot(x, y2)
    plt.show()


def local_test():
    """Test something. Should it be?"""
    from math import sin

    x = linspace(-10, 20, 100)

    # func = lambda x1: x1**4+3*x1 + 7 - 8*sin(x1)
    func = lambda t: t**2
    space = lambda n: chebyshev_nodes(-10, 10, n)

    approx = lambda n: lagrange_polynomial(func, space(n))
    t = symbols('t')

    def action(i):
        tmpfunc = approx(i)(t)
        # print(repr(tmpfunc()))
        lambdified = lambdify(t, tmpfunc, 'numpy')
        print(type(lambdified(x)))
    
    for i in range(10):
        action(i)

    # action(100)
    # raise SystemExit

    # Result, which was output:
    '''
    <class 'int'>
    <class 'float'>
    <class 'numpy.ndarray'>
    <class 'numpy.ndarray'>
    <class 'numpy.ndarray'>
    <class 'numpy.ndarray'>
    <class 'numpy.ndarray'>
    <class 'numpy.ndarray'>
    <class 'numpy.ndarray'>
    <class 'numpy.ndarray'>
    <class 'numpy.ndarray'>
    [Finished in 81.0s]
    '''
    print(approx(0)(t))
    print(approx(1)(t))
    print(approx(2)(t))

    main_mod(x, [approx(n) for n in range(1, 3+1)])


def test_builder(func, _n, testrange):
    space = lambda n: linspace(0, 1, n)
    x = space(100)
    main_mod(x, [(lagrange_polynomial(func, space(n)), {})
                      for n in testrange], form_type=[1, 2, 'default'][_n], show=False)


# Was at '~/interpolate':
def test_local(*, func=lambda x: x):
    """Compare the speed of two methods: _calling the interpolator each
time and forming a sympy-function_ and _just calling it with required
arguments then_.
"""
    print('-- Local test --')

    from time import time
    
    tmp = symbols('tmp')
    t0 = time()
    
    def show_time():
        print("Time: {}".format(time() - t0))

    show_time()
    asfunc = _lagrange_polynomial(func, linspace(-1, 1, 100), tmp)
    for j in [1, 2, 3]:
        print(asfunc.subs({tmp: j}))
    show_time()
    print('-------')
    
    for j in [1, 2, 3]:
        print(_lagrange_polynomial(func, linspace(-1, 1, 100), j))
    show_time()
    print('-------')
    print("--- End of local test. ---\n")

    raise SystemExit


# Was at `~/functions` and has been edited:
def null_test():
    from helpers.graph_builder import main as build

    func = abs  # lambda x: x*sin(1/x)
    a, b = -1, 1

    borders = a, b
    times = 1000
    kwargs = dict()
    
    approx = lagrange_polynomial(func, linspace(a, b, 7))
           # newton_polynomial_forward(func, a, b, 10, x)  # prev. v.

    x = linspace(*borders, times)
    build([(x, [approx(_x) for _x in x], kwargs)])

    raise SystemExit


if __name__ == '__main__':
    # From `__init__`:
    # whole_test(func="abs(x)")
    whole_test()
    
    input()

    # Other:
    # local_test()

    for _ in range(200):
        test_builder(lambda t: t, _n=1, testrange=[10])
