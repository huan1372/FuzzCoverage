#This is a Python API fuzzer for tf.config.set_visible_devices
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.config.set_visible_devices_exception.txt","a")
	try:
		parameter_0_choices = []
		parameter_0_LIST = fh.get_int_list(min_length=0, max_length=0)
		parameter_0_choices.append(parameter_0_LIST)
		parameter_0 = parameter_0_choices[0]
		parameter_1_choices = []
		parameter_1_STR_strlist = ['GPU'] 
		parameter_1_STR = parameter_1_STR_strlist[fh.get_int(min_int=0, max_int=len(parameter_1_STR_strlist)-1)]
		parameter_1_choices.append(parameter_1_STR)
		parameter_1 = parameter_1_choices[0]
		arg_class = tf.config.set_visible_devices(parameter_0,parameter_1)
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
