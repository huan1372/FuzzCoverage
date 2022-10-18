#This is a Python API fuzzer for tf.image.resize
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.image.resize_exception.txt","a")
	try:
		parameter_0_choices = []
		# Tensor generation for parameter_0
		parameter_0_DTYPES = [tf.int32,tf.float32,tf.uint8]
		int_list = fh.get_int_list(min_length=2,max_length=2)
		min_Val = min(int_list) - 1
		max_Val = max(int_list)
		if min_Val % 2 == 0:
			parameter_0_tensor = fh.get_random_numeric_tensor(dtype=fh.get_tf_dtype(allowed_set=parameter_0_DTYPES))
		else:
			parameter_0_tensor = fh.get_random_numeric_tensor(min_val = min_Val, max_val = max_Val, dtype=fh.get_tf_dtype(allowed_set=parameter_0_DTYPES))
		parameter_0_tensor = tf.identity(parameter_0_tensor)
		parameter_0_choices.append(parameter_0_tensor)
		parameter_0 = parameter_0_choices[0]
		parameter_1_choices = []
		parameter_1_LIST = fh.get_int_list(min_length=2, max_length=2)
		parameter_1_choices.append(parameter_1_LIST)
		parameter_1 = parameter_1_choices[0]
		method_choices = []
		method_STR_strlist = ['nearest'] 
		method_STR = method_STR_strlist[fh.get_int(min_int=0, max_int=len(method_STR_strlist)-1)]
		method_choices.append(method_STR)
		method = method_choices[0]
		preserve_aspect_ratio_choices = []
		preserve_aspect_ratio_BOOL = fh.get_bool()
		preserve_aspect_ratio_choices.append(preserve_aspect_ratio_BOOL)
		preserve_aspect_ratio = preserve_aspect_ratio_choices[0]
		antialias_choices = []
		antialias_BOOL = fh.get_bool()
		antialias_choices.append(antialias_BOOL)
		antialias = antialias_choices[0]
		arg_class = tf.image.resize(parameter_0,parameter_1,method=method,preserve_aspect_ratio=preserve_aspect_ratio,antialias=antialias)
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
