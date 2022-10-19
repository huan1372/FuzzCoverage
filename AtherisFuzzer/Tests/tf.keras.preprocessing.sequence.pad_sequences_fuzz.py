#This is a Python API fuzzer for tf.keras.preprocessing.sequence.pad_sequences
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.keras.preprocessing.sequence.pad_sequences_exception.txt","a")
	try:
		parameter_0_choices = []
		parameter_0_LIST = fh.get_int_list(min_length=3, max_length=3)
		parameter_0_choices.append(parameter_0_LIST)
		parameter_0 = parameter_0_choices[0]
		padding_choices = []
		padding_STR_strlist = ['post'] 
		padding_STR = padding_STR_strlist[fh.get_int(min_int=0, max_int=len(padding_STR_strlist)-1)]
		padding_choices.append(padding_STR)
		padding = padding_choices[0]
		value_choices = []
		value_INT = fh.get_int()
		value_choices.append(value_INT)
		value = value_choices[0]
		maxlen_choices = []
		maxlen_INT = fh.get_int()
		maxlen_choices.append(maxlen_INT)
		maxlen = maxlen_choices[0]
		arg_class = tf.keras.preprocessing.sequence.pad_sequences(parameter_0,padding=padding,value=value,maxlen=maxlen)
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
