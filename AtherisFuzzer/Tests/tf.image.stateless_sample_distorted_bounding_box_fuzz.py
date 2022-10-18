#This is a Python API fuzzer for tf.image.stateless_sample_distorted_bounding_box
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.image.stateless_sample_distorted_bounding_box_exception.txt","a")
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
		parameter_0 = parameter_0_choices[0]
		bounding_boxes_choices = []
		# Tensor generation for bounding_boxes
		bounding_boxes_DTYPES = [tf.float32]
		int_list = fh.get_int_list(min_length=2,max_length=2)
		min_Val = min(int_list) - 1
		max_Val = max(int_list)
		if min_Val % 2 == 0:
			bounding_boxes_tensor = fh.get_random_numeric_tensor(dtype=fh.get_tf_dtype(allowed_set=bounding_boxes_DTYPES))
		else:
			bounding_boxes_tensor = fh.get_random_numeric_tensor(min_val = min_Val, max_val = max_Val, dtype=fh.get_tf_dtype(allowed_set=bounding_boxes_DTYPES))
		bounding_boxes_tensor = tf.identity(bounding_boxes_tensor)
		bounding_boxes_choices.append(bounding_boxes_tensor)
		bounding_boxes = bounding_boxes_choices[0]
		seed_choices = []
		seed_LIST = fh.get_int_list(min_length=2, max_length=2)
		seed_choices.append(seed_LIST)
		seed = seed_choices[0]
		arg_class = tf.image.stateless_sample_distorted_bounding_box(parameter_0,bounding_boxes=bounding_boxes,seed=seed)
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
