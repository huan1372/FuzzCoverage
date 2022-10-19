#This is a Python API fuzzer for tf.keras.layers.Layer
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.keras.layers.Layer_exception.txt","a")
	try:
		activity_regularizer_choices = []
		activity_regularizer_None = None
		activity_regularizer_choices.append(activity_regularizer_None)
		activity_regularizer = activity_regularizer_choices[0]
		trainable_choices = []
		trainable_BOOL = fh.get_bool()
		trainable_choices.append(trainable_BOOL)
		trainable = trainable_choices[0]
		dtype_choices = []
		dtype_STR_strlist = ['float32'] 
		dtype_STR = dtype_STR_strlist[fh.get_int(min_int=0, max_int=len(dtype_STR_strlist)-1)]
		dtype_choices.append(dtype_STR)
		dtype_None = None
		dtype_choices.append(dtype_None)
		dtype_DTYPE_dtypelist = ['tf.bfloat16', 'tf.bool', 'tf.complex128', 'tf.complex64', 'tf.double', 'tf.float16', 'tf.float32', 'tf.float64', 'tf.half', 'tf.int16', 'tf.int32', 'tf.int64', 'tf.int8', 'tf.uint8', 'tf.uint16', 'tf.uint32', 'tf.uint64'] 
		dtype_DTYPE = eval(dtype_DTYPE_dtypelist[fh.get_int(min_int=0, max_int=len(dtype_DTYPE_dtypelist)-1)])
		dtype_choices.append(dtype_DTYPE)
		dtype = dtype_choices[fh.get_int()%3]
		autocast_choices = []
		autocast_BOOL = fh.get_bool()
		autocast_choices.append(autocast_BOOL)
		autocast = autocast_choices[0]
		arg_class = tf.keras.layers.Layer(activity_regularizer=activity_regularizer,trainable=trainable,dtype=dtype,autocast=autocast)
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
