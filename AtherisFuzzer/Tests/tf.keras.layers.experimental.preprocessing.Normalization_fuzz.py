#This is a Python API fuzzer for tf.keras.layers.experimental.preprocessing.Normalization
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.keras.layers.experimental.preprocessing.Normalization_exception.txt","a")
	try:
		mean_choices = []
		mean_INT = fh.get_int()
		mean_choices.append(mean_INT)
		mean = mean_choices[0]
		variance_choices = []
		variance_INT = fh.get_int()
		variance_choices.append(variance_INT)
		variance = variance_choices[0]
		axis_choices = []
		axis_INT = fh.get_int()
		axis_choices.append(axis_INT)
		axis = axis_choices[0]
		arg_class = tf.keras.layers.experimental.preprocessing.Normalization(mean=mean,variance=variance,axis=axis)
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
