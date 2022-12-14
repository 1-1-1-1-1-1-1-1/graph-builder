"""Realization of the solving the System of LAE method(s).

Brief desription
================

  Realization of the solving the System of LAE method(s).
  Implemented method: the iterative method.

Additional data
===============

  External link: [1].

References
==========

  .. [1] At <lib>[/**]/*docs[/].
"""


from .._typing import Vector


def iterative_method_solve(matrixA: 'Matrix', mB: Vector, k) -> Vector:
        """Solve the matrix equation Ax=B and return the result.

	Implemented method: the iterative method.
	"""
	from sympy import Matrix
	
	if k == 0:
		return mB
	n = len(matrixA)

	assert type(k) is int and k > 0

	def _alpha(i, j):
		if i == j:
			return 0
		return - matrixA[i][j] / matrixA[i][i]
	
	alpha = [[_alpha(i, j) for j in range(n)]]
	beta = [mB[i] / matrixA[i][i] for i in range(n)]

	prev = iterative_method_solve(matrixA, mB, k-1)

	return Matrix(beta) + Matrix(alpha) * prev


if __name__ == '__main__':
	mA = [[3, 1,  1],
	      [1, 3, -1],
	      [2, 1, -4]]
	mB = [3, 5, 7]

	for k in range(10):
		print(k, end=': ')
		tmp_res = iterative_method_solve(mA, mB, k)
		print(tmp_res)
