#This is a Python API fuzzer for tf.keras.layers.Dropout
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.keras.layers.Dropout_exception.txt","a")
	try:
		rate_choices = []
		rate_INT = fh.get_int()
		rate_choices.append(rate_INT)
		rate_FLOAT = fh.get_float()
		rate_choices.append(rate_FLOAT)
		rate = rate_choices[fh.get_int()%2]
		parameter_0_choices = []
		parameter_0_FLOAT = fh.get_float()
		parameter_0_choices.append(parameter_0_FLOAT)
		parameter_0 = parameter_0_choices[0]
		input_shape_choices = []
		input_shape_LIST = fh.get_int_list(min_length=1, max_length=1)
		input_shape_choices.append(input_shape_LIST)
		input_shape = input_shape_choices[0]
		name_choices = []
		name_STR_strlist = ['dropout_1', 'spatial_dropout2d', 'spatial_dropout3d_1', 'dropout', 'spatial_dropout1d', 'spatial_dropout3d', 'spatial_dropout2d_1'] 
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
		noise_shape_choices = []
		noise_shape_None = None
		noise_shape_choices.append(noise_shape_None)
		noise_shape_LIST = fh.get_int_list(min_length=2, max_length=3)
		noise_shape_choices.append(noise_shape_LIST)
		noise_shape = noise_shape_choices[fh.get_int()%2]
		seed_choices = []
		seed_None = None
		seed_choices.append(seed_None)
		seed = seed_choices[0]
		batch_input_shape_choices = []
		batch_input_shape_LIST = fh.get_int_list(min_length=2, max_length=5)
		batch_input_shape_choices.append(batch_input_shape_LIST)
		batch_input_shape = batch_input_shape_choices[0]
		arg_class = tf.keras.layers.Dropout(rate=rate,parameter_0,input_shape=input_shape,name=name,trainable=trainable,dtype=dtype,noise_shape=noise_shape,seed=seed,batch_input_shape=batch_input_shape)
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
