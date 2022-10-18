#This is a Python API fuzzer for tf.initializers.truncated_normal
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.initializers.truncated_normal_exception.txt","a")
	try:
		mean_choices = []
		mean_INT = fh.get_int()
		mean_choices.append(mean_INT)
		mean = mean_choices[0]
		stddev_choices = []
		stddev_INT = fh.get_int()
		stddev_choices.append(stddev_INT)
		stddev_FLOAT = fh.get_float()
		stddev_choices.append(stddev_FLOAT)
		stddev = stddev_choices[fh.get_int()%2]
		seed_choices = []
		seed_INT = fh.get_int()
		seed_choices.append(seed_INT)
		seed = seed_choices[0]
		arg_class = tf.initializers.truncated_normal(mean=mean,stddev=stddev,seed=seed)
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
