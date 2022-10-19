#This is a Python API fuzzer for tf.nn.bias_add
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.nn.bias_add_exception.txt","a")
	try:
		value_choices = []
		# Tensor generation for value
		value_DTYPES = [tf.float32]
		int_list = fh.get_int_list(min_length=2,max_length=2)
		min_Val = min(int_list) - 1
		max_Val = max(int_list)
		if min_Val % 2 == 0:
			value_tensor = fh.get_random_numeric_tensor(dtype=fh.get_tf_dtype(allowed_set=value_DTYPES))
		else:
			value_tensor = fh.get_random_numeric_tensor(min_val = min_Val, max_val = max_Val, dtype=fh.get_tf_dtype(allowed_set=value_DTYPES))
		value_tensor = tf.identity(value_tensor)
		value_choices.append(value_tensor)
		value = value_choices[0]
		bias_choices = []
		bias = bias_choices[fh.get_int()%0]
		arg_class = tf.nn.bias_add(value=value,bias=bias)
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
