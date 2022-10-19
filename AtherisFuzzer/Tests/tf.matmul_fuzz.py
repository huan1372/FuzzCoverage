#This is a Python API fuzzer for tf.matmul
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.matmul_exception.txt","a")
	try:
		parameter_0_choices = []
		# Tensor generation for parameter_0
		parameter_0_DTYPES = [tf.float32,tf.int32]
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
		parameter_1_LIST = fh.get_int_list(min_length=2, max_length=2)
		parameter_1_choices.append(parameter_1_LIST)
		# Tensor generation for parameter_1
		parameter_1_DTYPES = [tf.float32,tf.int32]
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
		a_choices = []
		# Tensor generation for a
		a_DTYPES = [tf.float32]
		int_list = fh.get_int_list(min_length=2,max_length=2)
		min_Val = min(int_list) - 1
		max_Val = max(int_list)
		if min_Val % 2 == 0:
			a_tensor = fh.get_random_numeric_tensor(dtype=fh.get_tf_dtype(allowed_set=a_DTYPES))
		else:
			a_tensor = fh.get_random_numeric_tensor(min_val = min_Val, max_val = max_Val, dtype=fh.get_tf_dtype(allowed_set=a_DTYPES))
		a_tensor = tf.identity(a_tensor)
		a_choices.append(a_tensor)
		a = a_choices[0]
		b_choices = []
		b = b_choices[fh.get_int()%0]
		transpose_b_choices = []
		transpose_b_BOOL = fh.get_bool()
		transpose_b_choices.append(transpose_b_BOOL)
		transpose_b = transpose_b_choices[0]
		arg_class = tf.matmul(parameter_0,parameter_1,a=a,b=b,transpose_b=transpose_b)
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
