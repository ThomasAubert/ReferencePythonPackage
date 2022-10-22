"""
Module that helps understand subpackage logic with Sphinx style.
"""
from main_package.module_p import count_character
# from ..module_p import count_character


def sphinx_count(string, char):
    return count_character(string, char)
