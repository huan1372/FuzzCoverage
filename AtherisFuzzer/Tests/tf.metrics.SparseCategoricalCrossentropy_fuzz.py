#This is a Python API fuzzer for tf.metrics.SparseCategoricalCrossentropy
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.metrics.SparseCategoricalCrossentropy_exception.txt","a")
	try:
		axis_choices = []
		axis_INT = fh.get_int()
		axis_choices.append(axis_INT)
		axis = axis_choices[0]
		from_logits_choices = []
		from_logits_BOOL = fh.get_bool()
		from_logits_choices.append(from_logits_BOOL)
		from_logits = from_logits_choices[0]
		arg_class = tf.metrics.SparseCategoricalCrossentropy(axis=axis,from_logits=from_logits)
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
