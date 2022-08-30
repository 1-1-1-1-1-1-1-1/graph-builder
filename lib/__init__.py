# Make this folder a package.


from .config import PACKAGE


exec(f"import {PACKAGE}.\
inwindow_interpolation")

