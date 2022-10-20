#This is a Python API fuzzer for tf.zeros
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.zeros_exception.txt","a")
	try:
		parameter_0_choices = []
		parameter_0_LIST = fh.get_int_list(min_length=1, max_length=5)
		parameter_0_choices.append(parameter_0_LIST)
		parameter_0_INT = fh.get_int()
		parameter_0_choices.append(parameter_0_INT)
		parameter_0 = parameter_0_choices[fh.get_int()%2]
		parameter_1_choices = []
		parameter_1_DTYPE_dtypelist = ['tf.int32'] 
		parameter_1_DTYPE = eval(parameter_1_DTYPE_dtypelist[fh.get_int(min_int=0, max_int=len(parameter_1_DTYPE_dtypelist)-1)])
		parameter_1_choices.append(parameter_1_DTYPE)
		parameter_1 = parameter_1_choices[0]
		dtype_choices = []
		dtype_DTYPE_dtypelist = ['tf.float32', 'tf.int32'] 
		dtype_DTYPE = eval(dtype_DTYPE_dtypelist[fh.get_int(min_int=0, max_int=len(dtype_DTYPE_dtypelist)-1)])
		dtype_choices.append(dtype_DTYPE)
		dtype = dtype_choices[0]
		shape_choices = []
		shape = shape_choices[fh.get_int()%0]
		arg_class = tf.zeros(parameter_0,parameter_1,dtype=dtype,shape=shape)
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
