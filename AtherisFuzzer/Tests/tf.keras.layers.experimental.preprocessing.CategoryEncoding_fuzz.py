#This is a Python API fuzzer for tf.keras.layers.experimental.preprocessing.CategoryEncoding
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.keras.layers.experimental.preprocessing.CategoryEncoding_exception.txt","a")
	try:
		max_tokens_choices = []
		max_tokens_INT = fh.get_int()
		max_tokens_choices.append(max_tokens_INT)
		max_tokens = max_tokens_choices[0]
		output_mode_choices = []
		output_mode_STR_strlist = ['count'] 
		output_mode_STR = output_mode_STR_strlist[fh.get_int(min_int=0, max_int=len(output_mode_STR_strlist)-1)]
		output_mode_choices.append(output_mode_STR)
		output_mode = output_mode_choices[0]
		arg_class = tf.keras.layers.experimental.preprocessing.CategoryEncoding(max_tokens=max_tokens,output_mode=output_mode)
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
