#This is a Python API fuzzer for tf.keras.layers.ZeroPadding1D
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.keras.layers.ZeroPadding1D_exception.txt","a")
	try:
		padding_choices = []
		padding_INT = fh.get_int()
		padding_choices.append(padding_INT)
		padding = padding_choices[0]
		arg_class = tf.keras.layers.ZeroPadding1D(padding=padding)
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
