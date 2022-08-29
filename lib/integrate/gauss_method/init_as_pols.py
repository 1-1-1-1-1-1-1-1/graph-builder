import sympy
from scipy.integrate import quad
from math import *  # sin, pi, ...  # <- tests
import copy


DEFAULT_NTYPE = None


def _coeffs(n, *, ntype=None):
	res = sympy.solve(sympy.legendre_poly(n))
	if ntype is not None:
		res = map(ntype, res)

	return res


def global_integrate(func, a, b, sep_nodes=None, n=None, ntype=None,
                     integrate_type='auto'):
	raise NotImplementedError

	if integrate_type == 'auto':
		integrate_type = 1 if ntype is None else 2
	if sep_nodes is None:
		sep_nodes = n

	if type(sep_nodes) is dict:
		for item in sep_nodes:
			if sep_nodes[item] is None:
				sep_nodes[item] = n  # Should be not `None`, if is used so.
	elif type(sep_nodes) is int:
		sep_nodes = [(a + (b-a)/(sep_nodes-1)*i, a + (b-a)/(sep_nodes-1)*(i+1))
		for i in range(sep_nodes-1)]
	else:
		# Is it realy great?
		_sep_nodes = copy.deepcopy(sep_nodes)
		sep_nodes = {}
		for item in _sep_nodes:
			sep_nodes[item] = n

		sep_nodes = _sep_nodes  #~

	res = 0

	if type(sep_nodes) is list:
		pre_coeffs = _coeffs(n+1, ntype=ntype)
		for a, b in sep_nodes:
			nodes = [(a+b)/2 + d*(b-a)/2 for d in pre_coeffs]

			# --- Tmp:
			def omega(x):
				res = 1
				for j in range(n+1):
					res *= x - nodes[j]
				return res

			varx = sympy.symbols('x')
			tmp_func = omega(varx)
			
			def c(i):
				int_func = tmp_func / ((varx-nodes[i])*tmp_func.diff(varx).subs({varx: nodes[i]}))
				# print(int_func)  # test
				if integrate_type == 1:
					return sympy.integrate(int_func, (varx, a, b))
				else:
					res = quad(lambda var: int_func.subs({varx: var}), a, b)
					# print(res)  # test
					return res[0]
			# ---
			
			coefficients = [c(i) for i in range(n)]

			for i in range(n):
				res += coefficients[i]*func(nodes[i])
	else:
		pass

	return res


def integrate(func, a, b, n, *, ntype=None, integrate_type='auto'):
	"""Integrate.

	Parameters
	----------
	
	`func` : function, type `callable`.
	`a`, `b` : limits
	`ntype`

	Return
	------
	
	Approximately estimated integral.
	"""
	if integrate_type == 'auto':
		integrate_type = 1 if ntype is None else 2

	nodes = [(a+b)/2 + d*(b-a)/2 for d in _coeffs(n+1, ntype=ntype)]
	# print(nodes)  # test

	def omega(x):
		res = 1
		for j in range(n+1):
			res *= x - nodes[j]
		return res

	varx = sympy.symbols('x')
	tmp_func = omega(varx)
	
	def c(i):
		int_func = tmp_func / ((varx-nodes[i])*tmp_func.diff(varx).subs({varx: nodes[i]}))
		# print(int_func)  # test
		if integrate_type == 1:
			return sympy.integrate(int_func, (varx, a, b))
		else:
			res = quad(lambda var: int_func.subs({varx: var}), a, b)
			# print(res)  #t
			return res[0]

	res = 0
	for i in range(n+1):
		# print('TYPE', c(i), type(c(i)))
		res += c(i)*func(nodes[i])
	
	return res


# Tests ---


def test_1():
	"""Docs."""
	func = sympy.symbols('f', cls=sympy.Function)
	return integrate(func, -1, 1, n=1)


def test_2():
	func = lambda x: sin(x)
	return float(integrate(func, 0, pi, 3, ntype=DEFAULT_NTYPE))


def test(n, args=(), kwargs={}):
	pre_name = "test_" + str(n)
	if pre_name in globals():  #~
		_test = eval(pre_name)
	else:
		raise Exception(f"Not found in globals (name: `{pre_name}`)")
		return
	print(f'#  Test number "{n}"')
	print(_test(*args, **kwargs))
	print('-'*10 + f' End of test `{pre_name}`. ' + '-'*3 + '\n')


def inittest():
	test(1)
	test(2)


if __name__ == '__main__':
	# # print(test_1())
	# test(1)

	# res = test_2()
	# print(res, float(res), sep='\n')
	# # main()

	inittest()

	# func = lambda x: sin(x)/x
	# print(float(global_integrate(func, 0, pi, sep_nodes=10, n=2, integrate_type=2)))
