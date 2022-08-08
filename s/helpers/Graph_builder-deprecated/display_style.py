# -*- coding: utf-8 -*-
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

from f import ffs

times = 50

import sympy
t = sympy.symbols('t')

from sympy import latex
functions = 't', '2*t**2'

def ffs(_fs_):
    return sympy.lambdify(t, _fs_, 'sympy')(t)

xf, yf = tuple(map(ffs, functions))
text = r'$ \left\{ x \right\} \{ x \} \left\{ \frac{x}{y} \right\} \{ - \frac{x}{y} \}{}$'
text = r'$ \left\{\,(x, y) \mid x = ' + str(latex(xf) ) + ', y = ' + str(latex(yf) ) + r' \,\right\}$'

mpl.rcParams['font.family'] = 'fantasy'
mpl.rcParams['font.fantasy'] = 'Arial', 'Times New Roman', 'Tahoma'
# string = r'$ \frac {1} {\sigma\cdot\sqrt{2 \pi}} \,e^{ -\frac{ \left( x- \mu \right)^2} {2\sigma^2}} $'
string = r'$ y(x) = {} $'.format('1+2*x**7-3'.replace('**', '^').replace('*', r'\cdot '))
string = text
x = np.linspace(-3, 5, times)
# sigma = 1
# mu = 1
sigma, mu = 1,1
y = (1 / (sigma*np.sqrt(2*np.pi))) * np.exp(-(x-mu)**2 / (2*sigma**2))

fig = plt.figure(facecolor = 'white', num = 'Пример оформления графика')
plt.plot(x, y, '-bo', linewidth = 3, markersize = 10, label = string)
plt.legend(fontsize=18, loc='upper left')

ax = fig.gca() # Получить ссылку на объект axes рисунка fig

plt.title(rf'$\mu={mu},\ \sigma={sigma}$')
plt.text(0.58, 0.95, r'График функции $\varphi(x)$',
    horizontalalignment = 'left', verticalalignment = 'center', transform = ax.transAxes,
    fontsize=16) # Положение в относительных координатах окна
ax.annotate('Максимум', xy = (1, 0.4), xytext = (-2, 0.25), arrowprops = dict(facecolor='green', shrink=0.05))
plt.text(-0.9, 0.15, 'График кривой', rotation=70, horizontalalignment='center', verticalalignment='center')

#?
# plt.text(2.5, 0.3, string, fontsize = 24, bbox = dict(edgecolor='w', color='cyan'), color = 'black') # Положение в координатах данных

plt.xlabel(u'$x$ — ось абсцисс', {'fontname': 'Times New Roman'})
plt.ylabel(r'$ \varphi(x) $ — ордината')

plt.grid(True)
plt.show()
