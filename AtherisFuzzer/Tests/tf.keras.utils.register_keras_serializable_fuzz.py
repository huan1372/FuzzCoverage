#This is a Python API fuzzer for tf.keras.utils.register_keras_serializable
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.keras.utils.register_keras_serializable_exception.txt","a")
	try:
		package_choices = []
		package_STR_strlist = ['Addons', 'Custom'] 
		package_STR = package_STR_strlist[fh.get_int(min_int=0, max_int=len(package_STR_strlist)-1)]
		package_choices.append(package_STR)
		package = package_choices[0]
		name_choices = []
		name_STR_strlist = ['l1', 'l2'] 
		name_STR = name_STR_strlist[fh.get_int(min_int=0, max_int=len(name_STR_strlist)-1)]
		name_choices.append(name_STR)
		name = name_choices[0]
		arg_class = tf.keras.utils.register_keras_serializable(package=package,name=name)
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
