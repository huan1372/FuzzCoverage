from Generator.Types import ArgType
from Generator.ArgCode import Argument
import tensorflow as tf
class TFArgument(Argument):
    _float_values = [0.0, 1.0, -1.0, 63.0, -63.0]
    _tensor_arg_dtypes = [ArgType.TF_TENSOR, ArgType.KERAS_TENSOR, ArgType.TF_VARIABLE]
    _dtypes = [
        tf.bfloat16, tf.bool, tf.complex128, tf.complex64, tf.double,
        tf.float16, tf.float32, tf.float64, tf.half,
        tf.int16, tf.int32, tf.int64, tf.int8,
        tf.uint8, tf.uint16, tf.uint32, tf.uint64,
    ]
    _support_types = [
        ArgType.TF_TENSOR, ArgType.TF_VARIABLE, ArgType.KERAS_TENSOR,
        ArgType.TF_DTYPE, ArgType.TF_OBJECT
    ]

    def __init__(self,type: ArgType, dtype=None,dtype_str=None) -> None:
        if isinstance(dtype, str):
            dtype_str, dtype = self.str_to_dtype(dtype)

        super().__init__(type)
        self.dtype = dtype
        self.dtype_str = dtype_str

    def __str__(self) -> str:
        if self.dtype == None:
            return super().__str__()
        else:
            return super().__str__() + " " + self.dtype_to_str()

    def dtype_to_str(self):
        if self.dtype_str == None:
            return ""
        else:
            return self.dtype_str

    def get_type(self):
        return self.type

    def get_dtype(self):
        return self.dtype_to_str()

    @staticmethod
    def str_to_dtype(dt: str):
        dt = dt.strip().replace("_ref", "")
        if not dt.startswith("tf."):
            dt = "tf." + dt
        try:
            return dt,eval(dt)
        except:
            return dt,tf.float32
    def to_code(self, var_name: str) -> str:
        return super().to_code(var_name)

    def add_str_value(self, value: str):
        return super().add_str_value(value)