# Tasks
# =====
# 
# * ! Gauss method (2-3 nodes; 2 nodes and composed formula).
#   (for integrating)
# * Rename from bad! Give normal names, not `one`, `two` etc.
# * Write great documentation for it, maybe later.
# * Realise great tests, not inline, which go bad over time.
# * Write comments greatly, and code. In can be read by other people,
#   who can be not so able to read bad code. And why can be illegible
#   or fast-written code better, then written in a classic code-style
#   with a given extra ease to read?

# Questions
# =========
# 
# * In this counts: v_1 or v_2? What value is better to return?


# __all__ = []


import warnings

from numpy import linspace


WARN = False


def one(func, a, b):
    return (func(a) + func(b))/2*(b-a)


# Is it deprecated?
def multiple_trapezoidal_rule_finite_v0(func, a, b, *, start_from=2, eps):
    v_1 = None  # Old
    v_2 = None  # New
    k = 0
    n = start_from * 2**k

    while v_1 is None or abs(v_1 - v_2) >= eps:
        version = 2.31
        # print(n, v_1)
        v_1 = v_2

        h = (b-a) / (n-1)

        # These counts (of the build's time) were made for 
        # `multiple_trapezoidal_rule_finite_v0(sin, 0, pi, eps=eps)`.

        if version == 1:
            # 10.3, 9.6, 9.3, 8.9, 8.9, 8.8, 8.9
            v_2 = 0
            for i in range(n-1):
                v_2 += one(func, a+i*h, a+(i+1)*h)
        if version == 2.1:
            # 7.4, 7.4, 7.2, 7.1, 7.1, 7.1, 7.2
            v_2 = 0
            for i in range(n-1):
                v_2 += func(a+i*h) + func(a+(i+1)*h)
            v_2 *= h/2
        if version == 2.2:
            # 7.0, 7.1, 7.4, 9.1, 7.7, 7.8, 7.4
            v_2 = h/2*sum(func(a+i*h) + func(a+(i+1)*h) for i in range(n-1))
        if version == 2.3:
            # 5.0, 4.9, 4.9, 4.9, 5.1, 4.9, 4.9
            v_2 = h/2*(func(a) + func(b) + 2*sum(map(func, linspace(a, b, n))))
        if version == 2.31:
            #~ 5.2, 4.9, 4.9, 5.1, 4.9, 4.9, 5.0
            v_2 = h*((func(a) + func(b))/2 + sum(map(func, linspace(a, b, n))))

        # nodes = linspace(a, b, n)
        # v_2 = sum(one(func, a_, b_) for a_, b_ in nod)

        k += 1  # Needed?
        n *= 2

    return v_2


def multiple_trapezoidal_rule_finite_v1(func, a, b, *, n='default', eps):
    _v_1 = None  # Old
    h_1 = None
    _v_2 = None  # New
    h_2 = None
    
    if n == 'default':
        n = int((b-a)*eps**(1/2)) + 1

    # print(n)  #
    n = 1

    _v_2 = (func(a) + func(b))/2
    h_2 = (b-a)/n

    while _v_1 is None or abs(h_1*_v_1 - h_2*_v_2) >= eps:
        _v_1 = _v_2
        h_1 = h_2

        h_2 /= 2
        # func(a+(2*i + 1)*h_2) for a in range(n)
        # range(n) -- [0..n-1]
        _v_2 += sum(map(func, (a+(2*i + 1)*h_2 for i in range(n))))

        n *= 2

    return h_2 * _v_2


# def simpson_rule_action(): ...
def simpson_rule(func, a, b, *, n=2, eps, return_mode=0):
    """Return the estimated value of the integral of func from a to b,
    a and b are finite, with error, ideologically less then eps
    (maybe it is not really so).

    `n` — initial number of parts.
    `eps` — positive integer, ...
    """
    assert eps > 0
    eps /= 15
    if eps < 1e-14 and WARN:
        warnings.warn("Using small `eps` may cause non-original behaviour.",
            stacklevel=2)
    _v_1 = None  # Old
    h_1 = None
    _v_2 = None  # New
    h_2 = None

    _v_2 = (func(a) + func(b))/2

    h_2 = (b-a)/(2*n)

    # Add `even`:
    _v_2 += sum(func(a + (2*k)*h_2) for k in range(1, n))
    # Add `Odd`:
    odd = sum(func(a + (2*k-1)*h_2) for k in range(1, n+1))
    _v_2 += 2*odd

    # 1   3   5
    #   2   4  
    while _v_1 is None or abs(h_1*_v_1 - h_2*_v_2)/3*2 >= eps:
        _v_1 = _v_2
        h_1 = h_2

        n *= 2
        h_2 /= 2
        _v_2 -= odd
        odd = sum(map(func, (a + (2*k-1)*h_2 for k in range(1, n+1))))
        _v_2 += 2*odd

    res = h_2/3 * 2*_v_2
    if return_mode == 0:
        return res
    else:
        res = [res]
    if return_mode >= 1:
        res.append(n)
    if return_mode >= 2:
        res.append((h_2))
    return res


# --- Part

# Gauss' method

# --- End of part

# -- tests


def single_test():
    print(simpson_rule(lambda t: 4/(1+t**2), 0, 1, eps=1e-12))
# single_test()


def test_trapezoidal_v0(eps=1e-13):
    from numpy import sin, pi

    return multiple_trapezoidal_rule_finite_v0(sin, 0, pi, eps=eps)


def test_trapezoidal_v1(eps=1e-13, n='default'):
    from numpy import sin, pi

    return multiple_trapezoidal_rule_finite_v1(sin, 0, pi, n=n, eps=eps)


def test_simpson_rule(func=None, a=None, b=None, eps=1):
    from math import sin
    from numpy import pi

    if func is None:
        func = sin
        a, b = 0, pi
    return simpson_rule(func, a, b, eps=eps)


from sympy import oo  # test
from sympy import atan
from math import cos, tan


def test_integrate(_func, a, b, by_func=simpson_rule, *, k='0.99', n=2, eps):
    if oo in (abs(a), abs(b)):
        r"""\int\limits_a^b f(x)\,dx= \left[t=\arctan(x) \Rightarrow
        f(x)\,dx=f(\tan(t))/\cos^2(t)\,dt \ldots \right]
        =\int\limits_{\arctan(a)}^{\arctan(b)} f(\tan(t))/\cos^2(t)\,dt"""
        a, b = map(float, map(atan, (a, b)))
        from sympy import pi
        
        # print(b*2, pi, b+1e-15<pi/2)
        # if b >= pi/2*0.9:
        #     b *= k
        b = (-1 if b < 0 else 1) * min(abs(b), pi/2*float(k))
        func = lambda t: _func(tan(t))/cos(t)**2
        # print()
    else:
        func = _func

    # x = sympy.symbols('x')
    # func = lambdify(lambda t: limit(func(x), x, t))
    res = by_func(func, 0.01, b, n=n, eps=eps)

    return res


def pre__for_infinite(eps=1):
    NotImplemented
    from numpy import sin, pi

    func = lambda x: sin(x) / x
    '''
        +oo
        _
       / sin(t)      pi
      /  ------ dt = --
    _/     t         2
    0
    '''
    # multiple_trapezoidal_rule_finite_v0(sin, 0, n)

    def one_action():
        nonlocal _v_1, _v_2, h_1, h_2, b, n

        n += 1
        b += 1
        # a, b = 0, pi
        # =======
        # n *= 2

        _v_1 = _v_2
        h_1 = h_2
        print(n)  # test

        _v_2 += func(b)
        h_2 /= 2
        '''
        for i in range(n * 2**n):
            res += one(func, 0.0001 + i*h, (i+1)*h)
        '''
        _v_2 += sum(map(func, (a+(2*i + 1)*h_2 for i in range(n * 2**(n-1)))))
        # res = sum(one(func, 0.0001 + i*h_2, (i+1)*h_2)
            # for i in range(n * 2**n))

        # n *= 2

    a = 1e-10
    n = 1  # #! <- See n: if starts from 1, it actually starts from 2.
    b = a + 1

    _v_1 = None
    _v_2 = None

    h_1 = None
    h_2 = None

    _v_2 = (func(a) + func(b))/2
    h_2 = 1

    while _v_1 is None or abs(h_1*_v_1 - h_2*_v_2) >= eps:
        one_action()
        print(abs(h_1*_v_1 - h_2*_v_2))

    return h_2*_v_2


def test_after_change_toplusinfty(func, from_, *, eps=1e-3):
    func_1 = lambda x: func(x-from_)
    # func(1/x__ - 1)/x__^2, x__, 0, 1
    # func_2 = lambda x: func_1(1/x - 1)/x**2
    # func_2 = lambda x: func_1(arctg(x*pi))...

    # near_zero = 1e-14  # Clear?
    near_zero = 1e-7
    to = 1-1e-10  # Test

    by_func = [simpson_rule, multiple_trapezoidal_rule_finite_v1][1]
    return 2*by_func(func_2, near_zero, to, eps=eps)


def test_with_infty_limits(func, a=None, b=None):  # At least one
    k = 0.99  # 0.999999
    res = float(test_integrate(func, 1e-10, +oo, k=k, eps=0.0001))

    return res


def test():
    import math

    # print(test_trapezoidal_v0(10e-12))
    # print(test_trapezoidal_v1(3e-12))
    # eps = 0.003; print(2*pre__for_infinite(eps=eps/2))

    print(test_simpson_rule(eps=1e-15))
    func = lambda x: 2*math.sin(x) / x
    print(test_simpson_rule(func, 1e-10, 1, eps=1e-10))

    # print(test_after_change_toplusinfty(lambda x: math.sin(x) / x, 1e-10))
    # func = lambda x: math.sin(x)/x
    print(test_with_infty_limits(func))


if __name__ == '__main__':
    0.9460830703671831
    test()
