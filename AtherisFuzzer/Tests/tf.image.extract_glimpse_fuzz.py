#This is a Python API fuzzer for tf.image.extract_glimpse
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.image.extract_glimpse_exception.txt","a")
	try:
		parameter_0_choices = []
		parameter_0_LIST = fh.get_int_list(min_length=1, max_length=1)
		parameter_0_choices.append(parameter_0_LIST)
		parameter_0 = parameter_0_choices[0]
		size_choices = []
		size_LIST = fh.get_int_list(min_length=2, max_length=2)
		size_choices.append(size_LIST)
		size = size_choices[0]
		offsets_choices = []
		offsets_LIST = fh.get_int_list(min_length=1, max_length=1)
		offsets_choices.append(offsets_LIST)
		offsets = offsets_choices[0]
		centered_choices = []
		centered_BOOL = fh.get_bool()
		centered_choices.append(centered_BOOL)
		centered = centered_choices[0]
		normalized_choices = []
		normalized_BOOL = fh.get_bool()
		normalized_choices.append(normalized_BOOL)
		normalized = normalized_choices[0]
		arg_class = tf.image.extract_glimpse(parameter_0,size=size,offsets=offsets,centered=centered,normalized=normalized)
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
