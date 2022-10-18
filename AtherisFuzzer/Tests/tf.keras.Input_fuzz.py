#This is a Python API fuzzer for tf.keras.Input
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.keras.Input_exception.txt","a")
	try:
		shape_choices = []
		shape_LIST = fh.get_int_list(min_length=1, max_length=4)
		shape_choices.append(shape_LIST)
		shape = shape_choices[0]
		dtype_choices = []
		dtype_DTYPE_dtypelist = ['tf.bfloat16', 'tf.bool', 'tf.complex128', 'tf.complex64', 'tf.double', 'tf.float16', 'tf.float32', 'tf.float64', 'tf.half', 'tf.int16', 'tf.int32', 'tf.int64', 'tf.int8', 'tf.uint8', 'tf.uint16', 'tf.uint32', 'tf.uint64'] 
		dtype_DTYPE = eval(dtype_DTYPE_dtypelist[fh.get_int(min_int=0, max_int=len(dtype_DTYPE_dtypelist)-1)])
		dtype_choices.append(dtype_DTYPE)
		dtype = dtype_choices[0]
		arg_class = tf.keras.Input(shape=shape,dtype=dtype)
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
