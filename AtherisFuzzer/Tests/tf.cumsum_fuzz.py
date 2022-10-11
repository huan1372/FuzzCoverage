#This is a Python API fuzzer for tf.cumsum
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.cumsum_exception.txt","a")
	try:
		parameter_0_choices = []
		# Tensor generation for parameter_0
		parameter_0_DTYPES = [tf.int32]
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
		exclusive_choices = []
		exclusive_STR_strlist = ['true', 'false'] 
		exclusive_STR = exclusive_STR_strlist[fh.get_int(min_int=0, max_int=len(exclusive_STR_strlist)]
		exclusive_choices.append(exclusive_STR)
		exclusive = exclusive_choices[fh.get_int()%1]
		reverse_choices = []
		reverse_STR_strlist = ['true', 'false'] 
		reverse_STR = reverse_STR_strlist[fh.get_int(min_int=0, max_int=len(reverse_STR_strlist)]
		reverse_choices.append(reverse_STR)
		reverse = reverse_choices[fh.get_int()%1]
		axis_choices = []
		axis_INT = fh.get_int()
		axis_choices.append(axis_INT)
		axis = axis_choices[fh.get_int()%1]
		_ = tf.cumsum(parameter_0,exclusive=exclusive,reverse=reverse,axis=axis)
	except Exception as e:
		f.write(str(e) + "\n")
	f.close()
def main():
	atheris.Setup(sys.argv, TestOneInput, enable_python_coverage=True)
	atheris.Fuzz()

if __name__ == "__main__":
	main()
