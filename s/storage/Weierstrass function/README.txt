Function:
---------
display(3.0, 1/2, borders=(-2, 2))  # maxn = "default",
# i. e. it's equal to int(log(2**1023/(pi*max(map(abs, borders))), abs(a))).
# Here a=3.0, so nmax=int(log(2**1023/(2*pi), 3)).

Figure_1:
---------
func = display(3.0, 1/2, borders=(-2, 2))  # maxn = "default"

space = chebyshev_nodes(-2, 2, 100)
build(linspace(-2, 2, 1000), [lagrange_polynomial(func, space)])

Figure_2:
---------
func = display(3.0, 1/2, borders=(-2, 2))  # maxn = "default"

space = chebyshev_nodes(-2, 2, 200)
build(linspace(-2, 2, 1000), [lagrange_polynomial(func, space)])