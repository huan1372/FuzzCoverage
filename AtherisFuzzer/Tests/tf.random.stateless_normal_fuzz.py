#This is a Python API fuzzer for tf.random.stateless_normal
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.random.stateless_normal_exception.txt","a")
	try:
		shape_choices = []
		shape_LIST = fh.get_int_list(min_length=1, max_length=1)
		shape_choices.append(shape_LIST)
		shape = shape_choices[0]
		seed_choices = []
		# Tensor generation for seed
		seed_DTYPES = [tf.int32]
		int_list = fh.get_int_list(min_length=2,max_length=2)
		min_Val = min(int_list) - 1
		max_Val = max(int_list)
		if min_Val % 2 == 0:
			seed_tensor = fh.get_random_numeric_tensor(dtype=fh.get_tf_dtype(allowed_set=seed_DTYPES))
		else:
			seed_tensor = fh.get_random_numeric_tensor(min_val = min_Val, max_val = max_Val, dtype=fh.get_tf_dtype(allowed_set=seed_DTYPES))
		seed_tensor = tf.identity(seed_tensor)
		seed_choices.append(seed_tensor)
		seed = seed_choices[0]
		arg_class = tf.random.stateless_normal(shape=shape,seed=seed)
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
