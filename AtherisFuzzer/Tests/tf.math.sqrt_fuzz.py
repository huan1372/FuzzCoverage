#This is a Python API fuzzer for tf.math.sqrt
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.math.sqrt_exception.txt","a")
	try:
		parameter_0_choices = []
		parameter_0_INT = fh.get_int()
		parameter_0_choices.append(parameter_0_INT)
		# Tensor generation for parameter_0
		parameter_0_DTYPES = [tf.float32]
		int_list = fh.get_int_list(min_length=2,max_length=2)
		min_Val = min(int_list) - 1
		max_Val = max(int_list)
		if min_Val % 2 == 0:
			parameter_0_tensor = fh.get_random_numeric_tensor(dtype=fh.get_tf_dtype(allowed_set=parameter_0_DTYPES))
		else:
			parameter_0_tensor = fh.get_random_numeric_tensor(min_val = min_Val, max_val = max_Val, dtype=fh.get_tf_dtype(allowed_set=parameter_0_DTYPES))
		parameter_0_tensor = tf.identity(parameter_0_tensor)
		parameter_0_choices.append(parameter_0_tensor)
		parameter_0 = parameter_0_choices[fh.get_int()%2]
		arg_class = tf.math.sqrt(parameter_0)
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
