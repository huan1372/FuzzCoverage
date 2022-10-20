from numpy.random import choice, randint
from enum import IntEnum

class ArgType(IntEnum):
    INT = 1
    STR = 2
    FLOAT = 3
    BOOL = 4
    TUPLE = 5
    LIST = 6
    NULL = 7
    DICT = 16
    TORCH_OBJECT = 8
    TORCH_TENSOR = 9
    TORCH_DTYPE = 10
    TF_TENSOR = 11
    TF_DTYPE = 12
    KERAS_TENSOR = 13
    TF_VARIABLE = 14
    TF_OBJECT = 15
