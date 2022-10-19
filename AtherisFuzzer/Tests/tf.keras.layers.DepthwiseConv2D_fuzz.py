#This is a Python API fuzzer for tf.keras.layers.DepthwiseConv2D
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.keras.layers.DepthwiseConv2D_exception.txt","a")
	try:
		kernel_size_choices = []
		kernel_size_INT = fh.get_int()
		kernel_size_choices.append(kernel_size_INT)
		kernel_size = kernel_size_choices[0]
		strides_choices = []
		strides_INT = fh.get_int()
		strides_choices.append(strides_INT)
		strides = strides_choices[0]
		activation_choices = []
		activation_None = None
		activation_choices.append(activation_None)
		activation = activation_choices[0]
		use_bias_choices = []
		use_bias_BOOL = fh.get_bool()
		use_bias_choices.append(use_bias_BOOL)
		use_bias = use_bias_choices[0]
		padding_choices = []
		padding_STR_strlist = ['valid', 'same'] 
		padding_STR = padding_STR_strlist[fh.get_int(min_int=0, max_int=len(padding_STR_strlist)-1)]
		padding_choices.append(padding_STR)
		padding = padding_choices[0]
		parameter_0_choices = []
		parameter_0_INT = fh.get_int()
		parameter_0_choices.append(parameter_0_INT)
		parameter_0 = parameter_0_choices[0]
		depth_multiplier_choices = []
		depth_multiplier_INT = fh.get_int()
		depth_multiplier_choices.append(depth_multiplier_INT)
		depth_multiplier = depth_multiplier_choices[0]
		depthwise_initializer_choices = []
		depthwise_initializer_STR_strlist = ['VarianceScaling'] 
		depthwise_initializer_STR = depthwise_initializer_STR_strlist[fh.get_int(min_int=0, max_int=len(depthwise_initializer_STR_strlist)-1)]
		depthwise_initializer_choices.append(depthwise_initializer_STR)
		depthwise_initializer = depthwise_initializer_choices[0]
		arg_class = tf.keras.layers.DepthwiseConv2D(kernel_size=kernel_size,strides=strides,activation=activation,use_bias=use_bias,padding=padding,parameter_0,depth_multiplier=depth_multiplier,depthwise_initializer=depthwise_initializer)
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
