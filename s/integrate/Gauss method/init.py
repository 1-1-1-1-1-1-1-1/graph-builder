# * https://en.wikipedia.org/wiki/Gaussian_quadrature
# (https://ru.wikipedia.org/wiki/Метод_Гаусса_(численное_интегрирование))
# * https://ru.wikipedia.org/wiki/Алгебраический_порядок_точности_численного_метода
#


def _coeffs(n, ntype=None):
	pass
	import sympy

	res = sympy.solve(sympy.legendre_poly(n))
	if ntype is not None:
		res = map(ntype, res)

	return res

def value_generate(func, a=None, b=None, n=None, *, res_coeffs_type=None):
	if a is None and b is None:
		return lambda a, b: value_generate(func, a, b, n=n)
	...

	# [-1, 1] -> [a, b]
	return (b-a)/n*\
	sum(map(func,
		                   (d*(b-a)/2\
		                    + (a+b)/2 for d in _coeffs(n, res_coeffs_type))
		                   ))
	# c_i*f(x_i) + ...

	# Ex. (for 2):
	# c_1+c_2 = ...
	# c_1*x_1+c_2*x_2 = ...
	# ... .

	# b-a
	# --- (f(x_1) + ... + f(x_n))
	#  n

def main():
	pass


if __name__ == '__main__':
	# from math import sin
	from sympy import sin
	func = lambda x: sin(x)/x
	# print(value_generate(func, 0.1, 2, 70, res_coeffs_type=float))
	from sympy.abc import a, b
	from sympy import symbols
	from sympy import Function  # test
	func = symbols('f', cls=Function)  # test
	print(value_generate(func, n=2, res_coeffs_type=None)(a, b))

	import sympy, scipy.integrate as integrate

	# Was for 70 number of nodes:
	# 1.474661609791697
	# 1.5054685156944179
	# [Finished in 309.1s]

	# print(integrate.quad(func, 0.1, 2)[0])
