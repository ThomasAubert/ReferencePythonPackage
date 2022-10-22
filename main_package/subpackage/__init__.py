"""
Subpackage for our reference.

We can make our functions public from the subpackage level with an import here.
This means that we can now do
`import main_package.subpackage as sub
help(sub.google_count)`
Even though the function is defined in a lower module.
"""

# Absolute import
from main_package.subpackage.google_module import google_count
from main_package.subpackage.numpy_module import numpy_count
from main_package.subpackage.sphinx_module import sphinx_count

# Relative import
# from .google_module import google_count
# from .numpy_module import numpy_count
# from .sphinx_module import sphinx_count

