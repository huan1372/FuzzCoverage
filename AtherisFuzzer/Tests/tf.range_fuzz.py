#This is a Python API fuzzer for tf.range
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.range_exception.txt","a")
	try:
		parameter_0_choices = []
		parameter_0_INT = fh.get_int()
		parameter_0_choices.append(parameter_0_INT)
		# Tensor generation for parameter_0
		parameter_0_DTYPES = [tf.int32,tf.int64]
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
		parameter_1_INT = fh.get_int()
		parameter_1_choices.append(parameter_1_INT)
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
		parameter_2_choices = []
		parameter_2_INT = fh.get_int()
		parameter_2_choices.append(parameter_2_INT)
		parameter_2_FLOAT = fh.get_float()
		parameter_2_choices.append(parameter_2_FLOAT)
		parameter_2 = parameter_2_choices[fh.get_int()%2]
		dtype_choices = []
		dtype_DTYPE_dtypelist = ['tf.int32'] 
		dtype_DTYPE = eval(dtype_DTYPE_dtypelist[fh.get_int(min_int=0, max_int=len(dtype_DTYPE_dtypelist)-1)])
		dtype_choices.append(dtype_DTYPE)
		dtype = dtype_choices[0]
		delta_choices = []
		delta_INT = fh.get_int()
		delta_choices.append(delta_INT)
		delta = delta_choices[0]
		start_choices = []
		start_INT = fh.get_int()
		start_choices.append(start_INT)
		start = start_choices[0]
		limit_choices = []
		limit_INT = fh.get_int()
		limit_choices.append(limit_INT)
		limit = limit_choices[0]
		arg_class = tf.range(parameter_0,parameter_1,parameter_2,dtype=dtype,delta=delta,start=start,limit=limit)
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
