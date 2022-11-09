#This is a Python API fuzzer for tf.keras.metrics.SparseCategoricalCrossentropy
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.keras.metrics.SparseCategoricalCrossentropy_exception.txt","a")
	try:
		axis_choices = []
		axis_INT_intlist = [0] 
		axis_INT_intlist_random = fh.get_int(min_int=-255,max_int=255)

		axis_INT_intlist.append(axis_INT_intlist_random)
		axis_INT = axis_INT_intlist[fh.get_int(min_int=0, max_int=len(axis_INT_intlist)-1)]
		axis_choices.append(axis_INT)
		axis = axis_choices[0]
		input_signature_choices = []
		input_signature = input_signature_choices[fh.get_int()%0]
		from_logits_choices = []
		from_logits_BOOL = fh.get_bool()
		from_logits_choices.append(from_logits_BOOL)
		from_logits = from_logits_choices[0]
		arg_class = tf.keras.metrics.SparseCategoricalCrossentropy(axis=axis,from_logits=from_logits)
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
