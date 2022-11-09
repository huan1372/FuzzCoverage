#This is a Python API fuzzer for tf.keras.metrics.Mean
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.keras.metrics.Mean_exception.txt","a")
	try:
		name_choices = []
		name_STR_strlist = ['', 'mean_absolute_error', 'zeros', 'min', 'my_mean_tensor', 'same', '1', 'squared_hinge', 'top_k_categorical_accuracy', 'valid', 'sum', 'mean_squared_logarithmic_error', 'max', 'my_mean', 'mean_absolute_percentage_error', 'mean_squared_error', 'poisson'] 
		name_STR = name_STR_strlist[fh.get_int(min_int=0, max_int=len(name_STR_strlist)-1)]
		name_choices.append(name_STR)
		name_None = None
		name_choices.append(name_None)
		name = name_choices[fh.get_int()%2]
		dtype_choices = []
		dtype_DTYPE_dtypelist = ['', 'zeros', 'same', '1', 'valid', 'sum', 'tf.float32', 'tf.float64'] 
		dtype_DTYPE = eval(dtype_DTYPE_dtypelist[fh.get_int(min_int=0, max_int=len(dtype_DTYPE_dtypelist)-1)])
		dtype_choices.append(dtype_DTYPE)
		dtype_None = None
		dtype_choices.append(dtype_None)
		dtype = dtype_choices[fh.get_int()%2]
		parameter_0_choices = []
		parameter_0_STR_strlist = ['', 'zeros', 'same', '1', 'valid', 'sum', 'root_mean_squared_error'] 
		parameter_0_STR = parameter_0_STR_strlist[fh.get_int(min_int=0, max_int=len(parameter_0_STR_strlist)-1)]
		parameter_0_choices.append(parameter_0_STR)
		parameter_0 = parameter_0_choices[0]
		arg_class = tf.keras.metrics.Mean(parameter_0,name=name,dtype=dtype,)
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
