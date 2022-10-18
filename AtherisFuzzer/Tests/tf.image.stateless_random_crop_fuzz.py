#This is a Python API fuzzer for tf.image.stateless_random_crop
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.image.stateless_random_crop_exception.txt","a")
	try:
		value_choices = []
		value_LIST = fh.get_int_list(min_length=2, max_length=2)
		value_choices.append(value_LIST)
		value = value_choices[0]
		size_choices = []
		size_LIST = fh.get_int_list(min_length=3, max_length=3)
		size_choices.append(size_LIST)
		size = size_choices[0]
		seed_choices = []
		seed_LIST = fh.get_int_list(min_length=2, max_length=2)
		seed_choices.append(seed_LIST)
		seed = seed_choices[0]
		arg_class = tf.image.stateless_random_crop(value=value,size=size,seed=seed)
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
