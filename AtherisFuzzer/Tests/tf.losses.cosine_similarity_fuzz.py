#This is a Python API fuzzer for tf.losses.cosine_similarity
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.losses.cosine_similarity_exception.txt","a")
	try:
		parameter_0_choices = []
		parameter_0_LIST_intLlist = [[[0.0, 1.0], [1.0, 1.0], [1.0, 1.0]]] 
		parameter_0_LIST_intLlist_random = fh.get_int_list(min_length=3, max_length=3,min_int=-255,max_int=255)

		parameter_0_LIST_intLlist.append(parameter_0_LIST_intLlist_random)
		parameter_0_LIST = parameter_0_LIST_intLlist[fh.get_int(min_int=0, max_int=len(parameter_0_LIST_intLlist)-1)]
		parameter_0_choices.append(parameter_0_LIST)
		parameter_0 = parameter_0_choices[0]
		axis_choices = []
		axis_INT_intlist = [1] 
		axis_INT_intlist_random = fh.get_int(min_int=-255,max_int=255)

		axis_INT_intlist.append(axis_INT_intlist_random)
		axis_INT = axis_INT_intlist[fh.get_int(min_int=0, max_int=len(axis_INT_intlist)-1)]
		axis_choices.append(axis_INT)
		axis = axis_choices[0]
		arg_class = tf.losses.cosine_similarity(parameter_0,axis=axis)
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
