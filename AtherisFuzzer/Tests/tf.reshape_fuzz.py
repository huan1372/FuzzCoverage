#This is a Python API fuzzer for tf.reshape
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.reshape_exception.txt","a")
	try:
		parameter_0_choices = []
		parameter_0_LIST = fh.get_int_list(min_length=1, max_length=9)
		parameter_0_choices.append(parameter_0_LIST)
		# Tensor generation for parameter_0
		parameter_0_DTYPES = [tf.int32,tf.float32,tf.bool]
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
		parameter_1_choices = []
		parameter_1_LIST = fh.get_int_list(min_length=0, max_length=4)
		parameter_1_choices.append(parameter_1_LIST)
		parameter_1 = parameter_1_choices[0]
		shape_choices = []
		shape_LIST = fh.get_int_list(min_length=1, max_length=4)
		shape_choices.append(shape_LIST)
		shape = shape_choices[0]
		tensor_choices = []
		# Tensor generation for tensor
		tensor_DTYPES = [tf.float32]
		int_list = fh.get_int_list(min_length=2,max_length=2)
		min_Val = min(int_list) - 1
		max_Val = max(int_list)
		if min_Val % 2 == 0:
			tensor_tensor = fh.get_random_numeric_tensor(dtype=fh.get_tf_dtype(allowed_set=tensor_DTYPES))
		else:
			tensor_tensor = fh.get_random_numeric_tensor(min_val = min_Val, max_val = max_Val, dtype=fh.get_tf_dtype(allowed_set=tensor_DTYPES))
		tensor_tensor = tf.identity(tensor_tensor)
		tensor_choices.append(tensor_tensor)
		tensor = tensor_choices[0]
		arg_class = tf.reshape(parameter_0,parameter_1,shape=shape,tensor=tensor)
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