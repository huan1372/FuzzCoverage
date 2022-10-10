from DataProcess.Types import ArgType
from Generator.ArgCode import Argument
import tensorflow as tf
class TFArgument(Argument):
    _str_values = ["", "1", "sum", "same", "valid", "zeros"]
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

    def __init__(self,type: ArgType, dtype=None) -> None:
        if isinstance(dtype, str):
            dtype = self.str_to_dtype(dtype)

        super().__init__(type)
        self.dtype = dtype
    def __str__(self) -> str:
        return super().__str__() + " " + self.dtype_to_str()

    def dtype_to_str(self):
        return str(self.dtype)

    @staticmethod
    def str_to_dtype(dt: str):
        dt = dt.strip().replace("_ref", "")
        if not dt.startswith("tf."):
            dt = "tf." + dt
        try:
            return eval(dt)
        except:
            return tf.float32


    def to_code_tensor(self, var_name, low_precision=False):
        dtype = self.dtype
        if low_precision:
            dtype = self.low_precision_dtype(dtype)
        shape = self.shape
        if dtype is None:
            assert (0)
        code = ""
        var_tensor_name = f"{var_name}_tensor"
        if dtype.is_floating:
            code += "%s = tf.random.uniform(%s, dtype=tf.%s)\n" % (var_tensor_name, shape, dtype.name)
        elif dtype.is_complex:
            ftype = "float64" if dtype == tf.complex128 else "float32"
            code += "%s = tf.complex(tf.random.uniform(%s, dtype=tf.%s)," \
                    "tf.random.uniform(%s, dtype=tf.%s))\n" % (var_tensor_name, shape, ftype, shape, ftype)
        elif dtype == tf.bool:
            code += "%s = tf.cast(tf.random.uniform(" \
                   "%s, minval=0, maxval=2, dtype=tf.int32), dtype=tf.bool)\n" % (var_tensor_name, shape)
        elif dtype == tf.string:
            code += "%s = tf.convert_to_tensor(np.ones(%s, dtype=str))\n" % (var_tensor_name, shape)
        elif dtype in [tf.int32, tf.int64]:
            code += "%s = tf.random.uniform(%s, minval=%d, maxval=%d, dtype=tf.%s)\n" \
                % (var_tensor_name, shape, self.minv, self.maxv + 1, dtype.name)
        else:
            code += "%s = tf.saturate_cast(" \
                "tf.random.uniform(%s, minval=%d, maxval=%d, dtype=tf.int64), " \
                "dtype=tf.%s)\n" % (var_tensor_name, shape, self.minv, self.maxv + 1, dtype.name)
        code += f"{var_name} = tf.identity({var_tensor_name})\n"
        return code

    # TODO: Add support for keras
    '''
    def to_code_keras_tensor(self, var_name, low_precision=False):
        return self.to_code_tensor(var_name, low_precision=low_precision)
    '''

    def to_code(self, var_name, low_precision=False) -> str:
        if self.type in [ArgType.LIST, ArgType.TUPLE]:
            code = ""
            arg_name_list = ""
            for i in range(len(self.value)):
                code += self.value[i].to_code(f"{var_name}_{i}", low_precision)
                arg_name_list += f"{var_name}_{i},"

            if self.type == ArgType.LIST:
                code += f"{var_name} = [{arg_name_list}]\n"
            else:
                code += f"{var_name} = ({arg_name_list})\n"
            return code
        elif self.type == ArgType.TF_OBJECT:
            return "%s = None\n" % (var_name)
        elif self.type == ArgType.TF_DTYPE:
            return "%s = tf.%s\n" % (var_name, self.value.name)
        elif self.type in self._tensor_arg_dtypes:
            # Did not consider cloning for in-place operation here.
            code = ""
            if self.type == ArgType.TF_TENSOR:
                code = self.to_code_tensor(var_name, low_precision=low_precision)
            elif self.type == ArgType.TF_VARIABLE:
                code = self.to_code_tensor(var_name, low_precision=low_precision)
                code += "%s = tf.Variable(%s)\n" % (var_name, var_name)
            elif self.type == ArgType.KERAS_TENSOR:
                code = self.to_code_keras_tensor(var_name, low_precision=low_precision)
            return code
        return super().to_code(var_name)


    @staticmethod
    def generate_arg_from_signature(signature):
        if isinstance(signature, bool):
            return TFArgument(signature, ArgType.BOOL)
        if isinstance(signature, int):
            return TFArgument(signature, ArgType.INT)
        if isinstance(signature, float):
            return TFArgument(signature, ArgType.FLOAT)
        if isinstance(signature, str):
            return TFArgument(signature, ArgType.STR)
        if isinstance(signature, list):
            value = []
            for elem in signature:
                value.append(TFArgument.generate_arg_from_signature(elem))
            return TFArgument(value, ArgType.LIST)
        if isinstance(signature, tuple):
            value = []
            for elem in signature:
                value.append(TFArgument.generate_arg_from_signature(elem))
            return TFArgument(value, ArgType.TUPLE)

        if (not isinstance(signature, dict)):
            return TFArgument(None, ArgType.NULL)

        if "type" not in signature and "Label" not in signature:
            return TFArgument(None, ArgType.NULL)

        label = signature["type"] if "type" in signature else signature["Label"]

        if label == "tf_object":
            if "class_name" not in signature:
                return TFArgument(None, ArgType.TF_OBJECT)

            if signature["class_name"] == "tensorflow.python.keras.engine.keras_tensor.KerasTensor" or \
                signature["class_name"] == "tensorflow.python.ops.variables.RefVariable":
                dtype = signature["dtype"]
                shape = signature["shape"]
                dtype = TFArgument.str_to_dtype(dtype)
                minv, maxv = TFArgument.random_tensor_value_range(dtype)
                return TFArgument(None, ArgType.TF_TENSOR, minv, maxv, shape, dtype)
            if signature["class_name"] == "tensorflow.python.framework.dtypes.DType":
                name = signature["to_str"].replace("<dtype: '", "").replace("'>", "")
                value = eval("tf." + name)
                return TFArgument(value, ArgType.TF_DTYPE)
            try:
                value = eval(signature.class_name)
            except:
                value = None
            return TFArgument(value, ArgType.TF_OBJECT)
        if label == "raw":
            try:
                value = json.loads(signature['value'])
            except:
                value = signature['value']
                pass
            if isinstance(value, int):
                return TFArgument(value, ArgType.INT)
            if isinstance(value, str):
                return TFArgument(value, ArgType.STR)
            if isinstance(value, float):
                return TFArgument(value, ArgType.FLOAT)
            if isinstance(value, tuple):
                tuple_value = []
                for elem in value:
                    tuple_value.append(TFArgument.generate_arg_from_signature(elem))
                return TFArgument(tuple_value, ArgType.TUPLE)
            if isinstance(value, list):
                list_value = []
                for elem in value:
                    list_value.append(TFArgument.generate_arg_from_signature(elem))
                return TFArgument(list_value, ArgType.LIST)

        if label == "tuple":
            try:
                value = json.loads(signature['value'])
                tuple_value = []
                for elem in value:
                    tuple_value.append(TFArgument.generate_arg_from_signature(elem))
                return TFArgument(tuple_value, ArgType.TUPLE)
            except:
                raise ValueError("Wrong signature " + str(signature))
        if label == "list":
            try:
                try:
                    value = json.loads(signature['value'])
                except:
                    value = signature['value']
                list_value = []
                for elem in value:
                    list_value.append(TFArgument.generate_arg_from_signature(elem))
                return TFArgument(list_value, ArgType.LIST)
            except:
                raise ValueError("Wrong signature " + str(signature))
        if label in ["tensor", "KerasTensor", "variable", "nparray"]:
            if not ('shape' in signature.keys()
                    and 'dtype' in signature.keys()):
                raise Exception('Wrong signature {0}'.format(signature))
            shape = signature['shape']
            dtype = signature["dtype"]
            dtype = TFArgument.str_to_dtype(dtype)

            if isinstance(shape, (list, tuple)):
                minv, maxv = TFArgument.random_tensor_value_range(dtype)
                return TFArgument(None, ArgType.TF_TENSOR, minv, maxv, shape, dtype)
            else:
                minv, maxv = 0, 1
                shape = [1, ]  
                return TFArgument(None, ArgType.TF_TENSOR, minv, maxv, shape, dtype)

        return TFArgument(None, ArgType.NULL)

class TFAPI():
    def __init__(self, api_name) -> None:
        pass

if __name__ == "__main__":
    pass