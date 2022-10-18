#This is a Python API fuzzer for tf.clip_by_value
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.clip_by_value_exception.txt","a")
	try:
		parameter_0_choices = []
		# Tensor generation for parameter_0
		parameter_0_DTYPES = [tf.float32,tf.float64]
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
		clip_value_min_choices = []
		clip_value_min_INT = fh.get_int()
		clip_value_min_choices.append(clip_value_min_INT)
		clip_value_min_LIST = fh.get_int_list(min_length=2, max_length=2)
		clip_value_min_choices.append(clip_value_min_LIST)
		clip_value_min = clip_value_min_choices[fh.get_int()%2]
		clip_value_max_choices = []
		clip_value_max_INT = fh.get_int()
		clip_value_max_choices.append(clip_value_max_INT)
		clip_value_max = clip_value_max_choices[0]
		parameter_1_choices = []
		parameter_1_FLOAT = fh.get_float()
		parameter_1_choices.append(parameter_1_FLOAT)
		parameter_1_INT = fh.get_int()
		parameter_1_choices.append(parameter_1_INT)
		parameter_1 = parameter_1_choices[fh.get_int()%2]
		parameter_2_choices = []
		parameter_2_INT = fh.get_int()
		parameter_2_choices.append(parameter_2_INT)
		parameter_2_FLOAT = fh.get_float()
		parameter_2_choices.append(parameter_2_FLOAT)
		parameter_2 = parameter_2_choices[fh.get_int()%2]
		arg_class = tf.clip_by_value(parameter_0,clip_value_min=clip_value_min,clip_value_max=clip_value_max,parameter_1,parameter_2)
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
