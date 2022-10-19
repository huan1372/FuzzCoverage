#This is a Python API fuzzer for tf.keras.layers.Cropping1D
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.keras.layers.Cropping1D_exception.txt","a")
	try:
		cropping_choices = []
		cropping_INT = fh.get_int()
		cropping_choices.append(cropping_INT)
		cropping = cropping_choices[0]
		arg_class = tf.keras.layers.Cropping1D(cropping=cropping)
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
