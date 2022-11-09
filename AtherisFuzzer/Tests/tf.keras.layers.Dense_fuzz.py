#This is a Python API fuzzer for tf.keras.layers.Dense
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.keras.layers.Dense_exception.txt","a")
	try:
		parameter_0_choices = []
		parameter_0_INT_intlist = [1024, 1, 2, 128, 4, 5, 3, 4096, 8, 512, 10, 16, 20, 21, 768, 32, 50, 64, 320, 81, 100, 1000, 501] 
		parameter_0_INT_intlist_random = fh.get_int(min_int=-255,max_int=255)

		parameter_0_INT_intlist.append(parameter_0_INT_intlist_random)
		parameter_0_INT = parameter_0_INT_intlist[fh.get_int(min_int=0, max_int=len(parameter_0_INT_intlist)-1)]
		parameter_0_choices.append(parameter_0_INT)
		parameter_0 = parameter_0_choices[0]
		input_dim_choices = []
		input_dim_INT_intlist = [5] 
		input_dim_INT_intlist_random = fh.get_int(min_int=-255,max_int=255)

		input_dim_INT_intlist.append(input_dim_INT_intlist_random)
		input_dim_INT = input_dim_INT_intlist[fh.get_int(min_int=0, max_int=len(input_dim_INT_intlist)-1)]
		input_dim_choices.append(input_dim_INT)
		input_dim = input_dim_choices[0]
		kernel_initializer_choices = []
		kernel_initializer_STR_strlist = ['', 'same', 'GlorotUniform', 'ones', 'valid', 'sum', 'VarianceScaling', 'glorot_normal', 'zeros', '1'] 
		kernel_initializer_STR = kernel_initializer_STR_strlist[fh.get_int(min_int=0, max_int=len(kernel_initializer_STR_strlist)-1)]
		kernel_initializer_choices.append(kernel_initializer_STR)
		kernel_initializer_None = None
		kernel_initializer_choices.append(kernel_initializer_None)
		kernel_initializer_TF_OBJECT_tfobjlist = ['', 'same', 'valid', 'TruncatedNormal', 'sum', 'zeros', '1'] 
		kernel_initializer_TF_OBJECT = eval("tf.keras.initializers." + {strListName}[fh.get_int(min_int=0, max_int=len({strListName})-1)])
		kernel_initializer_choices.append(kernel_initializer_TF_OBJECT)
		kernel_initializer = kernel_initializer_choices[fh.get_int()%3]
		kernel_regularizer_choices = []
		kernel_regularizer_None = None
		kernel_regularizer_choices.append(kernel_regularizer_None)
		kernel_regularizer_STR_strlist = ['', 'same', 'valid', 'sum', 'l1', 'zeros', '1'] 
		kernel_regularizer_STR = kernel_regularizer_STR_strlist[fh.get_int(min_int=0, max_int=len(kernel_regularizer_STR_strlist)-1)]
		kernel_regularizer_choices.append(kernel_regularizer_STR)
		kernel_regularizer = kernel_regularizer_choices[fh.get_int()%2]
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
		activation_choices = []
		activation_STR_strlist = ['', 'same', 'valid', 'sum', 'relu', 'softplus', 'sigmoid', 'softmax', 'tanh', 'zeros', '1', 'linear'] 
		activation_STR = activation_STR_strlist[fh.get_int(min_int=0, max_int=len(activation_STR_strlist)-1)]
		activation_choices.append(activation_STR)
		activation_None = None
		activation_choices.append(activation_None)
		activation = activation_choices[fh.get_int()%2]
		activity_regularizer_choices = []
		activity_regularizer_STR_strlist = ['', 'same', 'valid', 'sum', 'zeros', '1', 'l2'] 
		activity_regularizer_STR = activity_regularizer_STR_strlist[fh.get_int(min_int=0, max_int=len(activity_regularizer_STR_strlist)-1)]
		activity_regularizer_choices.append(activity_regularizer_STR)
		activity_regularizer_None = None
		activity_regularizer_choices.append(activity_regularizer_None)
		activity_regularizer = activity_regularizer_choices[fh.get_int()%2]
		input_shape_choices = []
		input_shape_LIST_intLlist = [[16], [3], [32], [5]] 
		input_shape_LIST_intLlist_random = fh.get_int_list(min_length=1, max_length=1,min_int=-255,max_int=255)

		input_shape_LIST_intLlist.append(input_shape_LIST_intLlist_random)
		input_shape_LIST = input_shape_LIST_intLlist[fh.get_int(min_int=0, max_int=len(input_shape_LIST_intLlist)-1)]
		input_shape_choices.append(input_shape_LIST)
		input_shape = input_shape_choices[0]
		name_choices = []
		name_STR_strlist = ['', 'same', 'valid', 'sum', 'dense', 'out', 'dense_2', 'dense_1', 'predictions', 'dense_3', 'zeros', '1'] 
		name_STR = name_STR_strlist[fh.get_int(min_int=0, max_int=len(name_STR_strlist)-1)]
		name_choices.append(name_STR)
		name_None = None
		name_choices.append(name_None)
		name = name_choices[fh.get_int()%2]
		trainable_choices = []
		trainable_BOOL = fh.get_bool()
		trainable_choices.append(trainable_BOOL)
		trainable = trainable_choices[0]
		batch_input_shape_choices = []
		batch_input_shape_LIST_intLlist = [[None, 3], [3, 2], [3, 4, 5, 2], [3, 4, 2], [None, None, 2]] 
		batch_input_shape_LIST_intLlist_random = fh.get_int_list(min_length=2, max_length=4,min_int=-255,max_int=255)

		batch_input_shape_LIST_intLlist.append(batch_input_shape_LIST_intLlist_random)
		batch_input_shape_LIST = batch_input_shape_LIST_intLlist[fh.get_int(min_int=0, max_int=len(batch_input_shape_LIST_intLlist)-1)]
		batch_input_shape_choices.append(batch_input_shape_LIST)
		batch_input_shape = batch_input_shape_choices[0]
		dtype_choices = []
		dtype_STR_strlist = ['', 'same', 'valid', 'sum', 'zeros', '1', 'float32'] 
		dtype_STR = dtype_STR_strlist[fh.get_int(min_int=0, max_int=len(dtype_STR_strlist)-1)]
		dtype_choices.append(dtype_STR)
		dtype_DTYPE_dtypelist = ['', 'same', 'valid', 'sum', 'tf.float32', 'tf.float64', 'zeros', '1'] 
		dtype_DTYPE = eval(dtype_DTYPE_dtypelist[fh.get_int(min_int=0, max_int=len(dtype_DTYPE_dtypelist)-1)])
		dtype_choices.append(dtype_DTYPE)
		dtype = dtype_choices[fh.get_int()%2]
		units_choices = []
		units_INT_intlist = [256, 1, 2, 3, 4, 5, 320, 10] 
		units_INT_intlist_random = fh.get_int(min_int=-255,max_int=255)

		units_INT_intlist.append(units_INT_intlist_random)
		units_INT = units_INT_intlist[fh.get_int(min_int=0, max_int=len(units_INT_intlist)-1)]
		units_choices.append(units_INT)
		units = units_choices[0]
		use_bias_choices = []
		use_bias_BOOL = fh.get_bool()
		use_bias_choices.append(use_bias_BOOL)
		use_bias = use_bias_choices[0]
		bias_initializer_choices = []
		bias_initializer_STR_strlist = ['', 'Zeros', 'same', 'valid', 'sum', 'zeros', '1'] 
		bias_initializer_STR = bias_initializer_STR_strlist[fh.get_int(min_int=0, max_int=len(bias_initializer_STR_strlist)-1)]
		bias_initializer_choices.append(bias_initializer_STR)
		bias_initializer = bias_initializer_choices[0]
		bias_regularizer_choices = []
		bias_regularizer_None = None
		bias_regularizer_choices.append(bias_regularizer_None)
		bias_regularizer = bias_regularizer_choices[0]
		kernel_constraint_choices = []
		kernel_constraint_None = None
		kernel_constraint_choices.append(kernel_constraint_None)
		kernel_constraint = kernel_constraint_choices[0]
		bias_constraint_choices = []
		bias_constraint_None = None
		bias_constraint_choices.append(bias_constraint_None)
		bias_constraint = bias_constraint_choices[0]
		arg_class = tf.keras.layers.Dense(parameter_0,input_dim=input_dim,kernel_initializer=kernel_initializer,kernel_regularizer=kernel_regularizer,activation=activation,activity_regularizer=activity_regularizer,input_shape=input_shape,name=name,trainable=trainable,batch_input_shape=batch_input_shape,dtype=dtype,units=units,use_bias=use_bias,bias_initializer=bias_initializer,bias_regularizer=bias_regularizer,kernel_constraint=kernel_constraint,bias_constraint=bias_constraint)
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
