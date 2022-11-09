#This is a Python API fuzzer for tf.keras.layers.SimpleRNN
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.keras.layers.SimpleRNN_exception.txt","a")
	try:
		name_choices = []
		name_STR_strlist = ['', 'simple_rnn_2', 'same', 'valid', 'simple_rnn', 'sum', 'zeros', '1', 'simple_rnn_1'] 
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
		dtype_STR_strlist = ['', 'same', 'float64', 'valid', 'sum', 'zeros', '1', 'float32'] 
		dtype_STR = dtype_STR_strlist[fh.get_int(min_int=0, max_int=len(dtype_STR_strlist)-1)]
		dtype_choices.append(dtype_STR)
		dtype = dtype_choices[0]
		return_sequences_choices = []
		return_sequences_BOOL = fh.get_bool()
		return_sequences_choices.append(return_sequences_BOOL)
		return_sequences = return_sequences_choices[0]
		return_state_choices = []
		return_state_BOOL = fh.get_bool()
		return_state_choices.append(return_state_BOOL)
		return_state = return_state_choices[0]
		go_backwards_choices = []
		go_backwards_BOOL = fh.get_bool()
		go_backwards_choices.append(go_backwards_BOOL)
		go_backwards = go_backwards_choices[0]
		stateful_choices = []
		stateful_BOOL = fh.get_bool()
		stateful_choices.append(stateful_BOOL)
		stateful = stateful_choices[0]
		unroll_choices = []
		unroll_BOOL = fh.get_bool()
		unroll_choices.append(unroll_BOOL)
		unroll = unroll_choices[0]
		time_major_choices = []
		time_major_BOOL = fh.get_bool()
		time_major_choices.append(time_major_BOOL)
		time_major = time_major_choices[0]
		units_choices = []
		units_INT_intlist = [2, 5] 
		units_INT_intlist_random = fh.get_int(min_int=-255,max_int=255)

		units_INT_intlist.append(units_INT_intlist_random)
		units_INT = units_INT_intlist[fh.get_int(min_int=0, max_int=len(units_INT_intlist)-1)]
		units_choices.append(units_INT)
		units = units_choices[0]
		activation_choices = []
		activation_STR_strlist = ['', 'same', 'valid', 'sum', 'tanh', 'zeros', '1'] 
		activation_STR = activation_STR_strlist[fh.get_int(min_int=0, max_int=len(activation_STR_strlist)-1)]
		activation_choices.append(activation_STR)
		activation = activation_choices[0]
		use_bias_choices = []
		use_bias_BOOL = fh.get_bool()
		use_bias_choices.append(use_bias_BOOL)
		use_bias = use_bias_choices[0]
		kernel_initializer_choices = []
		kernel_initializer_STR_strlist = ['', 'same', 'GlorotUniform', 'ones', 'valid', 'sum', 'zeros', '1'] 
		kernel_initializer_STR = kernel_initializer_STR_strlist[fh.get_int(min_int=0, max_int=len(kernel_initializer_STR_strlist)-1)]
		kernel_initializer_choices.append(kernel_initializer_STR)
		kernel_initializer = kernel_initializer_choices[0]
		recurrent_initializer_choices = []
		recurrent_initializer_STR_strlist = ['', 'same', 'valid', 'sum', 'Orthogonal', 'zeros', '1'] 
		recurrent_initializer_STR = recurrent_initializer_STR_strlist[fh.get_int(min_int=0, max_int=len(recurrent_initializer_STR_strlist)-1)]
		recurrent_initializer_choices.append(recurrent_initializer_STR)
		recurrent_initializer = recurrent_initializer_choices[0]
		bias_initializer_choices = []
		bias_initializer_STR_strlist = ['', 'Zeros', 'same', 'valid', 'sum', 'zeros', '1'] 
		bias_initializer_STR = bias_initializer_STR_strlist[fh.get_int(min_int=0, max_int=len(bias_initializer_STR_strlist)-1)]
		bias_initializer_choices.append(bias_initializer_STR)
		bias_initializer = bias_initializer_choices[0]
		kernel_regularizer_choices = []
		kernel_regularizer_None = None
		kernel_regularizer_choices.append(kernel_regularizer_None)
		kernel_regularizer = kernel_regularizer_choices[0]
		recurrent_regularizer_choices = []
		recurrent_regularizer_None = None
		recurrent_regularizer_choices.append(recurrent_regularizer_None)
		recurrent_regularizer = recurrent_regularizer_choices[0]
		bias_regularizer_choices = []
		bias_regularizer_None = None
		bias_regularizer_choices.append(bias_regularizer_None)
		bias_regularizer = bias_regularizer_choices[0]
		activity_regularizer_choices = []
		activity_regularizer_None = None
		activity_regularizer_choices.append(activity_regularizer_None)
		activity_regularizer = activity_regularizer_choices[0]
		kernel_constraint_choices = []
		kernel_constraint_None = None
		kernel_constraint_choices.append(kernel_constraint_None)
		kernel_constraint = kernel_constraint_choices[0]
		recurrent_constraint_choices = []
		recurrent_constraint_None = None
		recurrent_constraint_choices.append(recurrent_constraint_None)
		recurrent_constraint = recurrent_constraint_choices[0]
		bias_constraint_choices = []
		bias_constraint_None = None
		bias_constraint_choices.append(bias_constraint_None)
		bias_constraint = bias_constraint_choices[0]
		dropout_choices = []
		dropout_INT_intlist = [0] 
		dropout_INT_intlist_random = fh.get_int(min_int=-255,max_int=255)

		dropout_INT_intlist.append(dropout_INT_intlist_random)
		dropout_INT = dropout_INT_intlist[fh.get_int(min_int=0, max_int=len(dropout_INT_intlist)-1)]
		dropout_choices.append(dropout_INT)
		dropout_FLOAT_floatlist = [0.1, 0.5] 
		dropout_FLOAT_floatlist_random = fh.get_float(min_float=-255,max_float=255)

		dropout_FLOAT_floatlist.append(dropout_FLOAT_floatlist_random)
		dropout_FLOAT = dropout_FLOAT_floatlist[fh.get_int(min_int=0, max_int=len(dropout_FLOAT_floatlist)-1)]
		dropout_choices.append(dropout_FLOAT)
		dropout = dropout_choices[fh.get_int()%2]
		recurrent_dropout_choices = []
		recurrent_dropout_INT_intlist = [0] 
		recurrent_dropout_INT_intlist_random = fh.get_int(min_int=-255,max_int=255)

		recurrent_dropout_INT_intlist.append(recurrent_dropout_INT_intlist_random)
		recurrent_dropout_INT = recurrent_dropout_INT_intlist[fh.get_int(min_int=0, max_int=len(recurrent_dropout_INT_intlist)-1)]
		recurrent_dropout_choices.append(recurrent_dropout_INT)
		recurrent_dropout_FLOAT_floatlist = [0.1] 
		recurrent_dropout_FLOAT_floatlist_random = fh.get_float(min_float=-255,max_float=255)

		recurrent_dropout_FLOAT_floatlist.append(recurrent_dropout_FLOAT_floatlist_random)
		recurrent_dropout_FLOAT = recurrent_dropout_FLOAT_floatlist[fh.get_int(min_int=0, max_int=len(recurrent_dropout_FLOAT_floatlist)-1)]
		recurrent_dropout_choices.append(recurrent_dropout_FLOAT)
		recurrent_dropout = recurrent_dropout_choices[fh.get_int()%2]
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
		implementation_choices = []
		implementation_INT_intlist = [0, 1, 2] 
		implementation_INT_intlist_random = fh.get_int(min_int=-255,max_int=255)

		implementation_INT_intlist.append(implementation_INT_intlist_random)
		implementation_INT = implementation_INT_intlist[fh.get_int(min_int=0, max_int=len(implementation_INT_intlist)-1)]
		implementation_choices.append(implementation_INT)
		implementation = implementation_choices[0]
		parameter_0_choices = []
		parameter_0_INT_intlist = [2, 3] 
		parameter_0_INT_intlist_random = fh.get_int(min_int=-255,max_int=255)

		parameter_0_INT_intlist.append(parameter_0_INT_intlist_random)
		parameter_0_INT = parameter_0_INT_intlist[fh.get_int(min_int=0, max_int=len(parameter_0_INT_intlist)-1)]
		parameter_0_choices.append(parameter_0_INT)
		parameter_0 = parameter_0_choices[0]
		input_shape_choices = []
		input_shape_LIST_intLlist = [[None, 4]] 
		input_shape_LIST_intLlist_random = fh.get_int_list(min_length=2, max_length=2,min_int=-255,max_int=255)

		input_shape_LIST_intLlist.append(input_shape_LIST_intLlist_random)
		input_shape_LIST = input_shape_LIST_intLlist[fh.get_int(min_int=0, max_int=len(input_shape_LIST_intLlist)-1)]
		input_shape_choices.append(input_shape_LIST)
		input_shape = input_shape_choices[0]
		weights_choices = []
		weights_None = None
		weights_choices.append(weights_None)
		weights = weights_choices[0]
		arg_class = tf.keras.layers.SimpleRNN(parameter_0,name=name,trainable=trainable,batch_input_shape=batch_input_shape,dtype=dtype,return_sequences=return_sequences,return_state=return_state,go_backwards=go_backwards,stateful=stateful,unroll=unroll,time_major=time_major,units=units,activation=activation,use_bias=use_bias,kernel_initializer=kernel_initializer,recurrent_initializer=recurrent_initializer,bias_initializer=bias_initializer,kernel_regularizer=kernel_regularizer,recurrent_regularizer=recurrent_regularizer,bias_regularizer=bias_regularizer,activity_regularizer=activity_regularizer,kernel_constraint=kernel_constraint,recurrent_constraint=recurrent_constraint,bias_constraint=bias_constraint,dropout=dropout,recurrent_dropout=recurrent_dropout,implementation=implementation,input_shape=input_shape,weights=weights)
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
