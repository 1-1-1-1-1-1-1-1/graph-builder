Screenshot 3:
-------------

func = weierstrass_function(3, 1/2, 100)
build(linspace(-2, 2, 1000), [(func, {})])

space = chebyshev_nodes(-2, 2, 100)
build(linspace(-2, 2, 1000), [lagrange_polynomial(func, space)])