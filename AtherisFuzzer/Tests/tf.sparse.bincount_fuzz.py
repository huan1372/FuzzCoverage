#This is a Python API fuzzer for tf.sparse.bincount
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.sparse.bincount_exception.txt","a")
	try:
		parameter_0_choices = []
		parameter_0 = parameter_0_choices[fh.get_int()%0]
		axis_choices = []
		axis_INT = fh.get_int()
		axis_choices.append(axis_INT)
		axis = axis_choices[0]
		minlength_choices = []
		minlength_INT = fh.get_int()
		minlength_choices.append(minlength_INT)
		minlength = minlength_choices[0]
		maxlength_choices = []
		maxlength_INT = fh.get_int()
		maxlength_choices.append(maxlength_INT)
		maxlength = maxlength_choices[0]
		weights_choices = []
		weights_LIST = fh.get_int_list(min_length=2, max_length=2)
		weights_choices.append(weights_LIST)
		weights = weights_choices[0]
		binary_output_choices = []
		binary_output_BOOL = fh.get_bool()
		binary_output_choices.append(binary_output_BOOL)
		binary_output = binary_output_choices[0]
		arg_class = tf.sparse.bincount(parameter_0,axis=axis,minlength=minlength,maxlength=maxlength,weights=weights,binary_output=binary_output)
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
