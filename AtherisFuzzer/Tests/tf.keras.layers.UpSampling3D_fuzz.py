#This is a Python API fuzzer for tf.keras.layers.UpSampling3D
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.keras.layers.UpSampling3D_exception.txt","a")
	try:
		size_choices = []
		size_INT = fh.get_int()
		size_choices.append(size_INT)
		size = size_choices[0]
		arg_class = tf.keras.layers.UpSampling3D(size=size)
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
