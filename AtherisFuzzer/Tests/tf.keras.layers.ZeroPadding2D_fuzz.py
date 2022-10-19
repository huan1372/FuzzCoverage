#This is a Python API fuzzer for tf.keras.layers.ZeroPadding2D
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.keras.layers.ZeroPadding2D_exception.txt","a")
	try:
		padding_choices = []
		padding_INT = fh.get_int()
		padding_choices.append(padding_INT)
		padding = padding_choices[0]
		parameter_0_choices = []
		parameter_0 = parameter_0_choices[fh.get_int()%0]
		arg_class = tf.keras.layers.ZeroPadding2D(padding=padding,parameter_0)
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
