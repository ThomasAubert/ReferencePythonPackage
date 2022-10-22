"""
Module that helps understand subpackage logic with Sphinx style.
"""
from main_package.module_p import count_character
# from ..module_p import count_character


def sphinx_count(string, char):
    if not isinstance(string, str) or not isinstance(char, str):
        raise TypeError("Both arguments should be strings.")
    return count_character(string, char)
