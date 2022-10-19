#This is a Python API fuzzer for tf.keras.layers.concatenate
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.keras.layers.concatenate_exception.txt","a")
	try:
		parameter_0_choices = []
		parameter_0 = parameter_0_choices[fh.get_int()%0]
		axis_choices = []
		axis_INT = fh.get_int()
		axis_choices.append(axis_INT)
		axis = axis_choices[0]
		arg_class = tf.keras.layers.concatenate(parameter_0,axis=axis)
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
