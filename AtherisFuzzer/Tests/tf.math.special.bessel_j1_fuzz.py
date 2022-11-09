#This is a Python API fuzzer for tf.math.special.bessel_j1
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.math.special.bessel_j1_exception.txt","a")
	try:
		parameter_0_choices = []
		parameter_0_LIST_intLlist = [[0.5, 1.0, 2.0, 4.0]] 
		parameter_0_LIST_intLlist_random = fh.get_int_list(min_length=4, max_length=4,min_int=-255,max_int=255)

		parameter_0_LIST_intLlist.append(parameter_0_LIST_intLlist_random)
		parameter_0_LIST = parameter_0_LIST_intLlist[fh.get_int(min_int=0, max_int=len(parameter_0_LIST_intLlist)-1)]
		parameter_0_choices.append(parameter_0_LIST)
		parameter_0 = parameter_0_choices[0]
		arg_class = tf.math.special.bessel_j1(parameter_0,)
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
