#This is a Python API fuzzer for tf.random.create_rng_state
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.random.create_rng_state_exception.txt","a")
	try:
		parameter_0_choices = []
		parameter_0_LIST = fh.get_int_list(min_length=2, max_length=2)
		parameter_0_choices.append(parameter_0_LIST)
		parameter_0_INT = fh.get_int()
		parameter_0_choices.append(parameter_0_INT)
		parameter_0 = parameter_0_choices[fh.get_int()%2]
		parameter_1_choices = []
		parameter_1_STR_strlist = ['threefry', 'philox'] 
		parameter_1_STR = parameter_1_STR_strlist[fh.get_int(min_int=0, max_int=len(parameter_1_STR_strlist)-1)]
		parameter_1_choices.append(parameter_1_STR)
		parameter_1 = parameter_1_choices[0]
		arg_class = tf.random.create_rng_state(parameter_0,parameter_1)
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
