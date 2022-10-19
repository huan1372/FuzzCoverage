from Generator.Types import ArgType
import tensorflow as tf
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
    _dtypes = [
        "tf.bfloat16", "tf.bool", "tf.complex128", "tf.complex64", "tf.double",
        "tf.float16", "tf.float32", "tf.float64", "tf.half",
        "tf.int16", "tf.int32", "tf.int64", "tf.int8",
        "tf.uint8", "tf.uint16", "tf.uint32", "tf.uint64",
    ]
    _int_values = [-1024, -16, -1, 0, 1, 16, 1024]
    # _float_values = [0.0, 1.0, -1.0, 63.0, -63.0, 1024.0, -1024.0, 1e20, -1e20]

    def __init__(self,type: ArgType,tf_class=""):
        self.type = type
        self.str_value = []
        self.int_list = set()
        self.tf_class = tf_class

    def __str__(self) -> str:
        if self.type == ArgType.INT:
            return "INT"
        elif self.type == ArgType.FLOAT:
            return "FLOAT"
        elif self.type == ArgType.BOOL:
            return "BOOL"
        elif self.type == ArgType.STR:
            return "STR"
        elif self.type == ArgType.TF_TENSOR:
            return "TF_TENSOR"
        elif self.type == ArgType.LIST:
            return "LIST"
        elif self.type == ArgType.NULL:
            return "None"
        elif self.type == ArgType.TF_DTYPE:
            return "DTYPE"
        elif self.type == ArgType.TF_OBJECT:
            return "TF_OBJECT"

    def to_code(self, var_name: str) -> str:
        """ArgType.LIST and ArgType.TUPLE should be converted to code in the inherent class"""
        if self.type == ArgType.INT:
            return f"{var_name} = fh.get_int()\n"
        if self.type == ArgType.FLOAT:
            return f"{var_name} = fh.get_float()\n"
        if self.type == ArgType.BOOL:
            return f"{var_name} = fh.get_bool()\n"
        elif self.type == ArgType.STR:
            strListName = var_name + "_strlist"
            strListContent = str(self.str_value)
            return f"{strListName} = {strListContent} \n\t\t{var_name} = {strListName}[fh.get_int(min_int=0, max_int=len({strListName})-1)]\n"
        elif self.type == ArgType.LIST:
            ListName = var_name
            min_l , max_l = self.list_range()
            min_l = str(min_l)
            max_l = str(max_l)
            return f"{ListName} = fh.get_int_list(min_length={min_l}, max_length={max_l})\n"
        elif self.type == ArgType.NULL:
            return f"{var_name} = None\n"
        elif self.type == ArgType.TF_DTYPE:
            strListName = var_name + "_dtypelist"
            if "tf.string" not in self.str_value:
                strListContent = str(self.str_value)
            else:
                strListContent = str(Argument._dtypes)
            return f"{strListName} = {strListContent} \n\t\t{var_name} = eval({strListName}[fh.get_int(min_int=0, max_int=len({strListName})-1)])\n"
        elif self.type == ArgType.TF_OBJECT:
            strListName = var_name + "_tfobjlist"
            strListContent = str(self.str_value)
            return f"{strListName} = {strListContent} \n\t\t{var_name} = eval(\"" + self.tf_class + "\" + {strListName}[fh.get_int(min_int=0, max_int=len({strListName})-1)])\n"
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

    def add_str_value(self,value:str):
        if self.type == ArgType.STR or self.type== ArgType.TF_DTYPE or self.type==ArgType.TF_OBJECT:
            value = value.strip("\"")
            value = value.strip("\'")
            self.str_value.append(value)
            self.str_value = list(set(self.str_value))
        else:
            raise Exception("This type {} is not supported for function add_str_value()")
        return

    def add_list_value(self,value:int):
        self.int_list.add(value)
        return

    def list_range(self):
        if self.type != ArgType.LIST:
            raise Exception("This type {} is not supported for function add_str_value()")
        else:
            return min(self.int_list), max(self.int_list)