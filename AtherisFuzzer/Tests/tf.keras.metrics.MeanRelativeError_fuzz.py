#This is a Python API fuzzer for tf.keras.metrics.MeanRelativeError
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.keras.metrics.MeanRelativeError_exception.txt","a")
	try:
		normalizer_choices = []
		# Tensor generation for normalizer
		normalizer_DTYPES = [tf.int32,tf.float32]
		int_list = fh.get_int_list(min_length=2,max_length=2)
		min_Val = min(int_list) - 1
		max_Val = max(int_list)
		if min_Val % 2 == 0:
			normalizer_tensor = fh.get_random_numeric_tensor(dtype=fh.get_tf_dtype(allowed_set=normalizer_DTYPES))
		else:
			normalizer_tensor = fh.get_random_numeric_tensor(min_val = min_Val, max_val = max_Val, dtype=fh.get_tf_dtype(allowed_set=normalizer_DTYPES))
		normalizer_tensor = tf.identity(normalizer_tensor)
		normalizer_choices.append(normalizer_tensor)
		normalizer = normalizer_choices[0]
		arg_class = tf.keras.metrics.MeanRelativeError(normalizer=normalizer)
	except Exception as e:
		exception_type, exception_object, exception_traceback = sys.exc_info()
		line_number = str(exception_traceback.tb_lineno)
		f.write(str(e) + line_number + "\n")
	f.close()
def main():
	atheris.Setup(sys.argv, TestOneInput, enable_python_coverage=True)
	atheris.Fuzz()

if __name__ == "__main__":
	main()
