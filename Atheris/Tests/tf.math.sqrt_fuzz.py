"""This is a Python API fuzzer for tf.math.sqrt"""
import atheris
with atheris.instrument_imports():
    import sys
    from python_fuzzing import FuzzingHelper
    import tensorflow as tf


def TestOneInput(data):
    """Test randomized fuzzing input for tf.raw_ops.Abs."""
    fh = FuzzingHelper(data)
    # tf.math.sqrt takes tf.bfloat16, tf.float32, tf.float64,
    # half, tf.complex64,tf.complex128 but get_random_numeric_tensor only generates
    # tf.float16, tf.float32, tf.float64, tf.int32, tf.int64
    # ! TODO: ADD Complex number, and half generator in python fuzzing
    _TF_SQRT_DTYPES = [tf.float16, tf.float32, tf.float64]
    input_tensor = fh.get_random_numeric_tensor(dtype=fh.get_tf_dtype(allowed_set=_TF_SQRT_DTYPES))
    
    _ = tf.math.sqrt(x=input_tensor)


def main():
    atheris.Setup(sys.argv, TestOneInput, enable_python_coverage=True)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
