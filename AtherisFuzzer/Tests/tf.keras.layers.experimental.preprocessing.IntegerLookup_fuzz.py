#This is a Python API fuzzer for tf.keras.layers.experimental.preprocessing.IntegerLookup
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.keras.layers.experimental.preprocessing.IntegerLookup_exception.txt","a")
	try:
		vocabulary_choices = []
		vocabulary_LIST = fh.get_int_list(min_length=4, max_length=4)
		vocabulary_choices.append(vocabulary_LIST)
		vocabulary = vocabulary_choices[0]
		invert_choices = []
		invert_BOOL = fh.get_bool()
		invert_choices.append(invert_BOOL)
		invert = invert_choices[0]
		num_oov_indices_choices = []
		num_oov_indices_INT = fh.get_int()
		num_oov_indices_choices.append(num_oov_indices_INT)
		num_oov_indices = num_oov_indices_choices[0]
		arg_class = tf.keras.layers.experimental.preprocessing.IntegerLookup(vocabulary=vocabulary,invert=invert,num_oov_indices=num_oov_indices)
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
