#This is a Python API fuzzer for tf.random.normal
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.random.normal_exception.txt","a")
	try:
		shape_choices = []
		shape_LIST = fh.get_int_list(min_length=1, max_length=4)
		shape_choices.append(shape_LIST)
		shape = shape_choices[0]
		parameter_0_choices = []
		parameter_0_LIST = fh.get_int_list(min_length=1, max_length=6)
		parameter_0_choices.append(parameter_0_LIST)
		parameter_0 = parameter_0_choices[0]
		parameter_1_choices = []
		parameter_1_INT = fh.get_int()
		parameter_1_choices.append(parameter_1_INT)
		parameter_1 = parameter_1_choices[0]
		parameter_2_choices = []
		parameter_2_INT = fh.get_int()
		parameter_2_choices.append(parameter_2_INT)
		parameter_2 = parameter_2_choices[0]
		parameter_3_choices = []
		parameter_3_DTYPE_dtypelist = ['tf.float32'] 
		parameter_3_DTYPE = eval(parameter_3_DTYPE_dtypelist[fh.get_int(min_int=0, max_int=len(parameter_3_DTYPE_dtypelist)-1)])
		parameter_3_choices.append(parameter_3_DTYPE)
		parameter_3 = parameter_3_choices[0]
		seed_choices = []
		seed_INT = fh.get_int()
		seed_choices.append(seed_INT)
		seed = seed_choices[0]
		dtype_choices = []
		dtype_DTYPE_dtypelist = ['tf.float32'] 
		dtype_DTYPE = eval(dtype_DTYPE_dtypelist[fh.get_int(min_int=0, max_int=len(dtype_DTYPE_dtypelist)-1)])
		dtype_choices.append(dtype_DTYPE)
		dtype = dtype_choices[0]
		arg_class = tf.random.normal(shape=shape,parameter_0,parameter_1,parameter_2,parameter_3,seed=seed,dtype=dtype)
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
