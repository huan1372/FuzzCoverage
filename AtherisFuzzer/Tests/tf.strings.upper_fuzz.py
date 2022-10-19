#This is a Python API fuzzer for tf.strings.upper
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.strings.upper_exception.txt","a")
	try:
		parameter_0_choices = []
		parameter_0_STR_strlist = ['CamelCase string and ALL CAPS'] 
		parameter_0_STR = parameter_0_STR_strlist[fh.get_int(min_int=0, max_int=len(parameter_0_STR_strlist)-1)]
		parameter_0_choices.append(parameter_0_STR)
		parameter_0 = parameter_0_choices[0]
		arg_class = tf.strings.upper(parameter_0)
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
