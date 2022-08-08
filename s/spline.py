"""This module realises the spline interpolation.

Currently realised spline: natural (`cubic_spline`).

    Usage:
    `cubic_spline(<func: callable>, <nodes: iterable>)` ->
        `<function: callable>`.
"""
# TODO: Remake, which was `a(i)`, to be called in more enegry saving way.


__all__ = ['_cubic_spline_natural', 'cubic_spline']


from sympy import symbols, Matrix, solve_linear_system

from tdma import solve_tdma_fast as tdma


def _cubic_spline_natural(func, nodes, x, *, method=2):
    """Return the cubic spline's value for a given function at point `x`.

    Spline's type: natural.
    """
    nodes = sorted(nodes)
    n = len(nodes) - 1

    def h(i):
        return nodes[i] - nodes[i-1]
    def a(i):
        return func(nodes[i])

    if method == 1:
        system = Matrix([[0]*(i-1)
                        + [h(i), 2*(h(i) + h(i+1)), h(i+1)]
                        + [0]*(n-i-1)
                        + [3*((a(i+1) - a(i))/h(i+1) - (a(i) - a(i-1))/h(i))]
                        for i in range(1, n)]
                        + [[1] + [0]*n + [0]]  # Border conditions.
                        + [[0]*n + [1] + [0]]
                        )
        symbols_ = symbols("c:{}".format(n + 1))
        data = solve_linear_system(system, *symbols_)
        
        def c(i):
            return data[symbols("c" + str(i))]
    
    if method == 2:
        part_f = [0] + [3*((a(i+1) - a(i))/h(i+1) - (a(i) - a(i-1))/h(i)) for i in range(1, n)] + [0]
        data = list(tdma([h(i) for i in range(1, n)] + [0],
                         [1] + [2*(h(i) + h(i+1)) for i in range(1, n)] + [1],
                         [0] + [h(i+1) for i in range(1, n)],
                         part_f))
        def c(i):
            return data[-i-1]
    
    def d(i):
        return (c(i) - c(i-1))/(3*h(i))
    def b(i):
        return (a(i) - a(i-1))/h(i) + (2*c(i) + c(i-1))/3 * h(i)
    def _spline(i):
        tmp = x - nodes[i]
        return a(i) + b(i)*tmp + c(i)*tmp**2 + d(i)*tmp**3

    k = 1
    while x > nodes[k] and x <= nodes[-1]:
        k += 1

    return _spline(k)


def cubic_spline(func, nodes, *, method=2) -> callable:
    """Return the natural cubic spline."""
    return lambda x: _cubic_spline_natural(func, nodes, x, method=method)


### Tests -------


from helpers.graph_builder import main_mod

from helpers import expand


INIT_FUNCTION = "exp(sin(x)) - x/2"


def inittest(func, borders,
             form_space="linspace(*borders, splines_n)",
             *, splines_n=7, k=1.2, method=2):
    """Build 2 graphs: of `func` and its approximation."""
    space = eval(form_space)
    approx = cubic_spline(func, space, method=method)
    
    expanded = expand(borders, k)

    space2 = linspace(*expanded, 100)
    main_mod(space2, [(approx, {'color': 'orange'}), (func, {'color': 'green'})])


def test_speed(func, borders, *, k=1, splines_n=20):
    print("Running test with solving via TDMA.")
    inittest(func, borders, splines_n=splines_n, k=k, method=2)
    print("Running test with solving via `sympy.solve_linear_system`.")
    inittest(func, borders, splines_n=splines_n, k=k, method=1)


if __name__ == '__main__':
    from numpy import exp, linspace
    from numpy import *

    func = lambda x: exp(-x**2 / 2)
    # func = abs
    # func = lambda x: abs(x)**(2/3)
    func = lambda x: eval(INIT_FUNCTION)

    m = 2.2
    borders = (-m, m)

    # inittest(func, borders, k=1, splines_n=4)
    test_speed(func, borders, k=1, splines_n=12)
