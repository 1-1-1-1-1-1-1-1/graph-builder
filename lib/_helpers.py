"""Some helpers."""


__all__ = ['product', 'displaced_nodes', 'expand', 'mktitle', 'table']


from typing import Iterable, Tuple, Union, Generator
from ._typing import NoReturn, Callable, Optional, Number


N = Number  # Should be a number from 0 to 1...

random = __import__("random").random


def product(iterable: Iterable[Number]) -> Number:
    """Return product of all items of iterable.
    Example: [2, 2, 5] -> 20.
    """
    res = 1
    for item in iterable:
        res *= item
    return res


def displaced_nodes(nodes, *,
                    alpha: Union[Callable[[], N], N] = random):
    """Return displaced nodes (number 1 less than initial).

    `alpha` : is either callable or number.
              If number: should be `0 <= alpha <=1`.
              If callable: should return number from 0 to 1
    """
    tmp = nodes.copy()
    tmp.sort()
    _alpha = alpha
    
    if not callable(_alpha):
        alpha = lambda: _alpha
    else:
        alpha = _alpha

    for item, item_ in zip(tmp[:-1], tmp[1:]):  # Mind to the last node.
        step = item_ - item

        yield item + alpha()*step


def expand(borders, k):
    """Expand the borders. 

    `borders` is iterable object of length 2, `k` is a number.
    Returns borders with symmetrically enlarged in `k` times length.

    Examples:
    
        >>> expand((0, 10), k=1.2)
        (-1.0, 11.0)
        >>> expand((0, 10), k=-1)
        (10.0, 0.0)
    """
    # l, u = borders
    # m = (l + u)/2  # Not essential.
    # d = u - l
    ## l = m - d/2 |-> m - d/2*k, same to u.
    # l -= d/2*(k-1); u += d/2*(k-1)
    # expanded = l, u

    l, u = borders
    assert l < u
    d = u - l
    delta = d/2*(k-1)
    expanded = (l - delta, u + delta)

    return expanded


def mktitle(words: str, n, row=None, *, sep='='):  # `row` - ?
    assert len(sep) == 1
    
    def _align(string, n_times, *, by_symbol=" "):
        # If trying `"{:=...}".format(str(...))`
        # (with exact values intead of '...'): 
        # ``ValueError: '=' alignment not allowed in string format specifier``
        n_ = n_times - len(string)
        return by_symbol * (n_ // 2) + string \
             + by_symbol * ((n_ + 1) // 2)
    
    return \
"""\
#{2}{0}{2}#{row}
# {1} #{row}
#{2}{0}{2}#\
""".format(sep*n, _align(words, n), sep,
           row='\n# ' + ' '*n + ' #' if row is not None else '')


def table(lines: Iterable[Tuple], header: Optional[Tuple[str]], sep="=") \
    -> Optional[Generator]:
    """Make a table. Return either `None`, or a generator object, consisting
    from lines.

    TODO Write examples [possibly doc].
    """
    # Preperation:

    tmp_item = [header] if header is not None else []

    for line in lines + tmp_item:
        assert type(line) is tuple
    if header is not None:
        assert type(header) is tuple and set(map(type, header)) == {str}

    if header:
        assert len(sep) == 1

    if not lines:
        return

    counts = len(lines[0])
    for line in lines:
        if len(line) != counts:
            raise SyntaxError("Wrong data was input.")

    def _length(n: int) -> int:
        return max(len(repr(line[n])) for line in lines + tmp_item)

    length = [_length(n) for n in range(counts)]

    def normalize(line, *, by=repr):
        return ' ' + " | ".join([by(line[n]).ljust(length[n])
                                 for n in range(counts)])

    if header:
        header = normalize(header, by=str)
        yield header

        sepline = sep + "{0}|{0}".format(sep).join(sep*length[n]
                                                   for n in range(counts))
        yield sepline

    for i, line in enumerate(lines):
        yield normalize(line)


# -- Tests -------


def test(borders=(0, 10), k=None) -> NoReturn:
    print(expand(borders, k))


if __name__ == '__main__':
    test(k=0)
    test(k=1)
    test(k=-0.4999)
    test(k=2)

    phrase = "It's a test."
    print(mktitle(phrase, 80))
    print(mktitle(phrase, 79))
    print(mktitle(phrase, len(phrase)))
    print(mktitle(phrase, len(phrase) - 1))
