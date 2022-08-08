"""
"""

# Should this file be?


import argparse
import sys

from sympy import *  # tests

from helpers.graph_builder import main_mod as build_graph
from functions import *


APPROXIMATORS = {'npf': 'newton_polynomial_forward',
                 'npfe': 'newton_polynomial_forward_equidistant',
                 'lp': 'lagrange_polynomial',
                 'cs': 'cubic_spline'
                 }


class CustomFormatter(argparse.RawDescriptionHelpFormatter,
                      argparse.ArgumentDefaultsHelpFormatter):
    pass


def parse_args(args=sys.argv[1:]):
    """Parse arguments."""
    parser = argparse.ArgumentParser(
        description=sys.modules[__name__].__doc__,
        formatter_class=CustomFormatter)

    parser.add_argument("func", type=str, help="initial function (str)")
    g = parser.add_argument_group("graph settings")
    g.add_argument("-no-build",
                   action='store_true',
                   default=False,
                   help="disable graph's building")
    g.add_argument("--build-option",
                   default='both',
                   type=str,
                   choices=['func', 'approx', 'both'],
                   help="build option")
    g.add_argument("--approx-by",
                   default='lp',
                   type=str,
                   choices=APPROXIMATORS.keys(),
                   help="function to build the approximation (str)")

    parser.add_argument("borders", type=int, nargs=2, help="borders")
    parser.add_argument("nodes_n", type=int, help="number of nodes")

    extra = parser.add_argument_group("extra configurations")
    extra.add_argument("form_args", type=str, nargs='?',
                       default="(chebyshev_nodes(*xborders, nodes_n),)",
                       help="...")
    
    return parser.parse_args(args)


options = parse_args()

def func_test():
    from functions import test

    build_option = options.build_option
    if build_option != 'both':
        build_option = eval('build_option')
    test(eval(options.func), options.borders, eval(APPROXIMATORS[options.approx_by]), options.form_args,
         test_in_points=None,
         build=not options.no_build, build_params={'borders': 0.9, 'times': 100},
         build_option=build_option,
         nodes_n=options.nodes_n)


def main():
    """`main` function."""
    func_test()


if __name__ == '__main__':
    print(options)
    main()