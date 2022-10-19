#This is a Python API fuzzer for tf.nn.embedding_lookup
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.nn.embedding_lookup_exception.txt","a")
	try:
		params_choices = []
		# Tensor generation for params
		params_DTYPES = [tf.float32]
		int_list = fh.get_int_list(min_length=2,max_length=2)
		min_Val = min(int_list) - 1
		max_Val = max(int_list)
		if min_Val % 2 == 0:
			params_tensor = fh.get_random_numeric_tensor(dtype=fh.get_tf_dtype(allowed_set=params_DTYPES))
		else:
			params_tensor = fh.get_random_numeric_tensor(min_val = min_Val, max_val = max_Val, dtype=fh.get_tf_dtype(allowed_set=params_DTYPES))
		params_tensor = tf.identity(params_tensor)
		params_choices.append(params_tensor)
		params = params_choices[0]
		ids_choices = []
		# Tensor generation for ids
		ids_DTYPES = [tf.int32]
		int_list = fh.get_int_list(min_length=2,max_length=2)
		min_Val = min(int_list) - 1
		max_Val = max(int_list)
		if min_Val % 2 == 0:
			ids_tensor = fh.get_random_numeric_tensor(dtype=fh.get_tf_dtype(allowed_set=ids_DTYPES))
		else:
			ids_tensor = fh.get_random_numeric_tensor(min_val = min_Val, max_val = max_Val, dtype=fh.get_tf_dtype(allowed_set=ids_DTYPES))
		ids_tensor = tf.identity(ids_tensor)
		ids_choices.append(ids_tensor)
		ids = ids_choices[0]
		arg_class = tf.nn.embedding_lookup(params=params,ids=ids)
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
