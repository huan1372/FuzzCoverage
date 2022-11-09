#This is a Python API fuzzer for tf.transpose
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.transpose_exception.txt","a")
	try:
		parameter_0_choices = []
		parameter_0_LIST_intLlist = [[[1, 2, 3], [4, 5, 6]]] 
		parameter_0_LIST_intLlist_random = fh.get_int_list(min_length=2, max_length=2,min_int=-255,max_int=255)

		parameter_0_LIST_intLlist.append(parameter_0_LIST_intLlist_random)
		parameter_0_LIST = parameter_0_LIST_intLlist[fh.get_int(min_int=0, max_int=len(parameter_0_LIST_intLlist)-1)]
		parameter_0_choices.append(parameter_0_LIST)
		# Tensor generation for parameter_0
		parameter_0_DTYPES = [tf.bfloat16, tf.bool, tf.complex128, tf.complex64, tf.float64, tf.float16, tf.float32, tf.float64, tf.float16, tf.int16, tf.int32, tf.int64, tf.int8, tf.uint8, tf.uint16, tf.uint32, tf.uint64]
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
		perm_choices = []
		perm_LIST_intLlist = [[1, 0], [0, 2, 1], [1, 0, 2], [0, 2, 1, 3], [1, 2, 0]] 
		perm_LIST_intLlist_random = fh.get_int_list(min_length=2, max_length=4,min_int=-255,max_int=255)

		perm_LIST_intLlist.append(perm_LIST_intLlist_random)
		perm_LIST = perm_LIST_intLlist[fh.get_int(min_int=0, max_int=len(perm_LIST_intLlist)-1)]
		perm_choices.append(perm_LIST)
		perm = perm_choices[0]
		conjugate_choices = []
		conjugate_BOOL = fh.get_bool()
		conjugate_choices.append(conjugate_BOOL)
		conjugate = conjugate_choices[0]
		arg_class = tf.transpose(parameter_0,perm=perm,conjugate=conjugate)
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
