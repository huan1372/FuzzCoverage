#This is a Python API fuzzer for tf.keras.layers.Convolution2D
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.keras.layers.Convolution2D_exception.txt","a")
	try:
		filters_choices = []
		filters_INT = fh.get_int()
		filters_choices.append(filters_INT)
		filters = filters_choices[0]
		kernel_size_choices = []
		kernel_size_INT = fh.get_int()
		kernel_size_choices.append(kernel_size_INT)
		kernel_size_LIST = fh.get_int_list(min_length=2, max_length=2)
		kernel_size_choices.append(kernel_size_LIST)
		kernel_size = kernel_size_choices[fh.get_int()%2]
		parameter_0_choices = []
		parameter_0_INT = fh.get_int()
		parameter_0_choices.append(parameter_0_INT)
		parameter_0 = parameter_0_choices[0]
		parameter_1_choices = []
		parameter_1_INT = fh.get_int()
		parameter_1_choices.append(parameter_1_INT)
		parameter_1_LIST = fh.get_int_list(min_length=2, max_length=2)
		parameter_1_choices.append(parameter_1_LIST)
		parameter_1 = parameter_1_choices[fh.get_int()%2]
		activation_choices = []
		activation_STR_strlist = ['sigmoid', 'relu', 'swish', 'linear', 'elu', 'tanh'] 
		activation_STR = activation_STR_strlist[fh.get_int(min_int=0, max_int=len(activation_STR_strlist)-1)]
		activation_choices.append(activation_STR)
		activation_None = None
		activation_choices.append(activation_None)
		activation = activation_choices[fh.get_int()%2]
		input_shape_choices = []
		input_shape_LIST = fh.get_int_list(min_length=3, max_length=3)
		input_shape_choices.append(input_shape_LIST)
		input_shape = input_shape_choices[0]
		dilation_rate_choices = []
		dilation_rate_INT = fh.get_int()
		dilation_rate_choices.append(dilation_rate_INT)
		dilation_rate_LIST = fh.get_int_list(min_length=2, max_length=2)
		dilation_rate_choices.append(dilation_rate_LIST)
		dilation_rate = dilation_rate_choices[fh.get_int()%2]
		padding_choices = []
		padding_STR_strlist = ['SAME', 'same', 'valid'] 
		padding_STR = padding_STR_strlist[fh.get_int(min_int=0, max_int=len(padding_STR_strlist)-1)]
		padding_choices.append(padding_STR)
		padding = padding_choices[0]
		parameter_2_choices = []
		parameter_2_INT = fh.get_int()
		parameter_2_choices.append(parameter_2_INT)
		parameter_2 = parameter_2_choices[0]
		name_choices = []
		name_STR_strlist = ['conv2d', 'conv2d_1'] 
		name_STR = name_STR_strlist[fh.get_int(min_int=0, max_int=len(name_STR_strlist)-1)]
		name_choices.append(name_STR)
		name = name_choices[0]
		trainable_choices = []
		trainable_BOOL = fh.get_bool()
		trainable_choices.append(trainable_BOOL)
		trainable = trainable_choices[0]
		dtype_choices = []
		dtype_STR_strlist = ['float32'] 
		dtype_STR = dtype_STR_strlist[fh.get_int(min_int=0, max_int=len(dtype_STR_strlist)-1)]
		dtype_choices.append(dtype_STR)
		dtype = dtype_choices[0]
		strides_choices = []
		strides_LIST = fh.get_int_list(min_length=2, max_length=2)
		strides_choices.append(strides_LIST)
		strides_INT = fh.get_int()
		strides_choices.append(strides_INT)
		strides = strides_choices[fh.get_int()%2]
		data_format_choices = []
		data_format_STR_strlist = ['channels_last'] 
		data_format_STR = data_format_STR_strlist[fh.get_int(min_int=0, max_int=len(data_format_STR_strlist)-1)]
		data_format_choices.append(data_format_STR)
		data_format = data_format_choices[0]
		groups_choices = []
		groups_INT = fh.get_int()
		groups_choices.append(groups_INT)
		groups = groups_choices[0]
		use_bias_choices = []
		use_bias_BOOL = fh.get_bool()
		use_bias_choices.append(use_bias_BOOL)
		use_bias = use_bias_choices[0]
		kernel_initializer_choices = []
		kernel_initializer_STR_strlist = ['VarianceScaling', 'he_normal', 'GlorotUniform'] 
		kernel_initializer_STR = kernel_initializer_STR_strlist[fh.get_int(min_int=0, max_int=len(kernel_initializer_STR_strlist)-1)]
		kernel_initializer_choices.append(kernel_initializer_STR)
		kernel_initializer = kernel_initializer_choices[0]
		bias_initializer_choices = []
		bias_initializer_STR_strlist = ['Zeros'] 
		bias_initializer_STR = bias_initializer_STR_strlist[fh.get_int(min_int=0, max_int=len(bias_initializer_STR_strlist)-1)]
		bias_initializer_choices.append(bias_initializer_STR)
		bias_initializer = bias_initializer_choices[0]
		kernel_regularizer_choices = []
		kernel_regularizer_None = None
		kernel_regularizer_choices.append(kernel_regularizer_None)
		kernel_regularizer = kernel_regularizer_choices[0]
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
		bias_constraint_choices = []
		bias_constraint_None = None
		bias_constraint_choices.append(bias_constraint_None)
		bias_constraint = bias_constraint_choices[0]
		batch_input_shape_choices = []
		batch_input_shape_LIST = fh.get_int_list(min_length=4, max_length=5)
		batch_input_shape_choices.append(batch_input_shape_LIST)
		batch_input_shape = batch_input_shape_choices[0]
		arg_class = tf.keras.layers.Convolution2D(filters=filters,kernel_size=kernel_size,parameter_0,parameter_1,activation=activation,input_shape=input_shape,dilation_rate=dilation_rate,padding=padding,parameter_2,name=name,trainable=trainable,dtype=dtype,strides=strides,data_format=data_format,groups=groups,use_bias=use_bias,kernel_initializer=kernel_initializer,bias_initializer=bias_initializer,kernel_regularizer=kernel_regularizer,bias_regularizer=bias_regularizer,activity_regularizer=activity_regularizer,kernel_constraint=kernel_constraint,bias_constraint=bias_constraint,batch_input_shape=batch_input_shape)
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
