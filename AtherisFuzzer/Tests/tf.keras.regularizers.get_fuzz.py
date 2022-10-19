#This is a Python API fuzzer for tf.keras.regularizers.get
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.keras.regularizers.get_exception.txt","a")
	try:
		parameter_0_choices = []
		parameter_0_None = None
		parameter_0_choices.append(parameter_0_None)
		parameter_0 = parameter_0_choices[0]
		arg_class = tf.keras.regularizers.get(parameter_0)
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
