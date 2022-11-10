#This is a Python API fuzzer for tf.keras.metrics.Mean
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.keras.metrics.Mean_exception.txt","a")
	try:
		name_choices = []
		name_STR_strlist = ['', 'mean_squared_error', 'mean_absolute_percentage_error', 'mean_absolute_error', 'zeros', 'poisson', 'top_k_categorical_accuracy', 'sum', 'my_mean', 'my_mean_tensor', 'valid', '1', 'max', 'min', 'same', 'squared_hinge', 'mean_squared_logarithmic_error'] 
		name_STR = name_STR_strlist[fh.get_int(min_int=0, max_int=len(name_STR_strlist)-1)]
		name_choices.append(name_STR)
		name_None = None
		name_choices.append(name_None)
		name = name_choices[fh.get_int()%2]
		dtype_choices = []
		dtype_DTYPE_dtypelist = ['', 'zeros', 'sum', 'tf.float32', 'tf.float64', 'valid', '1', 'same'] 
		dtype_DTYPE = eval(dtype_DTYPE_dtypelist[fh.get_int(min_int=0, max_int=len(dtype_DTYPE_dtypelist)-1)])
		dtype_choices.append(dtype_DTYPE)
		dtype_None = None
		dtype_choices.append(dtype_None)
		dtype = dtype_choices[fh.get_int()%2]
		input_signature_choices = []
		input_signature_LIST_intLlist = [[[[1.0, 2.0], [3.0, 2.0], [0.5, 4.0]]], [[1], [5]], [63, 10], [1, 2], [1, 5]] 
		input_signature_LIST_intLlist_random = fh.get_int_list(min_length=1, max_length=2,min_int=-255,max_int=255)

		input_signature_LIST_intLlist.append(input_signature_LIST_intLlist_random)
		input_signature_LIST = input_signature_LIST_intLlist[fh.get_int(min_int=0, max_int=len(input_signature_LIST_intLlist)-1)]
		input_signature_choices.append(input_signature_LIST)
		input_signature_INT_intlist = [200, 1000, 100, 300] 
		input_signature_INT_intlist_random = fh.get_int(min_int=-255,max_int=255)

		input_signature_INT_intlist.append(input_signature_INT_intlist_random)
		input_signature_INT = input_signature_INT_intlist[fh.get_int(min_int=0, max_int=len(input_signature_INT_intlist)-1)]
		input_signature_choices.append(input_signature_INT)
		# Tensor generation for input_signature
		input_signature_DTYPES = [tf.bfloat16, tf.bool, tf.complex128, tf.complex64, tf.float64, tf.float16, tf.float32, tf.float64, tf.float16, tf.int16, tf.int32, tf.int64, tf.int8, tf.uint8, tf.uint16, tf.uint32, tf.uint64]
		int_list = fh.get_int_list(min_length=2,max_length=2)
		min_Val = min(int_list) - 1
		max_Val = max(int_list)
		if min_Val % 2 == 0:
			input_signature_tensor = fh.get_random_numeric_tensor(dtype=fh.get_tf_dtype(allowed_set=input_signature_DTYPES))
		else:
			input_signature_tensor = fh.get_random_numeric_tensor(min_val = min_Val, max_val = max_Val, dtype=fh.get_tf_dtype(allowed_set=input_signature_DTYPES))
		input_signature_tensor = tf.identity(input_signature_tensor)
		input_signature_choices.append(input_signature_tensor)
		input_signature = input_signature_choices[fh.get_int()%3]
		parameter_0_choices = []
		parameter_0_STR_strlist = ['', 'zeros', 'sum', 'valid', '1', 'same', 'root_mean_squared_error'] 
		parameter_0_STR = parameter_0_STR_strlist[fh.get_int(min_int=0, max_int=len(parameter_0_STR_strlist)-1)]
		parameter_0_choices.append(parameter_0_STR)
		parameter_0 = parameter_0_choices[0]
		arg_class = tf.keras.metrics.Mean(parameter_0,name=name,dtype=dtype,)
		arg_input = [input_signature,]
		final_output = arg_class(*arg_input)
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
