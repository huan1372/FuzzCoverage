#This is a Python API fuzzer for tf.keras.layers.ConvLSTM2D
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.keras.layers.ConvLSTM2D_exception.txt","a")
	try:
		data_format_choices = []
		data_format_STR_strlist = ['channels_first', 'channels_last'] 
		data_format_STR = data_format_STR_strlist[fh.get_int(min_int=0, max_int=len(data_format_STR_strlist)-1)]
		data_format_choices.append(data_format_STR)
		data_format = data_format_choices[0]
		return_sequences_choices = []
		return_sequences_BOOL = fh.get_bool()
		return_sequences_choices.append(return_sequences_BOOL)
		return_sequences = return_sequences_choices[0]
		return_state_choices = []
		return_state_BOOL = fh.get_bool()
		return_state_choices.append(return_state_BOOL)
		return_state = return_state_choices[0]
		stateful_choices = []
		stateful_BOOL = fh.get_bool()
		stateful_choices.append(stateful_BOOL)
		stateful = stateful_choices[0]
		filters_choices = []
		filters_INT = fh.get_int()
		filters_choices.append(filters_INT)
		filters = filters_choices[0]
		kernel_size_choices = []
		kernel_size_LIST = fh.get_int_list(min_length=2, max_length=2)
		kernel_size_choices.append(kernel_size_LIST)
		kernel_size = kernel_size_choices[0]
		padding_choices = []
		padding_STR_strlist = ['valid', 'same'] 
		padding_STR = padding_STR_strlist[fh.get_int(min_int=0, max_int=len(padding_STR_strlist)-1)]
		padding_choices.append(padding_STR)
		padding = padding_choices[0]
		name_choices = []
		name_STR_strlist = ['conv_lst_m2d_1', 'conv_lst_m2d'] 
		name_STR = name_STR_strlist[fh.get_int(min_int=0, max_int=len(name_STR_strlist)-1)]
		name_choices.append(name_STR)
		name = name_choices[0]
		trainable_choices = []
		trainable_BOOL = fh.get_bool()
		trainable_choices.append(trainable_BOOL)
		trainable = trainable_choices[0]
		batch_input_shape_choices = []
		batch_input_shape_LIST = fh.get_int_list(min_length=5, max_length=5)
		batch_input_shape_choices.append(batch_input_shape_LIST)
		batch_input_shape = batch_input_shape_choices[0]
		dtype_choices = []
		dtype_STR_strlist = ['float32'] 
		dtype_STR = dtype_STR_strlist[fh.get_int(min_int=0, max_int=len(dtype_STR_strlist)-1)]
		dtype_choices.append(dtype_STR)
		dtype = dtype_choices[0]
		go_backwards_choices = []
		go_backwards_BOOL = fh.get_bool()
		go_backwards_choices.append(go_backwards_BOOL)
		go_backwards = go_backwards_choices[0]
		unroll_choices = []
		unroll_BOOL = fh.get_bool()
		unroll_choices.append(unroll_BOOL)
		unroll = unroll_choices[0]
		time_major_choices = []
		time_major_BOOL = fh.get_bool()
		time_major_choices.append(time_major_BOOL)
		time_major = time_major_choices[0]
		strides_choices = []
		strides_LIST = fh.get_int_list(min_length=2, max_length=2)
		strides_choices.append(strides_LIST)
		strides = strides_choices[0]
		dilation_rate_choices = []
		dilation_rate_LIST = fh.get_int_list(min_length=2, max_length=2)
		dilation_rate_choices.append(dilation_rate_LIST)
		dilation_rate = dilation_rate_choices[0]
		activation_choices = []
		activation_STR_strlist = ['tanh'] 
		activation_STR = activation_STR_strlist[fh.get_int(min_int=0, max_int=len(activation_STR_strlist)-1)]
		activation_choices.append(activation_STR)
		activation = activation_choices[0]
		recurrent_activation_choices = []
		recurrent_activation_STR_strlist = ['hard_sigmoid'] 
		recurrent_activation_STR = recurrent_activation_STR_strlist[fh.get_int(min_int=0, max_int=len(recurrent_activation_STR_strlist)-1)]
		recurrent_activation_choices.append(recurrent_activation_STR)
		recurrent_activation = recurrent_activation_choices[0]
		use_bias_choices = []
		use_bias_BOOL = fh.get_bool()
		use_bias_choices.append(use_bias_BOOL)
		use_bias = use_bias_choices[0]
		kernel_initializer_choices = []
		kernel_initializer_STR_strlist = ['GlorotUniform'] 
		kernel_initializer_STR = kernel_initializer_STR_strlist[fh.get_int(min_int=0, max_int=len(kernel_initializer_STR_strlist)-1)]
		kernel_initializer_choices.append(kernel_initializer_STR)
		kernel_initializer = kernel_initializer_choices[0]
		recurrent_initializer_choices = []
		recurrent_initializer_STR_strlist = ['Orthogonal'] 
		recurrent_initializer_STR = recurrent_initializer_STR_strlist[fh.get_int(min_int=0, max_int=len(recurrent_initializer_STR_strlist)-1)]
		recurrent_initializer_choices.append(recurrent_initializer_STR)
		recurrent_initializer = recurrent_initializer_choices[0]
		bias_initializer_choices = []
		bias_initializer_STR_strlist = ['Zeros'] 
		bias_initializer_STR = bias_initializer_STR_strlist[fh.get_int(min_int=0, max_int=len(bias_initializer_STR_strlist)-1)]
		bias_initializer_choices.append(bias_initializer_STR)
		bias_initializer = bias_initializer_choices[0]
		unit_forget_bias_choices = []
		unit_forget_bias_BOOL = fh.get_bool()
		unit_forget_bias_choices.append(unit_forget_bias_BOOL)
		unit_forget_bias = unit_forget_bias_choices[0]
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
		dropout_INT = fh.get_int()
		dropout_choices.append(dropout_INT)
		dropout_FLOAT = fh.get_float()
		dropout_choices.append(dropout_FLOAT)
		dropout = dropout_choices[fh.get_int()%2]
		recurrent_dropout_choices = []
		recurrent_dropout_INT = fh.get_int()
		recurrent_dropout_choices.append(recurrent_dropout_INT)
		recurrent_dropout_FLOAT = fh.get_float()
		recurrent_dropout_choices.append(recurrent_dropout_FLOAT)
		recurrent_dropout = recurrent_dropout_choices[fh.get_int()%2]
		parameter_0_choices = []
		parameter_0_INT = fh.get_int()
		parameter_0_choices.append(parameter_0_INT)
		parameter_0 = parameter_0_choices[0]
		parameter_1_choices = []
		parameter_1_INT = fh.get_int()
		parameter_1_choices.append(parameter_1_INT)
		parameter_1 = parameter_1_choices[0]
		input_shape_choices = []
		input_shape_LIST = fh.get_int_list(min_length=4, max_length=4)
		input_shape_choices.append(input_shape_LIST)
		input_shape = input_shape_choices[0]
		arg_class = tf.keras.layers.ConvLSTM2D(data_format=data_format,return_sequences=return_sequences,return_state=return_state,stateful=stateful,filters=filters,kernel_size=kernel_size,padding=padding,name=name,trainable=trainable,batch_input_shape=batch_input_shape,dtype=dtype,go_backwards=go_backwards,unroll=unroll,time_major=time_major,strides=strides,dilation_rate=dilation_rate,activation=activation,recurrent_activation=recurrent_activation,use_bias=use_bias,kernel_initializer=kernel_initializer,recurrent_initializer=recurrent_initializer,bias_initializer=bias_initializer,unit_forget_bias=unit_forget_bias,kernel_regularizer=kernel_regularizer,recurrent_regularizer=recurrent_regularizer,bias_regularizer=bias_regularizer,activity_regularizer=activity_regularizer,kernel_constraint=kernel_constraint,recurrent_constraint=recurrent_constraint,bias_constraint=bias_constraint,dropout=dropout,recurrent_dropout=recurrent_dropout,parameter_0,parameter_1,input_shape=input_shape)
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
