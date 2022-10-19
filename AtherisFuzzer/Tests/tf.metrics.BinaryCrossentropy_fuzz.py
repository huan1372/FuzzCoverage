#This is a Python API fuzzer for tf.metrics.BinaryCrossentropy
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.metrics.BinaryCrossentropy_exception.txt","a")
	try:
		from_logits_choices = []
		from_logits_BOOL = fh.get_bool()
		from_logits_choices.append(from_logits_BOOL)
		from_logits = from_logits_choices[0]
		label_smoothing_choices = []
		label_smoothing_FLOAT = fh.get_float()
		label_smoothing_choices.append(label_smoothing_FLOAT)
		label_smoothing = label_smoothing_choices[0]
		arg_class = tf.metrics.BinaryCrossentropy(from_logits=from_logits,label_smoothing=label_smoothing)
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
