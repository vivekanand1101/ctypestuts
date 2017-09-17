# coding=utf-8

import ctypes

_add = ctypes.CDLL('/home/vivek/ctypestuts/libadd2nums.so')
_add.add_two_numbers.argtypes = (ctypes.c_int, ctypes.c_int)

def add_two_numbers(num1, num2):
    ''' Adds two numbers '''

    return _add.add_two_numbers(ctypes.c_int(num1), ctypes.c_int(num2))
