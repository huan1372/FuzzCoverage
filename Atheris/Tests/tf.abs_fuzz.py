"""This is a Python API fuzzer for tf.abs."""
import atheris
with atheris.instrument_imports():
    import sys
    from python_fuzzing import FuzzingHelper
    import tensorflow as tf


def TestOneInput(data):
    """Test randomized fuzzing input for tf.raw_ops.Abs."""
    fh = FuzzingHelper(data)

    # tf.raw_ops.Abs takes tf.bfloat16, tf.float32, tf.float64, tf.int8, tf.int16,
    # tf.int32, tf.int64, tf.half but get_random_numeric_tensor only generates
    # tf.float16, tf.float32, tf.float64, tf.int32, tf.int64
    try:
        _DTYPES = [tf.bfloat16, tf.float32, tf.float64, tf.int32, tf.int64, tf.complex64, tf.complex128]
        input_tensor = fh.get_random_numeric_tensor(dtype=fh.get_tf_dtype(allowed_set=_DTYPES))
        intarg0 = fh.get_int()
        floatarg0 = fh.get_float()
        int_random = fh.get_int()
        arg0_tensor = tf.identity(input_tensor)
        arg0 = [intarg0,floatarg0,arg0_tensor]
        _ = tf.abs(arg0[int_random%3])
    except Exception as e:
        pass


def main():
    atheris.Setup(sys.argv, TestOneInput, enable_python_coverage=True)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
