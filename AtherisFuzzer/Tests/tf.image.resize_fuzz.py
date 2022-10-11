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
		parameter_0 = parameter_0_choices[fh.get_int()%1]
		parameter_1_choices = []
		parameter_1 = parameter_1_choices[fh.get_int()%0]
		method_choices = []
		method_STR_strlist = ['nearest'] 
		method_STR = method_STR_strlist[fh.get_int(min_int=0, max_int=len(method_STR_strlist)]
		method_choices.append(method_STR)
		method = method_choices[fh.get_int()%1]
		preserve_aspect_ratio_choices = []
		preserve_aspect_ratio_STR_strlist = ['true', 'false'] 
		preserve_aspect_ratio_STR = preserve_aspect_ratio_STR_strlist[fh.get_int(min_int=0, max_int=len(preserve_aspect_ratio_STR_strlist)]
		preserve_aspect_ratio_choices.append(preserve_aspect_ratio_STR)
		preserve_aspect_ratio = preserve_aspect_ratio_choices[fh.get_int()%1]
		antialias_choices = []
		antialias_STR_strlist = ['true', 'false'] 
		antialias_STR = antialias_STR_strlist[fh.get_int(min_int=0, max_int=len(antialias_STR_strlist)]
		antialias_choices.append(antialias_STR)
		antialias = antialias_choices[fh.get_int()%1]
		_ = tf.image.resize(parameter_0,parameter_1,method=method,preserve_aspect_ratio=preserve_aspect_ratio,antialias=antialias)
	except Exception as e:
		f.write(str(e) + "\n")
	f.close()
def main():
	atheris.Setup(sys.argv, TestOneInput, enable_python_coverage=True)
	atheris.Fuzz()

if __name__ == "__main__":
	main()
