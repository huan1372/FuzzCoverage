#This is a Python API fuzzer for tf.keras.metrics.sparse_top_k_categorical_accuracy
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.keras.metrics.sparse_top_k_categorical_accuracy_exception.txt","a")
	try:
		parameter_0_choices = []
		parameter_0_LIST = fh.get_int_list(min_length=2, max_length=2)
		parameter_0_choices.append(parameter_0_LIST)
		parameter_0 = parameter_0_choices[0]
		parameter_1_choices = []
		parameter_1_LIST = fh.get_int_list(min_length=2, max_length=2)
		parameter_1_choices.append(parameter_1_LIST)
		parameter_1 = parameter_1_choices[0]
		k_choices = []
		k_INT = fh.get_int()
		k_choices.append(k_INT)
		k = k_choices[0]
		arg_class = tf.keras.metrics.sparse_top_k_categorical_accuracy(parameter_0,parameter_1,k=k)
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
