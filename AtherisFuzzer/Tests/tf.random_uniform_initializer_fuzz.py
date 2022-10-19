#This is a Python API fuzzer for tf.random_uniform_initializer
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.random_uniform_initializer_exception.txt","a")
	try:
		parameter_0_choices = []
		parameter_0_INT = fh.get_int()
		parameter_0_choices.append(parameter_0_INT)
		parameter_0 = parameter_0_choices[0]
		parameter_1_choices = []
		parameter_1_INT = fh.get_int()
		parameter_1_choices.append(parameter_1_INT)
		parameter_1 = parameter_1_choices[0]
		seed_choices = []
		seed_INT = fh.get_int()
		seed_choices.append(seed_INT)
		seed = seed_choices[0]
		minval_choices = []
		minval_INT = fh.get_int()
		minval_choices.append(minval_INT)
		minval = minval_choices[0]
		maxval_choices = []
		maxval_INT = fh.get_int()
		maxval_choices.append(maxval_INT)
		maxval = maxval_choices[0]
		arg_class = tf.random_uniform_initializer(parameter_0,parameter_1,seed=seed,minval=minval,maxval=maxval)
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
