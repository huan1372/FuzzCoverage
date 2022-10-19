#This is a Python API fuzzer for tf.keras.layers.Masking
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.keras.layers.Masking_exception.txt","a")
	try:
		mask_value_choices = []
		mask_value_INT = fh.get_int()
		mask_value_choices.append(mask_value_INT)
		mask_value = mask_value_choices[0]
		input_shape_choices = []
		input_shape_LIST = fh.get_int_list(min_length=2, max_length=2)
		input_shape_choices.append(input_shape_LIST)
		input_shape = input_shape_choices[0]
		parameter_0_choices = []
		parameter_0_INT = fh.get_int()
		parameter_0_choices.append(parameter_0_INT)
		parameter_0_FLOAT = fh.get_float()
		parameter_0_choices.append(parameter_0_FLOAT)
		parameter_0 = parameter_0_choices[fh.get_int()%2]
		name_choices = []
		name_STR_strlist = ['masking'] 
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
		batch_input_shape_choices = []
		batch_input_shape_LIST = fh.get_int_list(min_length=3, max_length=3)
		batch_input_shape_choices.append(batch_input_shape_LIST)
		batch_input_shape = batch_input_shape_choices[0]
		arg_class = tf.keras.layers.Masking(mask_value=mask_value,input_shape=input_shape,parameter_0,name=name,trainable=trainable,dtype=dtype,batch_input_shape=batch_input_shape)
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
