#This is a Python API fuzzer for tf.metrics.Mean
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.metrics.Mean_exception.txt","a")
	try:
		name_choices = []
		name_STR_strlist = ['my_mean', 'my_mean_tensor', 'max', 'min'] 
		name_STR = name_STR_strlist[fh.get_int(min_int=0, max_int=len(name_STR_strlist)-1)]
		name_choices.append(name_STR)
		name_None = None
		name_choices.append(name_None)
		name = name_choices[fh.get_int()%2]
		dtype_choices = []
		dtype_DTYPE_dtypelist = ['tf.float32', 'tf.float64'] 
		dtype_DTYPE = eval(dtype_DTYPE_dtypelist[fh.get_int(min_int=0, max_int=len(dtype_DTYPE_dtypelist)-1)])
		dtype_choices.append(dtype_DTYPE)
		dtype_None = None
		dtype_choices.append(dtype_None)
		dtype = dtype_choices[fh.get_int()%2]
		arg_class = tf.metrics.Mean(name=name,dtype=dtype)
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
