#This is a Python API fuzzer for tf.keras.layers.Input
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.keras.layers.Input_exception.txt","a")
	try:
		shape_choices = []
		shape_LIST = fh.get_int_list(min_length=1, max_length=1)
		shape_choices.append(shape_LIST)
		shape_INT = fh.get_int()
		shape_choices.append(shape_INT)
		shape = shape_choices[fh.get_int()%2]
		parameter_0_choices = []
		parameter_0_LIST = fh.get_int_list(min_length=1, max_length=2)
		parameter_0_choices.append(parameter_0_LIST)
		parameter_0 = parameter_0_choices[0]
		dtype_choices = []
		dtype_STR_strlist = ['float32'] 
		dtype_STR = dtype_STR_strlist[fh.get_int(min_int=0, max_int=len(dtype_STR_strlist)-1)]
		dtype_choices.append(dtype_STR)
		dtype_DTYPE_dtypelist = ['tf.float32'] 
		dtype_DTYPE = eval(dtype_DTYPE_dtypelist[fh.get_int(min_int=0, max_int=len(dtype_DTYPE_dtypelist)-1)])
		dtype_choices.append(dtype_DTYPE)
		dtype = dtype_choices[fh.get_int()%2]
		arg_class = tf.keras.layers.Input(shape=shape,parameter_0,dtype=dtype)
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
