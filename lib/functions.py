"""This module realises the Lagrange and Newton polynoms interpolations
and provides the cubic spline (natural) -- see module `spline`.

Important
=========
  NOTE: Use numba.jit (commented) to possibly speed up, if the appropriate
        software is available on the machine.

Currently realised:
-------------------

`newton_polynomial_forward`,
`newton_polynomial_forward_equidistant`,
`lagrange_polynomial`,
`cubic_spline`.

    Usage:
    ======
    
    `<function>(<func: callable>, arg/args)` ->
        `<function: callable>`,
    where arg/args is `a, b, n` for newton_polynomial_forward_equidistant
    and <nodes: iterable> for other.

    This module also provides `displaced_nodes`, `chebyshev_nodes` and
    `linspace` (from `numpy`).

References:
===========

  .. [1] See all links at this work/project/repository.
"""

# ~~~ Comments for developer. ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# > St. marks the 'statement'.
# 
# St.#1: At this work / file: Comments' syntax is partially LaTeX (marked with `$`).
# St.#2: `numba` can be used to speed up.
# Q#1: Should the assertion of a straight nodes' order be?
# Q#2: What is the difference of Newton forward and str. pol.?
# A#2: There is not different in classic Python. There is a different, if the
#      result is being cached: then adding nodes may be faster then without
#      caching. That way matters, where the nodes are added: left or right.
#      Depending on this, the function type *matter*.


__all__ = [# Newton polynomial:
           '_newton_polynomial_forward', # '_newton_polynomial_backward',
           'newton_polynomial_forward', # 'newton_polynomial_backward',
           '_newton_polynomial_forward_equidistant',
           'newton_polynomial_forward_equidistant',
           # Lagrange polynomial:
           '_lagrange_polynomial', 'lagrange_polynomial',
           # Other:
           'chebyshev_nodes', 'displaced_nodes', 'linspace'
           ]


from math import pi, cos

from numpy import linspace
# import numba

from .helpers import expand, product, displaced_nodes
from .spline import *
from ._typing import (Number)

from .spline import __all__ as sp_all


# From `spline`:
__all__ += sp_all

del sp_all


def chebyshev_nodes(a, b, n) -> list[Number]:
    """n Chebyshev nodes in interval [a, b].

    Their order here is straight.
    """
    s = a + b
    d = b - a
    return [s/2 + d/2 * cos((2*k - 1)/(2*n) * pi)
                for k in reversed(range(1, n + 1))]


def _lagrange_polynomial(func, x_points, x):
    n_ = len(x_points)  # n_ = n + 1

    def basis_polynomial(i):
        def item(j):
            return (x - x_points[j]) / (x_points[i] - x_points[j])
        return product(item(j) for j in range(n_) if j != i)

    return sum(func(x_points[i]) * basis_polynomial(i) for i in range(n_))


# Should it be?
def _finite_diff(func, x_0, h, k, order):
    if order == 0:
        y_k = func(x_0 + h*k)
        return y_k

    order -= 1
    return (_finite_diff(func, x_0, h, k + 1, order)
            - _finite_diff(func, x_0, h, k, order))

# @numba.njit()
def _newton_polynomial_forward_equidistant(func, a, b, n, x):
    assert a < b  # Does it matter [whether a < b or b < a]?
    assert type(n) is int and n > 0

    h = (b - a) / n
    q = (x - a) / h

    def item(k):
        return product(q - s for s in range(k)) / product(range(1, k + 1))

    def finite_diff(order):  # k = 0
        return _finite_diff(func, a, h, 0, order)

    # Examples:
    # * item(0) = <empty product>/<empty product> = 1
    # * finite_diff(0) = func(a + h*0) = func(a)
    # * item(1) = q / 1 = q
    # * finite_diff(1) = $\Delta$ func(a + h*0) = $\Delta y_0$

    return sum(item(k) * finite_diff(k) for k in range(n + 1))

def _newton_polynomial_forward(func, x_points, x, *, version=2.2):
    assert version in [1, 2.1, 2.2] or \
        (type(version) is int and version == 2)
    if version == 2:
        version == 2.1

    if version == 1:
        def divided_difference(points):
            if len(points) == 1:
                return func(points[0])

            return (divided_difference(points[1:]) - divided_difference(points[:-1])) /\
                        (points[-1] - points[0])

        def omega(j):
            return product(x - x_points[k] for k in range(j))

        return sum(divided_difference(x_points[:j+1]) * omega(j)
                   for j in range(len(x_points)))

    if version == 2.1:
        # Copied from the code, which had been shown on the meeting.
        # (With only editions to realise style.)

        # Ranges -- ?

        n_ = len(x_points)
        xi = x_points  #?
        fi = [func(point) for point in x_points]
        fi1 = [None]*(n_)  # What is it?
        fd = [None]*(n_)  #?!
        for i in range(n_):
            fi1[i] = fi[i]
        for i in range(n_):
            fd[i] = fi1[i]
        for i in range(1, n_):
            for k in range(i, n_):
                fd[k] = ((fi1[k] - fi1[k-1]) /\
                       # -------------------
                          (xi[k] - xi[k-i]))
            for k in range(i, n_):
                fi1[k] = fd[k]
        N = fi1[0]
        for i in range(1, n_):
            xx = 1
            for j in range(i):
                xx *= x-xi[j]
            N += fi1[i] * xx
        return N

    if version == 2.2:
        n_ = len(x_points)
        xi = x_points  #?
        fi = [func(point) for point in x_points]
        for i in range(1, n_):
            for k in reversed(range(i, n_)):
                fi[k] = ((fi[k] - fi[k-1]) /\
                       # -----------------
                         (xi[k] - xi[k-i]))
        N = fi[0]
        for i in range(1, n_):
            xx = 1
            for j in range(i):
                xx *= x-xi[j]
            N += fi[i] * xx
        return N

    else:  #~
        # Another v.:
        raise NotImplementedError

        values = [func(node) for node in x_points]
        div_differences_0n_1 = [func(points[0])]
        div_differences_1n = [func(points[0])]
        for i in range(...):
            num = (div_differences_1n[-1] - div_differences_0n_1)
            den = x_points[...] - x_points[...]
            div_differences_0n_1.append(num/den)
            
            num = (div_differences_1n[-1] - div_differences_0n_1)
            den = x_points[...] - x_points[...]
            div_differences_0n_1.append(num/den)

        return sum(divided_difference(x_points[:j+1]) * omega(j)
                   for j in range(len(x_points)))

'''
def _newton_polynomial_backward_equidistant(func, a, b, n, x):
    # assert a < b
    assert type(n) is int and n > 0

    h = (b - a) / n
    q = (x - b) / h

    def item(k):
        return product(q + s for s in range(k)) / product(range(1, k + 1))

    def finite_diff(order):
        return _finite_diff(func, a, h, n - order, order)

    return sum(item(k) * finite_diff(k) for k in range(n + 1))
'''

def newton_polynomial_forward_equidistant(func, a, b, n) -> callable:
    """Implement the Newton polynomial for equidistant nodes.

    Uses the finite difference. See the `Newton polynomial` folder.
    """
    return lambda x: _newton_polynomial_forward_equidistant(func, a, b, n, x)

def newton_polynomial_forward(func, x_points, *, version=2.2) -> callable:
    """Implement the Newton forward polynomial.

    Uses the divided difference. See the `Newton polynomial` folder.
    """
    return lambda x: _newton_polynomial_forward(func, x_points, x, version=version)


def lagrange_polynomial(func, x_points) -> callable:
    """Implement the Lagrange polynomial."""
    return lambda x: _lagrange_polynomial(func, x_points, x)


# --- Tests --------------------------------------------------------------------


# To test: abs [^1].
#
# [^1]: Why should this be tested.
# --------------------------------
# the Runge's phenomenon happens to the `abs`
# function (in particular), hence ensuring the function with that function
# works correctly means the function is preveting the Runge's phenomenon.
# Refering to
# [Runge's phenomenon](https://en.wikipedia.org/wiki/Runge%27s_phenomenon/).
def test(func: callable, xborders=(-10, 10),
         approx_by=lagrange_polynomial,
         form_args: str = "(chebyshev_nodes(*xborders, nodes_n),)",
         test_in_points=None,
         build=True,
         build_params={'borders': 0.9, 'times': 100, 'kwargs': {}},
         build_option='both',
         *, block=True, nodes_n=10, v=2.2):  # `v` - tmp
    assert len(xborders) == 2

    extra_kw = dict(version=v) if approx_by \
        is newton_polynomial_forward else {}
    approx = approx_by(func, *eval(form_args), **extra_kw)

    if test_in_points:
        for var_value in test_in_points:
            print(str(var_value).ljust(20),      
                  approx(eval(var_value))
                  )
        print('=' * 42)

    if build:
        from helpers.graph_builder import main_mod

        build_borders = expand(xborders, build_params['borders'])
        times = build_params['times']
        kwargs = build_params.get('kwargs', {})
        grid_it = kwargs.get('grid_it', True)

        tofunc = (func, dict(color='green', label='Initial function'))
        toapprox = (approx, dict(color='orange'))

        if build_option == 'both':
            funcs = [tofunc, toapprox]
        elif build_option == 'func':
            funcs = [tofunc]
        else:
            assert build_option == 'interpolant'
            funcs = [approx]

        space_ = linspace(*build_borders, times)
        return main_mod(space_, funcs, # kwargs
                        grid_plot=grid_it,
                        form_type=2,  # testing it
                        mode='update', block=block)


if __name__ == '__main__':
##    test(func=abs, xborders=(-1, 1),
##         approx_by=lagrange_polynomial,
##         test_in_points=None,
##         build=True, build_params={'borders': 0.9, 'times': 100},
##         nodes_n=7,
##         form_args="(linspace(*xborders, nodes_n),)")
    
##    test(func=abs, xborders=(-1, 1),
##         approx_by=newton_polynomial_forward,
##         test_in_points=None,
##         build=True, build_params={'borders': 0.9, 'times': 100},
##         nodes_n=7,
##         form_args="(chebyshev_nodes(*xborders, nodes_n),)")
    nodes_n = 40
    test(func=abs, xborders=(-1, 1),
         approx_by=newton_polynomial_forward,
         test_in_points=None,
         build=True, build_params={'borders': 0.9, 'times': 100},
         nodes_n=nodes_n,
         form_args="(chebyshev_nodes(*xborders, nodes_n),)", v=2.1)
    test(func=abs, xborders=(-1, 1),
         approx_by=newton_polynomial_forward,
         test_in_points=None,
         build=True, build_params={'borders': 0.9, 'times': 100},
         nodes_n=nodes_n,
         form_args="(chebyshev_nodes(*xborders, nodes_n),)", v=2.2)
    raise SystemExit

    from helpers.graph_builder import test as test_2

    test_2([4])
