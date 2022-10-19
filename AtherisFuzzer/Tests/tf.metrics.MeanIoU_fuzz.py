#This is a Python API fuzzer for tf.metrics.MeanIoU
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.metrics.MeanIoU_exception.txt","a")
	try:
		num_classes_choices = []
		num_classes_INT = fh.get_int()
		num_classes_choices.append(num_classes_INT)
		num_classes = num_classes_choices[0]
		arg_class = tf.metrics.MeanIoU(num_classes=num_classes)
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
