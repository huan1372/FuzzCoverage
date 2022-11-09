#This is a Python API fuzzer for tf.keras.losses.SquaredHinge
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.keras.losses.SquaredHinge_exception.txt","a")
	try:
		reduction_choices = []
		reduction_STR_strlist = ['', 'same', 'valid', 'sum', 'none', 'zeros', '1'] 
		reduction_STR = reduction_STR_strlist[fh.get_int(min_int=0, max_int=len(reduction_STR_strlist)-1)]
		reduction_choices.append(reduction_STR)
		reduction = reduction_choices[0]
		input_signature_choices = []
		input_signature_LIST_intLlist = [[[0.0, 1.0], [0.0, 0.0]]] 
		input_signature_LIST_intLlist_random = fh.get_int_list(min_length=2, max_length=2,min_int=-255,max_int=255)

		input_signature_LIST_intLlist.append(input_signature_LIST_intLlist_random)
		input_signature_LIST = input_signature_LIST_intLlist[fh.get_int(min_int=0, max_int=len(input_signature_LIST_intLlist)-1)]
		input_signature_choices.append(input_signature_LIST)
		input_signature = input_signature_choices[0]
		arg_class = tf.keras.losses.SquaredHinge(reduction=reduction,)
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
