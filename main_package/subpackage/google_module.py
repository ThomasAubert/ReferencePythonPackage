"""
Module that helps understand subpackage logic with Google style.
"""

from main_package.module_p import count_character
# from ..module_p import count_character


def google_count(string, char):
    return count_character(string, char)
