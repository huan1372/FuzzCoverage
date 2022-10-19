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
		parameter_0_INT = fh.get_int()
		parameter_0_choices.append(parameter_0_INT)
		parameter_0 = parameter_0_choices[0]
		input_dim_choices = []
		input_dim_INT = fh.get_int()
		input_dim_choices.append(input_dim_INT)
		input_dim = input_dim_choices[0]
		kernel_initializer_choices = []
		kernel_initializer_STR_strlist = ['ones', 'VarianceScaling', 'glorot_normal', 'GlorotUniform'] 
		kernel_initializer_STR = kernel_initializer_STR_strlist[fh.get_int(min_int=0, max_int=len(kernel_initializer_STR_strlist)-1)]
		kernel_initializer_choices.append(kernel_initializer_STR)
		kernel_initializer_None = None
		kernel_initializer_choices.append(kernel_initializer_None)
		kernel_initializer_TF_OBJECT_tfobjlist = ['TruncatedNormal'] 
		kernel_initializer_TF_OBJECT = eval("tf.keras.initializers." + {strListName}[fh.get_int(min_int=0, max_int=len({strListName})-1)])
		kernel_initializer_choices.append(kernel_initializer_TF_OBJECT)
		kernel_initializer = kernel_initializer_choices[fh.get_int()%3]
		kernel_regularizer_choices = []
		kernel_regularizer_None = None
		kernel_regularizer_choices.append(kernel_regularizer_None)
		kernel_regularizer = kernel_regularizer_choices[0]
		activation_choices = []
		activation_STR_strlist = ['relu', 'softmax', 'softplus', 'sigmoid', 'tanh', 'linear'] 
		activation_STR = activation_STR_strlist[fh.get_int(min_int=0, max_int=len(activation_STR_strlist)-1)]
		activation_choices.append(activation_STR)
		activation_None = None
		activation_choices.append(activation_None)
		activation = activation_choices[fh.get_int()%2]
		activity_regularizer_choices = []
		activity_regularizer_None = None
		activity_regularizer_choices.append(activity_regularizer_None)
		activity_regularizer = activity_regularizer_choices[0]
		input_shape_choices = []
		input_shape_LIST = fh.get_int_list(min_length=1, max_length=1)
		input_shape_choices.append(input_shape_LIST)
		input_shape = input_shape_choices[0]
		name_choices = []
		name_STR_strlist = ['dense_3', 'out', 'dense_1', 'predictions', 'dense', 'dense_2'] 
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
		batch_input_shape_LIST = fh.get_int_list(min_length=2, max_length=4)
		batch_input_shape_choices.append(batch_input_shape_LIST)
		batch_input_shape = batch_input_shape_choices[0]
		dtype_choices = []
		dtype_STR_strlist = ['float32'] 
		dtype_STR = dtype_STR_strlist[fh.get_int(min_int=0, max_int=len(dtype_STR_strlist)-1)]
		dtype_choices.append(dtype_STR)
		dtype_DTYPE_dtypelist = ['tf.float32', 'tf.float64'] 
		dtype_DTYPE = eval(dtype_DTYPE_dtypelist[fh.get_int(min_int=0, max_int=len(dtype_DTYPE_dtypelist)-1)])
		dtype_choices.append(dtype_DTYPE)
		dtype = dtype_choices[fh.get_int()%2]
		units_choices = []
		units_INT = fh.get_int()
		units_choices.append(units_INT)
		units = units_choices[0]
		use_bias_choices = []
		use_bias_BOOL = fh.get_bool()
		use_bias_choices.append(use_bias_BOOL)
		use_bias = use_bias_choices[0]
		bias_initializer_choices = []
		bias_initializer_STR_strlist = ['Zeros'] 
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
