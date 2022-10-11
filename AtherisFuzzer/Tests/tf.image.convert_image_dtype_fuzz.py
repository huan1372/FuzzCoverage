#This is a Python API fuzzer for tf.image.convert_image_dtype
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.image.convert_image_dtype_exception.txt","a")
	try:
		parameter_0_choices = []
		# Tensor generation for parameter_0
		parameter_0_DTYPES = [tf.uint8]
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
		dtype_choices = []
		dtype = dtype_choices[fh.get_int()%0]
		saturate_choices = []
		saturate_STR_strlist = ['false'] 
		saturate_STR = saturate_STR_strlist[fh.get_int(min_int=0, max_int=len(saturate_STR_strlist)]
		saturate_choices.append(saturate_STR)
		saturate = saturate_choices[fh.get_int()%1]
		parameter_1_choices = []
		parameter_1 = parameter_1_choices[fh.get_int()%0]
		_ = tf.image.convert_image_dtype(parameter_0,dtype=dtype,saturate=saturate,parameter_1)
	except Exception as e:
		f.write(str(e) + "\n")
	f.close()
def main():
	atheris.Setup(sys.argv, TestOneInput, enable_python_coverage=True)
	atheris.Fuzz()

if __name__ == "__main__":
	main()
