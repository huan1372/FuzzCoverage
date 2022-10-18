#This is a Python API fuzzer for tf.keras.applications.EfficientNetB1
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.keras.applications.EfficientNetB1_exception.txt","a")
	try:
		weights_choices = []
		weights_STR_strlist = ['imagenet'] 
		weights_STR = weights_STR_strlist[fh.get_int(min_int=0, max_int=len(weights_STR_strlist)-1)]
		weights_choices.append(weights_STR)
		weights = weights_choices[0]
		arg_class = tf.keras.applications.EfficientNetB1(weights=weights)
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
