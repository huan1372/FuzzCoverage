#This is a Python API fuzzer for tf.metrics.MeanIoU
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.metrics.MeanIoU_exception.txt","a")
	try:
		num_classes_choices = []
		num_classes_INT_intlist = [2] 
		num_classes_INT_intlist_random = fh.get_int(min_int=-255,max_int=255)

		num_classes_INT_intlist.append(num_classes_INT_intlist_random)
		num_classes_INT = num_classes_INT_intlist[fh.get_int(min_int=0, max_int=len(num_classes_INT_intlist)-1)]
		num_classes_choices.append(num_classes_INT)
		num_classes = num_classes_choices[0]
		input_signature_choices = []
		input_signature_LIST_intLlist = [[0, 0, 1, 1]] 
		input_signature_LIST_intLlist_random = fh.get_int_list(min_length=4, max_length=4,min_int=-255,max_int=255)

		input_signature_LIST_intLlist.append(input_signature_LIST_intLlist_random)
		input_signature_LIST = input_signature_LIST_intLlist[fh.get_int(min_int=0, max_int=len(input_signature_LIST_intLlist)-1)]
		input_signature_choices.append(input_signature_LIST)
		# Tensor generation for input_signature
		input_signature_DTYPES = [tf.bfloat16, tf.bool, tf.complex128, tf.complex64, tf.float64, tf.float16, tf.float32, tf.float64, tf.float16, tf.int16, tf.int32, tf.int64, tf.int8, tf.uint8, tf.uint16, tf.uint32, tf.uint64]
		int_list = fh.get_int_list(min_length=2,max_length=2)
		min_Val = min(int_list) - 1
		max_Val = max(int_list)
		if min_Val % 2 == 0:
			input_signature_tensor = fh.get_random_numeric_tensor(dtype=fh.get_tf_dtype(allowed_set=input_signature_DTYPES))
		else:
			input_signature_tensor = fh.get_random_numeric_tensor(min_val = min_Val, max_val = max_Val, dtype=fh.get_tf_dtype(allowed_set=input_signature_DTYPES))
		input_signature_tensor = tf.identity(input_signature_tensor)
		input_signature_choices.append(input_signature_tensor)
		input_signature = input_signature_choices[fh.get_int()%2]
		arg_class = tf.metrics.MeanIoU(num_classes=num_classes,)
		arg_input = [input_signature,]
		final_output = arg_class(*arg_input)
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
