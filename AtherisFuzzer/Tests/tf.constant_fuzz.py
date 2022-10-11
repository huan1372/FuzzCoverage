#This is a Python API fuzzer for tf.constant
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.constant_exception.txt","a")
	try:
		parameter_0_choices = []
		parameter_0_INT = fh.get_int()
		parameter_0_choices.append(parameter_0_INT)
		parameter_0_STR_strlist = ['palmer 30'] 
		parameter_0_STR = parameter_0_STR_strlist[fh.get_int(min_int=0, max_int=len(parameter_0_STR_strlist)]
		parameter_0_choices.append(parameter_0_STR)
		parameter_0 = parameter_0_choices[fh.get_int()%2]
		dtype_choices = []
		dtype = dtype_choices[fh.get_int()%0]
		parameter_1_choices = []
		parameter_1 = parameter_1_choices[fh.get_int()%0]
		_ = tf.constant(parameter_0,dtype=dtype,parameter_1)
	except Exception as e:
		f.write(str(e) + "\n")
	f.close()
def main():
	atheris.Setup(sys.argv, TestOneInput, enable_python_coverage=True)
	atheris.Fuzz()

if __name__ == "__main__":
	main()
