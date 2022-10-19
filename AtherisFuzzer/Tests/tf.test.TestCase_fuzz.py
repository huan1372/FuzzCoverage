#This is a Python API fuzzer for tf.test.TestCase
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.test.TestCase_exception.txt","a")
	try:
		parameter_0_choices = []
		parameter_0_STR_strlist = ['test_session'] 
		parameter_0_STR = parameter_0_STR_strlist[fh.get_int(min_int=0, max_int=len(parameter_0_STR_strlist)-1)]
		parameter_0_choices.append(parameter_0_STR)
		parameter_0 = parameter_0_choices[0]
		methodName_choices = []
		methodName_STR_strlist = ['test_session'] 
		methodName_STR = methodName_STR_strlist[fh.get_int(min_int=0, max_int=len(methodName_STR_strlist)-1)]
		methodName_choices.append(methodName_STR)
		methodName = methodName_choices[0]
		arg_class = tf.test.TestCase(parameter_0,methodName=methodName)
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
