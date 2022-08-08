"""Docs"""

r'''
 1                    1
 /                    /
 |  dx     pi         |  4
 |------ = -- => pi = |------dx
 |1+x**2   4          |1+x^2 
/                     /
 0                    0
'''

from trapezoidal_rule_functions import simpson_rule


def simpson_rule_modified(func, a, b, *, n=2, start_eps=1, end_at=1e-15):
    """Docs. from init:

    Return the estimated value of the integral of func from a to b,
    a and b are finite, with error, ideologically less then eps
    (maybe it is not really so).

    `n` — initial number of parts.
    `eps` — positive integer, ...
    """
    assert start_eps > 0
    '''
    # if start_eps < 1e-14 and WARN:
        # warnings.warn("Using small `eps` can cause non-original behaviour.",
            # stacklevel=2)
    '''
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

    def action(eps):
        nonlocal _v_1, _v_2, h_1, h_2, n, odd
        while _v_1 is None or abs(h_1*_v_1 - h_2*_v_2)/3*2 >= eps:
            # print("Eps.", eps)
            _v_1 = _v_2
            h_1 = h_2

            n *= 2
            h_2 /= 2
            _v_2 -= odd
            odd = sum(map(func, (a + (2*k-1)*h_2 for k in range(1, n+1))))
            _v_2 += 2*odd
        return h_2/3*2*_v_2

    import re

    eps = start_eps
    digits = []
    is_first_print = True
    printed = None
    while eps > end_at:
        _v_1 = None  # test
        res = action(eps)
        # print(res)
        number = int(abs(res/eps))
        number = str(number)
        eps /= 10
        if not is_first_print:
            number = "".join(list(number)[-(-printed+1):])
        actual, other = re.fullmatch(r'(-?[0-9\.]*?)([0\.9]*)', number).groups()
        print(actual, end='')
        printed = -len(other.replace('.', ''))
        digits = list(other)
        if is_first_print:
            is_first_print = False
        
        # print(number)
        
    if digits:
        for i in digits: print(i, end='')
    return


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

def main_v1():
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

if __name__ == '__main__':
    func = lambda t: 4/(1+t**2)
    simpson_rule_modified(func, 0, 1, end_at=1e-16)