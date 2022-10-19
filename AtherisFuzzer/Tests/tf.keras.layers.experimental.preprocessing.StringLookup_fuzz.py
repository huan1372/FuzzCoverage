#This is a Python API fuzzer for tf.keras.layers.experimental.preprocessing.StringLookup
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.keras.layers.experimental.preprocessing.StringLookup_exception.txt","a")
	try:
		vocabulary_choices = []
		vocabulary = vocabulary_choices[fh.get_int()%0]
		mask_token_choices = []
		mask_token_None = None
		mask_token_choices.append(mask_token_None)
		mask_token = mask_token_choices[0]
		invert_choices = []
		invert_BOOL = fh.get_bool()
		invert_choices.append(invert_BOOL)
		invert = invert_choices[0]
		arg_class = tf.keras.layers.experimental.preprocessing.StringLookup(vocabulary=vocabulary,mask_token=mask_token,invert=invert)
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
