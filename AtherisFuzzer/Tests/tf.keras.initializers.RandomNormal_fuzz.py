#This is a Python API fuzzer for tf.keras.initializers.RandomNormal
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.keras.initializers.RandomNormal_exception.txt","a")
	try:
		mean_choices = []
		mean_INT_intlist = [0] 
		mean_INT_intlist_random = fh.get_int(min_int=-255,max_int=255)

		mean_INT_intlist.append(mean_INT_intlist_random)
		mean_INT = mean_INT_intlist[fh.get_int(min_int=0, max_int=len(mean_INT_intlist)-1)]
		mean_choices.append(mean_INT)
		mean = mean_choices[0]
		stddev_choices = []
		stddev_INT_intlist = [1, 100] 
		stddev_INT_intlist_random = fh.get_int(min_int=-255,max_int=255)

		stddev_INT_intlist.append(stddev_INT_intlist_random)
		stddev_INT = stddev_INT_intlist[fh.get_int(min_int=0, max_int=len(stddev_INT_intlist)-1)]
		stddev_choices.append(stddev_INT)
		stddev = stddev_choices[0]
		seed_choices = []
		seed_INT_intlist = [153] 
		seed_INT_intlist_random = fh.get_int(min_int=-255,max_int=255)

		seed_INT_intlist.append(seed_INT_intlist_random)
		seed_INT = seed_INT_intlist[fh.get_int(min_int=0, max_int=len(seed_INT_intlist)-1)]
		seed_choices.append(seed_INT)
		seed = seed_choices[0]
		input_signature_choices = []
		input_signature_LIST_intLlist = [[8, 12, 99]] 
		input_signature_LIST_intLlist_random = fh.get_int_list(min_length=3, max_length=3,min_int=-255,max_int=255)

		input_signature_LIST_intLlist.append(input_signature_LIST_intLlist_random)
		input_signature_LIST = input_signature_LIST_intLlist[fh.get_int(min_int=0, max_int=len(input_signature_LIST_intLlist)-1)]
		input_signature_choices.append(input_signature_LIST)
		input_signature = input_signature_choices[0]
		arg_class = tf.keras.initializers.RandomNormal(mean=mean,stddev=stddev,seed=seed,)
		arg_input = [input_signature,]
		final_output = arg_class(*arg_input)
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
