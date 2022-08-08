# About the Weierstrass function:
# * https://en.wikipedia.org/wiki/Weierstrass_function
# * https://ru.wikipedia.org/wiki/Функция_Вейерштрасса


# from numpy import cos, linspace, pi
from numpy import linspace
# from sympy import cos, pi
from numpy import pi
# from sympy import pi
# from sympy import cos
from numpy import cos

from functions import *
from spline import *
from helpers.graph_builder import main_mod as build
from helpers import expand


def weierstrass_function(a, b, maxn='default', *, borders=None):
	if maxn == 'default':
		from math import log
		# Not to cause the error with math:
		maxn = int(log(2**1023/(pi*max(map(abs, borders))), abs(a)))
	return lambda x: sum(b**n*cos(a**n*pi*x) for n in range(maxn + 1))


def display(a, b, borders, *, maxn='default'):
	func = weierstrass_function(a, b, maxn, borders=borders)

	...
	'''
	# Test:
	space = chebyshev_nodes(-2, 2, 20)

	build(linspace(*expand(borders, 0.99), 100),
		  [(func, dict(color='green')),
		      (cubic_spline(func, space), dict(color='red')),
		      (lagrange_polynomial(func, space), dict(color='blue'))])
	'''
	return func


if __name__ == '__main__':
	# main()
	...

	func = display(3.0, 1/2, borders=(-2, 2))

	space = chebyshev_nodes(-2, 2, 50)

	# build(linspace(-2, 2, 1000), [func])
	build(linspace(-2, 2, 1000), [lagrange_polynomial(func, space)])
	# build(linspace(-2, 2, 100), [cubic_spline(func, space)])
