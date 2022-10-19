#This is a Python API fuzzer for tf.random.stateless_parameterized_truncated_normal
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.random.stateless_parameterized_truncated_normal_exception.txt","a")
	try:
		shape_choices = []
		shape_LIST = fh.get_int_list(min_length=3, max_length=3)
		shape_choices.append(shape_LIST)
		shape = shape_choices[0]
		seed_choices = []
		seed_LIST = fh.get_int_list(min_length=2, max_length=2)
		seed_choices.append(seed_LIST)
		seed = seed_choices[0]
		means_choices = []
		means_INT = fh.get_int()
		means_choices.append(means_INT)
		means = means_choices[0]
		stddevs_choices = []
		# Tensor generation for stddevs
		stddevs_DTYPES = [tf.float32]
		int_list = fh.get_int_list(min_length=2,max_length=2)
		min_Val = min(int_list) - 1
		max_Val = max(int_list)
		if min_Val % 2 == 0:
			stddevs_tensor = fh.get_random_numeric_tensor(dtype=fh.get_tf_dtype(allowed_set=stddevs_DTYPES))
		else:
			stddevs_tensor = fh.get_random_numeric_tensor(min_val = min_Val, max_val = max_Val, dtype=fh.get_tf_dtype(allowed_set=stddevs_DTYPES))
		stddevs_tensor = tf.identity(stddevs_tensor)
		stddevs_choices.append(stddevs_tensor)
		stddevs = stddevs_choices[0]
		minvals_choices = []
		minvals_LIST = fh.get_int_list(min_length=3, max_length=3)
		minvals_choices.append(minvals_LIST)
		minvals = minvals_choices[0]
		maxvals_choices = []
		maxvals_LIST = fh.get_int_list(min_length=2, max_length=2)
		maxvals_choices.append(maxvals_LIST)
		maxvals = maxvals_choices[0]
		arg_class = tf.random.stateless_parameterized_truncated_normal(shape=shape,seed=seed,means=means,stddevs=stddevs,minvals=minvals,maxvals=maxvals)
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
