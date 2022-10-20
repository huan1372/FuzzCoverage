#This is a Python API fuzzer for tf.keras.layers.SpatialDropout2D
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.keras.layers.SpatialDropout2D_exception.txt","a")
	try:
		name_choices = []
		name_STR_strlist = ['spatial_dropout2d_1', 'spatial_dropout2d'] 
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
		rate_choices = []
		rate_FLOAT = fh.get_float()
		rate_choices.append(rate_FLOAT)
		rate = rate_choices[0]
		noise_shape_choices = []
		noise_shape_None = None
		noise_shape_choices.append(noise_shape_None)
		noise_shape = noise_shape_choices[0]
		seed_choices = []
		seed_None = None
		seed_choices.append(seed_None)
		seed = seed_choices[0]
		batch_input_shape_choices = []
		batch_input_shape_LIST = fh.get_int_list(min_length=4, max_length=4)
		batch_input_shape_choices.append(batch_input_shape_LIST)
		batch_input_shape = batch_input_shape_choices[0]
		data_format_choices = []
		data_format_STR_strlist = ['channels_first'] 
		data_format_STR = data_format_STR_strlist[fh.get_int(min_int=0, max_int=len(data_format_STR_strlist)-1)]
		data_format_choices.append(data_format_STR)
		data_format = data_format_choices[0]
		arg_class = tf.keras.layers.SpatialDropout2D(name=name,trainable=trainable,dtype=dtype,rate=rate,noise_shape=noise_shape,seed=seed,batch_input_shape=batch_input_shape,data_format=data_format)
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
