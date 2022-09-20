"""This is a Python API fuzzer for tf.keras.layers.PReLU"""
import atheris
with atheris.instrument_imports():
    import sys
    from python_fuzzing import FuzzingHelper
    import tensorflow as tf

def TestOneInput(input_bytes):
    """This is a Python API fuzzer for tf.keras.layers.PReLU"""
    """
    name: string
    trainable : boolean
    alpha_initializer = None
    alpha_regularizer = None
    alpha_constraint = None
    shared_axes = [int,int]
    """
    fh = FuzzingHelper(input_bytes)

    dtype = fh.get_tf_dtype()
    # Max shape can be 8 in length and randomized from 0-8 without running into
    # a OOM error.
    shape = fh.get_int_list(min_length=0, max_length=8, min_int=0, max_int=8)
    seed = fh.get_int()
    name_list = ["p_re_lu",None,"zeros","alpha"]
    name_index = fh.get_int(min_int=0,max_int=len(name_list))
    name = fh.get_string() if name_index==len(name_list) else name_list[name_index]
    shared_index_1 = fh.get_int(min_int=-1024,max_int=1024)
    shared_index_2 = fh.get_int(min_int=-1024,max_int=1024)
    shared_axes = [shared_index_1,shared_index_2] if name_index%2==0 else None
    #x = tf.saturate_cast(tf.random.uniform(shape=shape, dtype=dtype, seed=seed))
    #arg_input_0 = tf.identity(x)
    #arg_input = [arg_input_0,]
    try:
        arg_class = tf.keras.layers.PReLU(
            name=name,
            trainable = fh.get_bool(),
            alpha_regularizer=None,
            alpha_constraint=None,
            shared_axes=shared_axes
            )
        #_ = arg_class(*arg_input)
    except (tf.errors.InvalidArgumentError, ValueError, TypeError):
        pass



def main():
    atheris.Setup(sys.argv, TestOneInput, enable_python_coverage=True)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
