#This is a Python API fuzzer for tf.nn.batch_normalization
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.nn.batch_normalization_exception.txt","a")
	try:
		parameter_0_choices = []
		# Tensor generation for parameter_0
		parameter_0_DTYPES = [tf.float32]
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
		mean_choices = []
		# Tensor generation for mean
		mean_DTYPES = [tf.float32]
		int_list = fh.get_int_list(min_length=2,max_length=2)
		min_Val = min(int_list) - 1
		max_Val = max(int_list)
		if min_Val % 2 == 0:
			mean_tensor = fh.get_random_numeric_tensor(dtype=fh.get_tf_dtype(allowed_set=mean_DTYPES))
		else:
			mean_tensor = fh.get_random_numeric_tensor(min_val = min_Val, max_val = max_Val, dtype=fh.get_tf_dtype(allowed_set=mean_DTYPES))
		mean_tensor = tf.identity(mean_tensor)
		mean_choices.append(mean_tensor)
		mean = mean_choices[0]
		variance_choices = []
		# Tensor generation for variance
		variance_DTYPES = [tf.float32]
		int_list = fh.get_int_list(min_length=2,max_length=2)
		min_Val = min(int_list) - 1
		max_Val = max(int_list)
		if min_Val % 2 == 0:
			variance_tensor = fh.get_random_numeric_tensor(dtype=fh.get_tf_dtype(allowed_set=variance_DTYPES))
		else:
			variance_tensor = fh.get_random_numeric_tensor(min_val = min_Val, max_val = max_Val, dtype=fh.get_tf_dtype(allowed_set=variance_DTYPES))
		variance_tensor = tf.identity(variance_tensor)
		variance_choices.append(variance_tensor)
		variance = variance_choices[0]
		scale_choices = []
		# Tensor generation for scale
		scale_DTYPES = [tf.float32]
		int_list = fh.get_int_list(min_length=2,max_length=2)
		min_Val = min(int_list) - 1
		max_Val = max(int_list)
		if min_Val % 2 == 0:
			scale_tensor = fh.get_random_numeric_tensor(dtype=fh.get_tf_dtype(allowed_set=scale_DTYPES))
		else:
			scale_tensor = fh.get_random_numeric_tensor(min_val = min_Val, max_val = max_Val, dtype=fh.get_tf_dtype(allowed_set=scale_DTYPES))
		scale_tensor = tf.identity(scale_tensor)
		scale_choices.append(scale_tensor)
		scale = scale_choices[0]
		offset_choices = []
		# Tensor generation for offset
		offset_DTYPES = [tf.float32]
		int_list = fh.get_int_list(min_length=2,max_length=2)
		min_Val = min(int_list) - 1
		max_Val = max(int_list)
		if min_Val % 2 == 0:
			offset_tensor = fh.get_random_numeric_tensor(dtype=fh.get_tf_dtype(allowed_set=offset_DTYPES))
		else:
			offset_tensor = fh.get_random_numeric_tensor(min_val = min_Val, max_val = max_Val, dtype=fh.get_tf_dtype(allowed_set=offset_DTYPES))
		offset_tensor = tf.identity(offset_tensor)
		offset_choices.append(offset_tensor)
		offset = offset_choices[0]
		variance_epsilon_choices = []
		variance_epsilon_FLOAT = fh.get_float()
		variance_epsilon_choices.append(variance_epsilon_FLOAT)
		variance_epsilon = variance_epsilon_choices[0]
		arg_class = tf.nn.batch_normalization(parameter_0,mean=mean,variance=variance,scale=scale,offset=offset,variance_epsilon=variance_epsilon)
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
