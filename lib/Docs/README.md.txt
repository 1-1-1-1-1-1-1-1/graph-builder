README
======

> !This is about the documentation to the building of this structure.

Main
----

Solving the System of Analytical linear equations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 - Tridiagonal matrix algorithm (TDMA): https://ru.wikipedia.org/wiki/Метод_прогонки (https://en.wikipedia.org/wiki/Tridiagonal_matrix_algorithm).
	+ Implementing formulas from `TDMA.png`.
 - Iterative method: https://ru.wikipedia.org/wiki/Метод_итерации (https://en.wikipedia.org/wiki/Iterative_method)
 - Trapezoidal rule: https://ru.wikipedia.org/wiki/Метод_трапеций (https://en.wikipedia.org/wiki/Trapezoidal_rule)

Interpolation
~~~~~~~~~~~~~

 - Lagrange polynomial: https://ru.wikipedia.org/wiki/Интерполяционный_многочлен_Лагранжа (https://en.wikipedia.org/wiki/Lagrange_polynomial)
	+ Implementing formulas from "Lagrange-polynomial.png".
 - Newton polinomial: see the "Newton polynomial" folder.
 - Cubic spline: https://ru.wikipedia.org/wiki/Кубический_сплайн, https://ru.wikipedia.org/wiki/Сплайн (https://en.wikipedia.org/wiki/Spline_interpolation)
	+ Implementing formulas, using the data at "Spline-interpolation.png".
 - Runge's phenomenon: https://ru.wikipedia.org/wiki/Феномен_Рунге (https://en.wikipedia.org/wiki/Runge%27s_phenomenon). To minimize the effect of it, Chebyshev nodes can be used.
 - Chebyshev nodes: https://ru.wikipedia.org/wiki/Узлы_Чебышёва (https://en.wikipedia.org/wiki/Chebyshev_nodes)
	+ See the "Runge's phenomen" folder.

Integration
~~~~~~~~~~~

#### With Runge's rule

 - http://www.electro-vgsha.narod.ru/Biblioteka/Chislennye_metody.pdf (c. 72)
 - https://ru.wikipedia.org/wiki/Правило_Рунге
 - https://encyclopediaofmath.org/wiki/Runge_rule
 - "Правило Рунге": https://studfile.net/preview/2640020/page:2/

#### Gaussian

 - https://en.wikipedia.org/wiki/Gaussian_quadrature (https://ru.wikipedia.org/wiki/Метод_Гаусса_(численное_интегрирование))
 - https://ru.wikipedia.org/wiki/Алгебраический_порядок_точности_численного_метода

Other
-----

 - Useful link: http://mathhelpplanet.com/static.php?p=chislennyye-metody-resheniya-slau.
 - About interpolation: https://ru.wikipedia.org/wiki/Интерполяция (https://en.wikipedia.org/wiki/Interpolation)
 - Maybe useful:
	* https://studfile.net/preview/3075823/page:3/
	* https://old.math.tsu.ru/EEResources/cm/text/4_7_1.htm#:~:text=Метод%20прогонки%20является%20частным%20случаем,161–166%5D).&text=Указанное%20ускорение%20вычислений%20допускают%20системы,треугольными%20и%20другими%20матрицами%20(см.
 - Доступ к глобальной переменной Python между файлами: https://coderoad.ru/25072311/Доступ-к-глобальной-переменной-Python-между-файлами
