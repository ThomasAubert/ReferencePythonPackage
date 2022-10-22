"""
Reference package
==================

This is a dummy package that serves as reference for structure and style best practices.

Everything that is imported here will be accessible by doing
`import main_package
help(main_package.imported_stuff)`

If we do not import subpackage here, our only option is
`from main_package import subpackage`
"""

# Without importing module_s functions inside subpackage.__init__.py
# Absolute import
# from main_package.subpackage.module_s import google_count, sphinx_count, numpy_count

# Relative import (not recommended!)
# from .subpackage.module_s import google_count, sphinx_count, numpy_count


# After importing module_s functions inside subpackage.__init__.py
# Absolute import
from main_package import subpackage

# Relative import (not recommended!)
# from . import subpackage
