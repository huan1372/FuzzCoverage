#This is a Python API fuzzer for tf.keras.initializers.RandomUniform
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.keras.initializers.RandomUniform_exception.txt","a")
	try:
		minval_choices = []
		minval_INT = fh.get_int()
		minval_choices.append(minval_INT)
		minval_FLOAT = fh.get_float()
		minval_choices.append(minval_FLOAT)
		minval = minval_choices[fh.get_int()%2]
		maxval_choices = []
		maxval_INT = fh.get_int()
		maxval_choices.append(maxval_INT)
		maxval_FLOAT = fh.get_float()
		maxval_choices.append(maxval_FLOAT)
		maxval = maxval_choices[fh.get_int()%2]
		seed_choices = []
		seed_INT = fh.get_int()
		seed_choices.append(seed_INT)
		seed_None = None
		seed_choices.append(seed_None)
		seed = seed_choices[fh.get_int()%2]
		arg_class = tf.keras.initializers.RandomUniform(minval=minval,maxval=maxval,seed=seed)
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
