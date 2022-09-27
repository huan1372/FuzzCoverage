"""This is a Python API fuzzer for tf.math.sqrt"""
from email.mime import image
import atheris
with atheris.instrument_imports():
    import sys
    from python_fuzzing import FuzzingHelper
    import tensorflow as tf


def TestOneInput(data):
    """Test randomized fuzzing input for tf.raw_ops.Abs."""
    fh = FuzzingHelper(data)
    # lower_bound >=0 and lower_bound < upperbound

    lower_bound = fh.get_float()
    upper_bound = fh.get_float()
    image = []
    dimension1 = fh.get_int(min_int=1,max_int=10)
    dimension2 = fh.get_int(min_int=1,max_int=10)
    for i in range(dimension1):
        new_dimension1 = []
        for j in range(dimension2):
            arg_0 = fh.get_float_list(min_length=3,max_length=3)
            new_dimension1.append(arg_0)
        image.append(new_dimension1)
    try:
        _ = tf.image.random_contrast(image,lower_bound, upper_bound)
    except (tf.errors.InvalidArgumentError, ValueError, TypeError):
        pass


def main():
    atheris.Setup(sys.argv, TestOneInput, enable_python_coverage=True)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
