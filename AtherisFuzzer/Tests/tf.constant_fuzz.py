#This is a Python API fuzzer for tf.constant
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.constant_exception.txt","a")
	try:
		parameter_0_choices = []
		parameter_0_INT_intlist = [0, 1] 
		parameter_0_INT_intlist_random = fh.get_int(min_int=-255,max_int=255)

		parameter_0_INT_intlist.append(parameter_0_INT_intlist_random)
		parameter_0_INT = parameter_0_INT_intlist[fh.get_int(min_int=0, max_int=len(parameter_0_INT_intlist)-1)]
		parameter_0_choices.append(parameter_0_INT)
		parameter_0_LIST_intLlist = [[1.8, 2.2], [0.3, 0.7], [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]], [[13, 14, 15], [16, 17, 18]]], [[[5, 0], [7, 0], [0, 0]], [[0, 0], [3, 0], [0, 0]], [[6, 0], [0, 0], [0, 0]]], [[1, 2, 3], [4, 5, 6]], [[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]], [2, 20, 30, 3, 6], [False, True, False, True]] 
		parameter_0_LIST_intLlist_random = fh.get_int_list(min_length=2, max_length=5,min_int=-255,max_int=255)

		parameter_0_LIST_intLlist.append(parameter_0_LIST_intLlist_random)
		parameter_0_LIST = parameter_0_LIST_intLlist[fh.get_int(min_int=0, max_int=len(parameter_0_LIST_intLlist)-1)]
		parameter_0_choices.append(parameter_0_LIST)
		parameter_0_STR_strlist = ['', 'same', 'valid', 'sum', 'palmer 30', 'zeros', '1'] 
		parameter_0_STR = parameter_0_STR_strlist[fh.get_int(min_int=0, max_int=len(parameter_0_STR_strlist)-1)]
		parameter_0_choices.append(parameter_0_STR)
		parameter_0 = parameter_0_choices[fh.get_int()%3]
		dtype_choices = []
		dtype_DTYPE_dtypelist = ['', 'same', 'valid', 'sum', 'tf.float32', 'zeros', '1'] 
		dtype_DTYPE = eval(dtype_DTYPE_dtypelist[fh.get_int(min_int=0, max_int=len(dtype_DTYPE_dtypelist)-1)])
		dtype_choices.append(dtype_DTYPE)
		dtype = dtype_choices[0]
		arg_class = tf.constant(parameter_0,dtype=dtype)
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
