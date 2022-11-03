#This is a Python API fuzzer for tf.keras.layers.LeakyReLU
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.keras.layers.LeakyReLU_exception.txt","a")
	try:
		alpha_choices = []
		alpha_FLOAT = fh.get_float()
		alpha_choices.append(alpha_FLOAT)
		alpha_INT = fh.get_int()
		alpha_choices.append(alpha_INT)
		alpha = alpha_choices[fh.get_int()%2]
		name_choices = []
		name_STR_strlist = ['leaky_re_lu_2', 'leaky_re_lu', 'leaky_re_lu_1'] 
		name_STR = name_STR_strlist[fh.get_int(min_int=0, max_int=len(name_STR_strlist)-1)]
		name_choices.append(name_STR)
		name = name_choices[0]
		trainable_choices = []
		trainable_BOOL = fh.get_bool()
		trainable_choices.append(trainable_BOOL)
		trainable = trainable_choices[0]
		batch_input_shape_choices = []
		batch_input_shape_LIST = fh.get_int_list(min_length=3, max_length=3)
		batch_input_shape_choices.append(batch_input_shape_LIST)
		batch_input_shape = batch_input_shape_choices[0]
		dtype_choices = []
		dtype_STR_strlist = ['float32'] 
		dtype_STR = dtype_STR_strlist[fh.get_int(min_int=0, max_int=len(dtype_STR_strlist)-1)]
		dtype_choices.append(dtype_STR)
		dtype = dtype_choices[0]
		parameter_0_choices = []
		parameter_0_FLOAT = fh.get_float()
		parameter_0_choices.append(parameter_0_FLOAT)
		parameter_0 = parameter_0_choices[0]
		arg_class = tf.keras.layers.LeakyReLU(alpha=alpha,name=name,trainable=trainable,batch_input_shape=batch_input_shape,dtype=dtype,parameter_0)
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