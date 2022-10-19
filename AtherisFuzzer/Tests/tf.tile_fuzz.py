#This is a Python API fuzzer for tf.tile
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.tile_exception.txt","a")
	try:
		parameter_0_choices = []
		# Tensor generation for parameter_0
		parameter_0_DTYPES = [tf.int32,tf.bool,tf.float32]
		int_list = fh.get_int_list(min_length=2,max_length=2)
		min_Val = min(int_list) - 1
		max_Val = max(int_list)
		if min_Val % 2 == 0:
			parameter_0_tensor = fh.get_random_numeric_tensor(dtype=fh.get_tf_dtype(allowed_set=parameter_0_DTYPES))
		else:
			parameter_0_tensor = fh.get_random_numeric_tensor(min_val = min_Val, max_val = max_Val, dtype=fh.get_tf_dtype(allowed_set=parameter_0_DTYPES))
		parameter_0_tensor = tf.identity(parameter_0_tensor)
		parameter_0_choices.append(parameter_0_tensor)
		parameter_0 = parameter_0_choices[0]
		parameter_1_choices = []
		parameter_1_LIST = fh.get_int_list(min_length=2, max_length=4)
		parameter_1_choices.append(parameter_1_LIST)
		# Tensor generation for parameter_1
		parameter_1_DTYPES = [tf.int32]
		int_list = fh.get_int_list(min_length=2,max_length=2)
		min_Val = min(int_list) - 1
		max_Val = max(int_list)
		if min_Val % 2 == 0:
			parameter_1_tensor = fh.get_random_numeric_tensor(dtype=fh.get_tf_dtype(allowed_set=parameter_1_DTYPES))
		else:
			parameter_1_tensor = fh.get_random_numeric_tensor(min_val = min_Val, max_val = max_Val, dtype=fh.get_tf_dtype(allowed_set=parameter_1_DTYPES))
		parameter_1_tensor = tf.identity(parameter_1_tensor)
		parameter_1_choices.append(parameter_1_tensor)
		parameter_1 = parameter_1_choices[fh.get_int()%2]
		input_choices = []
		# Tensor generation for input
		input_DTYPES = [tf.int32,tf.string,tf.float32]
		int_list = fh.get_int_list(min_length=2,max_length=2)
		min_Val = min(int_list) - 1
		max_Val = max(int_list)
		if min_Val % 2 == 0:
			input_tensor = fh.get_random_numeric_tensor(dtype=fh.get_tf_dtype(allowed_set=input_DTYPES))
		else:
			input_tensor = fh.get_random_numeric_tensor(min_val = min_Val, max_val = max_Val, dtype=fh.get_tf_dtype(allowed_set=input_DTYPES))
		input_tensor = tf.identity(input_tensor)
		input_choices.append(input_tensor)
		input = input_choices[0]
		multiples_choices = []
		multiples_LIST = fh.get_int_list(min_length=2, max_length=3)
		multiples_choices.append(multiples_LIST)
		multiples = multiples_choices[0]
		arg_class = tf.tile(parameter_0,parameter_1,input=input,multiples=multiples)
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
