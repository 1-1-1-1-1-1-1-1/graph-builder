# Make this folder a package.


from .config import package


exec(f"import {package}.\
inwindow_interpolation")

