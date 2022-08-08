import matplotlib.pyplot as plt
from numpy import linspace

from __init__ import _build_graph

def testcolor(color, n):
    x = linspace(0, 1, 100)
    _build_graph(x, [_x + n for _x in x], color=color)

# def grad(srart:, end):

colors1 = [
    'ff00ff',
    'bb00ff',
    '880088',
    'ffffff',
    'ff0000',
    'aa0000'
    ]

def hex_(n):
    return hex(int(n))[2:]
# colors2 = [hex_() + '00' + ]
colors = colors1
for n, color in enumerate(map(lambda string: '#' + string, colors)):
    testcolor(color, n)
plt.show()

if __name__ != '__main__':
    raise SystemExit("Not allowed to launch it in not main")
