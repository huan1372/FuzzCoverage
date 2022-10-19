#This is a Python API fuzzer for tf.keras.metrics.BinaryAccuracy
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.keras.metrics.BinaryAccuracy_exception.txt","a")
	try:
		threshold_choices = []
		threshold_FLOAT = fh.get_float()
		threshold_choices.append(threshold_FLOAT)
		threshold = threshold_choices[0]
		name_choices = []
		name_STR_strlist = ['my_acc'] 
		name_STR = name_STR_strlist[fh.get_int(min_int=0, max_int=len(name_STR_strlist)-1)]
		name_choices.append(name_STR)
		name = name_choices[0]
		arg_class = tf.keras.metrics.BinaryAccuracy(threshold=threshold,name=name)
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
