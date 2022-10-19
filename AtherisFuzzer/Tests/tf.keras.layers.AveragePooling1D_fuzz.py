#This is a Python API fuzzer for tf.keras.layers.AveragePooling1D
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.keras.layers.AveragePooling1D_exception.txt","a")
	try:
		name_choices = []
		name_STR_strlist = ['average_pooling1d_4', 'average_pooling1d_1', 'average_pooling1d_3', 'average_pooling1d', 'average_pooling1d_2'] 
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
		strides_LIST = fh.get_int_list(min_length=1, max_length=1)
		strides_choices.append(strides_LIST)
		strides_INT = fh.get_int()
		strides_choices.append(strides_INT)
		strides = strides_choices[fh.get_int()%2]
		pool_size_choices = []
		pool_size_LIST = fh.get_int_list(min_length=1, max_length=1)
		pool_size_choices.append(pool_size_LIST)
		pool_size = pool_size_choices[0]
		padding_choices = []
		padding_STR_strlist = ['valid', 'same'] 
		padding_STR = padding_STR_strlist[fh.get_int(min_int=0, max_int=len(padding_STR_strlist)-1)]
		padding_choices.append(padding_STR)
		padding = padding_choices[0]
		data_format_choices = []
		data_format_STR_strlist = ['channels_first', 'channels_last'] 
		data_format_STR = data_format_STR_strlist[fh.get_int(min_int=0, max_int=len(data_format_STR_strlist)-1)]
		data_format_choices.append(data_format_STR)
		data_format = data_format_choices[0]
		batch_input_shape_choices = []
		batch_input_shape_LIST = fh.get_int_list(min_length=3, max_length=3)
		batch_input_shape_choices.append(batch_input_shape_LIST)
		batch_input_shape = batch_input_shape_choices[0]
		arg_class = tf.keras.layers.AveragePooling1D(name=name,trainable=trainable,dtype=dtype,strides=strides,pool_size=pool_size,padding=padding,data_format=data_format,batch_input_shape=batch_input_shape)
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
