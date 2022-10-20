#This is a Python API fuzzer for tf.keras.layers.experimental.RandomFourierFeatures
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.keras.layers.experimental.RandomFourierFeatures_exception.txt","a")
	try:
		output_dim_choices = []
		output_dim_INT = fh.get_int()
		output_dim_choices.append(output_dim_INT)
		output_dim = output_dim_choices[0]
		kernel_initializer_choices = []
		kernel_initializer_STR_strlist = ['gaussian', 'laplacian'] 
		kernel_initializer_STR = kernel_initializer_STR_strlist[fh.get_int(min_int=0, max_int=len(kernel_initializer_STR_strlist)-1)]
		kernel_initializer_choices.append(kernel_initializer_STR)
		kernel_initializer = kernel_initializer_choices[0]
		scale_choices = []
		scale_INT = fh.get_int()
		scale_choices.append(scale_INT)
		scale_FLOAT = fh.get_float()
		scale_choices.append(scale_FLOAT)
		scale_None = None
		scale_choices.append(scale_None)
		scale = scale_choices[fh.get_int()%3]
		name_choices = []
		name_STR_strlist = ['rff2', 'rff', 'random_fourier_features'] 
		name_STR = name_STR_strlist[fh.get_int(min_int=0, max_int=len(name_STR_strlist)-1)]
		name_choices.append(name_STR)
		name = name_choices[0]
		trainable_choices = []
		trainable_BOOL = fh.get_bool()
		trainable_choices.append(trainable_BOOL)
		trainable = trainable_choices[0]
		arg_class = tf.keras.layers.experimental.RandomFourierFeatures(output_dim=output_dim,kernel_initializer=kernel_initializer,scale=scale,name=name,trainable=trainable)
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
