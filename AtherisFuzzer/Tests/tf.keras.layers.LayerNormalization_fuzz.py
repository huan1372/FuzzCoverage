#This is a Python API fuzzer for tf.keras.layers.LayerNormalization
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.keras.layers.LayerNormalization_exception.txt","a")
	try:
		axis_choices = []
		axis_INT = fh.get_int()
		axis_choices.append(axis_INT)
		axis_LIST = fh.get_int_list(min_length=1, max_length=3)
		axis_choices.append(axis_LIST)
		axis = axis_choices[fh.get_int()%2]
		dtype_choices = []
		dtype_STR_strlist = ['float64', 'float32', 'float16'] 
		dtype_STR = dtype_STR_strlist[fh.get_int(min_int=0, max_int=len(dtype_STR_strlist)-1)]
		dtype_choices.append(dtype_STR)
		dtype = dtype_choices[0]
		batch_input_shape_choices = []
		batch_input_shape_LIST = fh.get_int_list(min_length=2, max_length=4)
		batch_input_shape_choices.append(batch_input_shape_LIST)
		batch_input_shape = batch_input_shape_choices[0]
		epsilon_choices = []
		epsilon_FLOAT = fh.get_float()
		epsilon_choices.append(epsilon_FLOAT)
		epsilon = epsilon_choices[0]
		beta_initializer_choices = []
		beta_initializer_STR_strlist = ['ones', 'Ones', 'Zeros'] 
		beta_initializer_STR = beta_initializer_STR_strlist[fh.get_int(min_int=0, max_int=len(beta_initializer_STR_strlist)-1)]
		beta_initializer_choices.append(beta_initializer_STR)
		beta_initializer = beta_initializer_choices[0]
		gamma_initializer_choices = []
		gamma_initializer_STR_strlist = ['ones', 'Ones'] 
		gamma_initializer_STR = gamma_initializer_STR_strlist[fh.get_int(min_int=0, max_int=len(gamma_initializer_STR_strlist)-1)]
		gamma_initializer_choices.append(gamma_initializer_STR)
		gamma_initializer = gamma_initializer_choices[0]
		input_shape_choices = []
		input_shape_LIST = fh.get_int_list(min_length=3, max_length=3)
		input_shape_choices.append(input_shape_LIST)
		input_shape = input_shape_choices[0]
		name_choices = []
		name_STR_strlist = ['layer_normalization_1', 'layer_normalization', 'layer_normalization_3', 'layer_normalization_2'] 
		name_STR = name_STR_strlist[fh.get_int(min_int=0, max_int=len(name_STR_strlist)-1)]
		name_choices.append(name_STR)
		name = name_choices[0]
		trainable_choices = []
		trainable_BOOL = fh.get_bool()
		trainable_choices.append(trainable_BOOL)
		trainable = trainable_choices[0]
		center_choices = []
		center_BOOL = fh.get_bool()
		center_choices.append(center_BOOL)
		center = center_choices[0]
		scale_choices = []
		scale_BOOL = fh.get_bool()
		scale_choices.append(scale_BOOL)
		scale = scale_choices[0]
		beta_regularizer_choices = []
		beta_regularizer_None = None
		beta_regularizer_choices.append(beta_regularizer_None)
		beta_regularizer_STR_strlist = ['L2', 'l2'] 
		beta_regularizer_STR = beta_regularizer_STR_strlist[fh.get_int(min_int=0, max_int=len(beta_regularizer_STR_strlist)-1)]
		beta_regularizer_choices.append(beta_regularizer_STR)
		beta_regularizer = beta_regularizer_choices[fh.get_int()%2]
		gamma_regularizer_choices = []
		gamma_regularizer_None = None
		gamma_regularizer_choices.append(gamma_regularizer_None)
		gamma_regularizer_STR_strlist = ['L2', 'l2'] 
		gamma_regularizer_STR = gamma_regularizer_STR_strlist[fh.get_int(min_int=0, max_int=len(gamma_regularizer_STR_strlist)-1)]
		gamma_regularizer_choices.append(gamma_regularizer_STR)
		gamma_regularizer = gamma_regularizer_choices[fh.get_int()%2]
		beta_constraint_choices = []
		beta_constraint_None = None
		beta_constraint_choices.append(beta_constraint_None)
		beta_constraint = beta_constraint_choices[0]
		gamma_constraint_choices = []
		gamma_constraint_None = None
		gamma_constraint_choices.append(gamma_constraint_None)
		gamma_constraint = gamma_constraint_choices[0]
		arg_class = tf.keras.layers.LayerNormalization(axis=axis,dtype=dtype,batch_input_shape=batch_input_shape,epsilon=epsilon,beta_initializer=beta_initializer,gamma_initializer=gamma_initializer,input_shape=input_shape,name=name,trainable=trainable,center=center,scale=scale,beta_regularizer=beta_regularizer,gamma_regularizer=gamma_regularizer,beta_constraint=beta_constraint,gamma_constraint=gamma_constraint)
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
