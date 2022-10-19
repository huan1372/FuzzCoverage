#This is a Python API fuzzer for tf.repeat
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.repeat_exception.txt","a")
	try:
		parameter_0_choices = []
		parameter_0_LIST = fh.get_int_list(min_length=2, max_length=2)
		parameter_0_choices.append(parameter_0_LIST)
		parameter_0_INT = fh.get_int()
		parameter_0_choices.append(parameter_0_INT)
		parameter_0 = parameter_0_choices[fh.get_int()%2]
		repeats_choices = []
		repeats_LIST = fh.get_int_list(min_length=2, max_length=2)
		repeats_choices.append(repeats_LIST)
		repeats_INT = fh.get_int()
		repeats_choices.append(repeats_INT)
		repeats = repeats_choices[fh.get_int()%2]
		axis_choices = []
		axis_INT = fh.get_int()
		axis_choices.append(axis_INT)
		axis = axis_choices[0]
		arg_class = tf.repeat(parameter_0,repeats=repeats,axis=axis)
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
