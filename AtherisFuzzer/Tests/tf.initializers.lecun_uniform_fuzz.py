#This is a Python API fuzzer for tf.initializers.lecun_uniform
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.initializers.lecun_uniform_exception.txt","a")
	try:
		seed_choices = []
		seed_INT_intlist = [123] 
		seed_INT_intlist_random = fh.get_int(min_int=-255,max_int=255)

		seed_INT_intlist.append(seed_INT_intlist_random)
		seed_INT = seed_INT_intlist[fh.get_int(min_int=0, max_int=len(seed_INT_intlist)-1)]
		seed_choices.append(seed_INT)
		seed = seed_choices[0]
		input_signature_choices = []
		input_signature_LIST_intLlist = [[5, 6, 4, 2]] 
		input_signature_LIST_intLlist_random = fh.get_int_list(min_length=4, max_length=4,min_int=-255,max_int=255)

		input_signature_LIST_intLlist.append(input_signature_LIST_intLlist_random)
		input_signature_LIST = input_signature_LIST_intLlist[fh.get_int(min_int=0, max_int=len(input_signature_LIST_intLlist)-1)]
		input_signature_choices.append(input_signature_LIST)
		input_signature = input_signature_choices[0]
		arg_class = tf.initializers.lecun_uniform(seed=seed,)
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
