"""This is a Python API fuzzer for tf.keras.layers.PReLU"""
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
    input_tensor = fh.get_random_numeric_tensor()

    _ = tf.abs(x=input_tensor)


def main():
    atheris.Setup(sys.argv, TestOneInput, enable_python_coverage=True)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
