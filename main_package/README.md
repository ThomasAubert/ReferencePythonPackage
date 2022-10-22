# ReferencePythonPackage
This is a reference package with all best practices

## What is on display?
- File layout (package, subpackage, module doctrings)
- Import structure (with the help of __init__.py and setup.py)
- Adding important package files (README.md, LICENSE, MANIFEST.in, .gitignore)
- Style guides (PEP8, Black, and Google, NumPy or Sphinx styles)
- Registering/publishing package
- Using package template

## Useful vocabulary
- Script - A Python file which is run like 'python myscript.py'
- Package - A directory full of Pyhton code to be imported
- Subpackage - A smaller package inside a package
- Module - A Python file that stores code inside a package
- Library - A package or collection of packages

## Useful links
- [Markdown cheatsheet](https://www.markdownguide.org/cheat-sheet/)
- [Google style](https://google.github.io/styleguide/pyguide.html#s3.8-comments-and-docstrings)
- [NumPy style](https://numpydoc.readthedocs.io/en/latest/format.html)
- [Sphinx style](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html)
- [pyment package](https://pypi.org/project/pyment/)

## Building a python package
### First setup
1. Create a repository and clone in a well suited local directory.
2. Create a 'normal' directory with the name of your Python package.
3. Inside this directory create a Python directory (package) with the same name.
4. Create an init file inside the Python package.

The 'normal' directory will have all the top level files and the Python package.
Repeat step 3 and 4 to create subpackages inside the main package.

### Making it installable
1. Create the setup.py
2. run ```pip install -e <absolute or relative path to package directory>```

### Persisting dependencies