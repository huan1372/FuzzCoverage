#This is a Python API fuzzer for tf.cast
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.cast_exception.txt","a")
	try:
		parameter_0_choices = []
		parameter_0_LIST = fh.get_int_list(min_length=2, max_length=3)
		parameter_0_choices.append(parameter_0_LIST)
		parameter_0_INT = fh.get_int()
		parameter_0_choices.append(parameter_0_INT)
		parameter_0_FLOAT = fh.get_float()
		parameter_0_choices.append(parameter_0_FLOAT)
		# Tensor generation for parameter_0
		parameter_0_DTYPES = [tf.float32,tf.int32,tf.bool,tf.float64,tf.int64,tf.uint8]
		int_list = fh.get_int_list(min_length=2,max_length=2)
		min_Val = min(int_list) - 1
		max_Val = max(int_list)
		if min_Val % 2 == 0:
			parameter_0_tensor = fh.get_random_numeric_tensor(dtype=fh.get_tf_dtype(allowed_set=parameter_0_DTYPES))
		else:
			parameter_0_tensor = fh.get_random_numeric_tensor(min_val = min_Val, max_val = max_Val, dtype=fh.get_tf_dtype(allowed_set=parameter_0_DTYPES))
		parameter_0_tensor = tf.identity(parameter_0_tensor)
		parameter_0_choices.append(parameter_0_tensor)
		parameter_0 = parameter_0_choices[fh.get_int()%4]
		dtype_choices = []
		dtype_DTYPE_dtypelist = ['tf.float32', 'tf.int32'] 
		dtype_DTYPE = eval(dtype_DTYPE_dtypelist[fh.get_int(min_int=0, max_int=len(dtype_DTYPE_dtypelist)-1)])
		dtype_choices.append(dtype_DTYPE)
		dtype_STR_strlist = ['int64'] 
		dtype_STR = dtype_STR_strlist[fh.get_int(min_int=0, max_int=len(dtype_STR_strlist)-1)]
		dtype_choices.append(dtype_STR)
		dtype = dtype_choices[fh.get_int()%2]
		parameter_1_choices = []
		parameter_1_DTYPE_dtypelist = ['tf.complex128', 'tf.uint8', 'tf.float32', 'tf.int32', 'tf.float64'] 
		parameter_1_DTYPE = eval(parameter_1_DTYPE_dtypelist[fh.get_int(min_int=0, max_int=len(parameter_1_DTYPE_dtypelist)-1)])
		parameter_1_choices.append(parameter_1_DTYPE)
		parameter_1 = parameter_1_choices[0]
		arg_class = tf.cast(parameter_0,dtype=dtype,parameter_1)
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
