# Functions: `_build_graph', `main', `main_mod'.


import matplotlib.pyplot as plt
from sympy import symbols, lambdify
from collections.abc import Iterable


def _build_graph(x, y, grid_plot=True, **build_kwargs):
    """Internal. Plot `x, y` with `build_kwargs`, don't display the plot."""
    global ax  # <- Is it really needed?
    if 'ax' not in globals():
        ax = plt
    ax.plot(x, y, **build_kwargs)
    ax.grid(grid_plot)


def main(iterable: Iterable, grid_plot=True, *, block=True, show=True):
    """Build the graph of each function from `iterable` in one window."""
    global ax
    fig, ax = plt.subplots()
    for x, y, kwargs in iterable:
        _build_graph(x, y, grid_plot, **kwargs)

    if show:
        plt.show(block=block)
        return fig


def main_mod(x, iterable: Iterable, kwargs=None, grid_plot=True,
             form_type='default', mode='update', *, block=True, show=True):
    """Modified version of `main`.

    `x` : iterable of x's (numbers) to build the graph.
    `iterable` : iterable, each item is either `f` or `(f, kw)`, `f` is
                 a callable (function to graph), `kw` is the respective
                 dict of keywords.
    `kwargs` : `dict` object or `None`.
    `form_type` : 1, 2 or "default".
    `mode` : "update" or "rewrite".

    `mode`
    ======
    If "update", changes each item `(y, kw)` (or `y`) of iterable to
    `(y, kw_new)`, where kw_new is `kw`, updated with `kwargs` (or
    `kwargs` if `kw` is absent).
    """
    if not form_type in [1, 2, 'default']:
        raise ValueError("Invalid `form_type`: use 1, 2 or \"default\"")
    
    for i, item in enumerate(iterable):
        try:
            iter(item)
        except:
            iterable[i] = (item, {})

    if kwargs is not None:
        if mode == 'update':
            for i, (item, local_kwargs) in enumerate(iterable):
                local_kwargs.update(kwargs)
                iterable[i] = (item, local_kwargs)
        elif mode == 'rewrite':
            for i, (item, _) in enumerate(iterable):
                iterable[i] = (item, kwargs)
            iterable = ((item, kwargs) for item, _ in iterable)
        else:
            raise ValueError("Undefined mode: use \"update\" or \"rewrite\"")

    def y_1(func, x):
        t = symbols('t')
        maybe_res = lambdify(t, func(t), 'numpy')(x)
        iter(maybe_res)
        assert len(maybe_res) == len(x)

        return maybe_res

    def y_2(func, x):
        return [func(_x) for _x in x]

    def y(func, x):
        if form_type == 1:
            return y_1(func, x)
        if form_type == 2:
            return y_2(func, x)

        try:
            res = y_1(func, x)
        except:
            res = y_2(func, x)

        return res

    return main([(x, y(func, x), kwargs)
                      for func, kwargs in iterable], grid_plot, block=block, show=show)


# Tests ---


if __name__ == '__main__':
    from numpy import *


def test(parts: Iterable):
    # Build graphs and return None.
    #
    # :param:`parts` depending only whether 1, 2, 3 or 4 are included to it.
    #     Tests with the mentioned at `parts` IDs should be complited.
    
    from numpy import linspace
    from sympy import sin, cos, exp

    x = linspace(-10, 20, 100)

    if 1 in parts:
        main([(x, [sin(_x) for _x in x], {}),
              (x[10:], [cos(_x) for _x in x[10:]], dict(color='blue'))
              ], True)
    
    if 2 in parts:
        main([(x, [func(_x) for _x in x], kwargs)
               for func, kwargs in
                   ((sin, dict(linewidth=0.3)), (cos, dict(color='green')))
              ], True)

    if 3 in parts:
        main_mod(x, [sin, cos, lambda x: 1/(1+x**2), lambda x: exp(-x**2 / 2)])

    if 4 in parts:
        from functions import chebyshev_nodes, lagrange_polynomial

        
        def _color(n):
            def helpfunc(n):
                return hex(int(200 / n))[2:]
            return '#' + helpfunc(n)*3

        # func = lambda x: e**(-x**2 / 2)
        # func = abs
        func = lambda x: x**4+3*x + 7 - 8*sin(x)

        # space = lambda n: linspace(-10, 10, n)
        space = lambda n: chebyshev_nodes(-10, 10, n)

        main_mod(x, [(lagrange_polynomial(func, space(n)), {})  #, dict(alpha=1-0.8/n, color=_color(n), linewidth=3/(n**0.5)))
                          for n in range(2, 31+1)])


# --- Tests


if __name__ == '__main__':
    # raise SystemExit(test(parts=[2]))
    # main(...)
    fig, ax = plt.subplots()
    _build_graph([1, 2, 3], [1, 3, 2], label='Test')
    # ax.plot([1, 2, 3], label='Inline label')
    # ax.legend(['Si  mple line'])
    # ax.legend(['T'])
    ax.legend(loc='upper center')
    plt.show()
