from typing import (Union, NoReturn,)
from collections.abc import Generator, Iterable, Callable


# - Not sure if it is compatible with complex.
# - Not sure this soft is capable for complex sphere, but, seems to be, it is...
# + Just release, all is great I see that.
# + Don't know the algorithm, just release.
Number = Union[float, complex]
NormalFunc = Callable[Number, Number]

Vector = list[Number]
