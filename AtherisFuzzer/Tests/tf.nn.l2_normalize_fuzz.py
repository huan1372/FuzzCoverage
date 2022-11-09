#This is a Python API fuzzer for tf.nn.l2_normalize
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.nn.l2_normalize_exception.txt","a")
	try:
		parameter_0_choices = []
		parameter_0 = parameter_0_choices[fh.get_int()%0]
		axis_choices = []
		axis_LIST_intLlist = [[0, 1, 2]] 
		axis_LIST_intLlist_random = fh.get_int_list(min_length=3, max_length=3,min_int=-255,max_int=255)

		axis_LIST_intLlist.append(axis_LIST_intLlist_random)
		axis_LIST = axis_LIST_intLlist[fh.get_int(min_int=0, max_int=len(axis_LIST_intLlist)-1)]
		axis_choices.append(axis_LIST)
		axis = axis_choices[0]
		arg_class = tf.nn.l2_normalize(parameter_0,axis=axis)
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
