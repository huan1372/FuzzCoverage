from DataProcess.Types import ArgType
class Argument:
    """
    _support_types: all the types that Argument supports.
    NOTICE: The inherent class should call the method of its parent
    when it does not support its type
    """
    _support_types = [
        ArgType.INT, ArgType.STR, ArgType.FLOAT, ArgType.NULL, ArgType.TUPLE,
        ArgType.LIST, ArgType.BOOL
    ]
    _int_values = [-1024, -16, -1, 0, 1, 16, 1024]
    _str_values = [
        "mean", "sum", "max", 'zeros', 'reflect', 'circular', 'replicate'
    ]
    _float_values = [0.0, 1.0, -1.0, 63.0, -63.0, 1024.0, -1024.0, 1e20, -1e20]

    def __init__(self,type: ArgType):
        self.type = type

    def to_code(self, var_name: str) -> str:
        """ArgType.LIST and ArgType.TUPLE should be converted to code in the inherent class"""
        if self.type == ArgType.INT:
            return f"{var_name} = fh.get_int()\n"
        if self.type == ArgType.FLOAT:
            return f"{var_name} = fh.get_float()\n"
        if self.type == ArgType.BOOL:
            return f"{var_name} = \n"
        elif self.type == ArgType.STR:
            strListName = var_name + "_strlist"
            strListContent = str(_str_values)
            return f"{strListName} = {strListContent} \n{var_name} = {strListName}[fh.get_int(min_int=0, max_int=len({strListName})]\n"
        elif self.type == ArgType.NULL:
            return f"{var_name} = None\n"
        else:
            assert (0)

    @staticmethod
    def get_type(x):
        if x is None:
            return ArgType.NULL
        elif isinstance(x, bool):
            return ArgType.BOOL
        elif isinstance(x, int):
            return ArgType.INT
        elif isinstance(x, str):
            return ArgType.STR
        elif isinstance(x, float):
            return ArgType.FLOAT
        elif isinstance(x, tuple):
            return ArgType.TUPLE
        elif isinstance(x, list):
            return ArgType.LIST
        else:
            return None