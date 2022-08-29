"""Realization of the TDMA.

Brief description
=================

  Realization of the TDMA.

Additional data
===============

  External link: [1].

References
==========

  .. [1] https://en.wikipedia.org/wiki/Tridiagonal_matrix_algorithm
"""


# TODO Test typing everywhere.


__all__ = ['solve_tdma', 'solve_tdma_fast']


from .._typing import (Union, Generator,
                       Number, Vector)


def solve_tdma(a, b, c, f: Vector) -> Vector:
    """Solve the matrix equation with tridiagonal matrix at left part.

    Realisation the TDMA. Here:
     * `b` is the main diagonal, `a` is the lower, `c` is the upper.
     * `f` is the right part.
    """
    alpha = [0]
    beta = [0]
    n = len(f)
    assert len(a) == n-1 and len(b) == n and \
        (len(c) == n-1 or len(c) == n and c[-1] == 0)
    x = [None]*n
    a = [0] + a  # Compatability for computing the alpha.

    for i in range(n-1):
        den = a[i]*alpha[i] + b[i]
        alpha.append(-c[i] / den)
        beta.append((f[i] - a[i]*beta[i]) / den)

    x[-1] = (f[-1] - a[-1]*beta[-1]) / (b[-1] + a[-1]*alpha[-1])

    for i in reversed(range(1, n)):
        x[i-1] = alpha[i]*x[i] + beta[i]

    return x


def _solve_tdma_fast(a, b, c, f):
    n = len(f)
    a = [0] + a  # Compatability for computing the alpha.

    alpha = [0]
    beta = [0]

    for i in range(n-1):
        den = a[i]*alpha[-1] + b[i]
        alpha.append(-c.pop(0) / den)
        beta.append((f[i] - a[i]*beta[-1]) / den)

    yield (_ := (f[-1] - a[-1]*beta[-1]) / (b[-1] + a[-1]*alpha[-1]))

    for i in reversed(range(1, n)):
        yield (_ := alpha[i]*_ + beta[i])


def solve_tdma_fast(a, b, c, f: Vector) -> Generator[Number]:
    """Probably the faster working implementation of the TDMA.
    See the docs for ``solve_tdma'' for more info.
    """
    n = len(f)
    assert len(a) == n-1 and len(b) == n and \
        (len(c) == n-1 or len(c) == n and c[-1] == 0)
    return _solve_tdma_fast(a, b, c, f)


# Tests ---


def inittest():
    from time import time as t
    import sympy

    def show_time(action_id="", *, reload_t0: bool=True):
        nonlocal t0
        print(action_id, end='')
        print(t() - t0)

        if reload_t0:
            t0 = t()

    times = 1_000_000
    measure_number = 1
    
    def measure(func, args=(), kwargs={},
                name='f"Measure number {measure_number}: "',
                *, _times=times, eval_name=True):
        nonlocal t0
        nonlocal measure_number

        t0 = t()
        for _ in range(_times):
            res = func(*args, **kwargs)

        if eval_name:
            name = eval(name)
        show_time(name)
        measure_number += 1
        return res

    # Numpy test
    t0 = t()

    d = sympy.solve_linear_system(sympy.Matrix([
        [1, 3, 0, 2],
        [1, 7, 1, 0],
        [0, 2, 11, 1]
        ]), *sympy.symbols('x y z'))

    show_time('Test with numpy: ')
    print('Results\n' + '='*7)
    print(list(d.values()))
    print(list(map(float, d.values())), end='\n\n')

    # Other tests:
    print(f"Other tests. times = {times}.\n")

    a = [1, 2]
    b = [1, 7, 11]
    c = [3, 1]
    f = [2, 0, 1]

    res = measure(solve_tdma, args=(a, b, c, f), name="Test 1: ",
                  eval_name=False)
    print(res)
    
    _res = measure(solve_tdma_fast, args=(a, b, c, f), name="Test 2: ",
                   eval_name=False)
    print(list(_res)[::-1])


if __name__ == '__main__':
    inittest()
