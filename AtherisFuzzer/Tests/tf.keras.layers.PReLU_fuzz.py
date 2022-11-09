#This is a Python API fuzzer for tf.keras.layers.PReLU
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.keras.layers.PReLU_exception.txt","a")
	try:
		name_choices = []
		name_STR_strlist = ['', 'same', 'valid', 'p_re_lu', 'sum', 'zeros', '1'] 
		name_STR = name_STR_strlist[fh.get_int(min_int=0, max_int=len(name_STR_strlist)-1)]
		name_choices.append(name_STR)
		name = name_choices[0]
		trainable_choices = []
		trainable_BOOL = fh.get_bool()
		trainable_choices.append(trainable_BOOL)
		trainable = trainable_choices[0]
		batch_input_shape_choices = []
		batch_input_shape_LIST_intLlist = [[2, 3, 4]] 
		batch_input_shape_LIST_intLlist_random = fh.get_int_list(min_length=3, max_length=3,min_int=-255,max_int=255)

		batch_input_shape_LIST_intLlist.append(batch_input_shape_LIST_intLlist_random)
		batch_input_shape_LIST = batch_input_shape_LIST_intLlist[fh.get_int(min_int=0, max_int=len(batch_input_shape_LIST_intLlist)-1)]
		batch_input_shape_choices.append(batch_input_shape_LIST)
		batch_input_shape = batch_input_shape_choices[0]
		dtype_choices = []
		dtype_STR_strlist = ['', 'same', 'valid', 'sum', 'zeros', '1', 'float32'] 
		dtype_STR = dtype_STR_strlist[fh.get_int(min_int=0, max_int=len(dtype_STR_strlist)-1)]
		dtype_choices.append(dtype_STR)
		dtype = dtype_choices[0]
		alpha_initializer_choices = []
		alpha_initializer_STR_strlist = ['', 'Zeros', 'same', 'valid', 'sum', 'zeros', '1'] 
		alpha_initializer_STR = alpha_initializer_STR_strlist[fh.get_int(min_int=0, max_int=len(alpha_initializer_STR_strlist)-1)]
		alpha_initializer_choices.append(alpha_initializer_STR)
		alpha_initializer = alpha_initializer_choices[0]
		alpha_regularizer_choices = []
		alpha_regularizer_None = None
		alpha_regularizer_choices.append(alpha_regularizer_None)
		alpha_regularizer = alpha_regularizer_choices[0]
		alpha_constraint_choices = []
		alpha_constraint_None = None
		alpha_constraint_choices.append(alpha_constraint_None)
		alpha_constraint = alpha_constraint_choices[0]
		shared_axes_choices = []
		shared_axes_None = None
		shared_axes_choices.append(shared_axes_None)
		shared_axes_LIST_intLlist = [[1], [1, 2]] 
		shared_axes_LIST_intLlist_random = fh.get_int_list(min_length=1, max_length=2,min_int=-255,max_int=255)

		shared_axes_LIST_intLlist.append(shared_axes_LIST_intLlist_random)
		shared_axes_LIST = shared_axes_LIST_intLlist[fh.get_int(min_int=0, max_int=len(shared_axes_LIST_intLlist)-1)]
		shared_axes_choices.append(shared_axes_LIST)
		shared_axes_INT_intlist = [1] 
		shared_axes_INT_intlist_random = fh.get_int(min_int=-255,max_int=255)

		shared_axes_INT_intlist.append(shared_axes_INT_intlist_random)
		shared_axes_INT = shared_axes_INT_intlist[fh.get_int(min_int=0, max_int=len(shared_axes_INT_intlist)-1)]
		shared_axes_choices.append(shared_axes_INT)
		shared_axes = shared_axes_choices[fh.get_int()%3]
		input_signature_choices = []
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
		input_signature = input_signature_choices[0]
		arg_class = tf.keras.layers.PReLU(name=name,trainable=trainable,batch_input_shape=batch_input_shape,dtype=dtype,alpha_initializer=alpha_initializer,alpha_regularizer=alpha_regularizer,alpha_constraint=alpha_constraint,shared_axes=shared_axes,)
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
