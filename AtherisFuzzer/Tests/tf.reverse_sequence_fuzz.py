#This is a Python API fuzzer for tf.reverse_sequence
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.reverse_sequence_exception.txt","a")
	try:
		parameter_0_choices = []
		parameter_0_LIST = fh.get_int_list(min_length=4, max_length=4)
		parameter_0_choices.append(parameter_0_LIST)
		parameter_0 = parameter_0_choices[0]
		parameter_1_choices = []
		parameter_1_LIST = fh.get_int_list(min_length=4, max_length=4)
		parameter_1_choices.append(parameter_1_LIST)
		parameter_1 = parameter_1_choices[0]
		seq_axis_choices = []
		seq_axis_INT = fh.get_int()
		seq_axis_choices.append(seq_axis_INT)
		seq_axis = seq_axis_choices[0]
		batch_axis_choices = []
		batch_axis_INT = fh.get_int()
		batch_axis_choices.append(batch_axis_INT)
		batch_axis = batch_axis_choices[0]
		arg_class = tf.reverse_sequence(parameter_0,parameter_1,seq_axis=seq_axis,batch_axis=batch_axis)
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
