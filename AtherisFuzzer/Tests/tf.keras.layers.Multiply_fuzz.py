#This is a Python API fuzzer for tf.keras.layers.Multiply
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.keras.layers.Multiply_exception.txt","a")
	try:
		input_signature_choices = []
		input_signature_LIST_intLlist = [[{'Label': 'tensor', 'dtype': 'float32', 'shape': [5, 8]}, {'Label': 'tensor', 'dtype': 'float32', 'shape': [5, 8]}]] 
		input_signature_LIST_intLlist_random = fh.get_int_list(min_length=2, max_length=2,min_int=-255,max_int=255)

		input_signature_LIST_intLlist.append(input_signature_LIST_intLlist_random)
		input_signature_LIST = input_signature_LIST_intLlist[fh.get_int(min_int=0, max_int=len(input_signature_LIST_intLlist)-1)]
		input_signature_choices.append(input_signature_LIST)
		input_signature = input_signature_choices[0]
		arg_class = tf.keras.layers.Multiply()
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
