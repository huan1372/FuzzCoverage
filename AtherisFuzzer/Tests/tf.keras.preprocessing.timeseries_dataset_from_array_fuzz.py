#This is a Python API fuzzer for tf.keras.preprocessing.timeseries_dataset_from_array
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.keras.preprocessing.timeseries_dataset_from_array_exception.txt","a")
	try:
		parameter_0_choices = []
		parameter_0 = parameter_0_choices[fh.get_int()%0]
		parameter_1_choices = []
		parameter_1 = parameter_1_choices[fh.get_int()%0]
		sequence_length_choices = []
		sequence_length_INT = fh.get_int()
		sequence_length_choices.append(sequence_length_INT)
		sequence_length = sequence_length_choices[0]
		sampling_rate_choices = []
		sampling_rate_INT = fh.get_int()
		sampling_rate_choices.append(sampling_rate_INT)
		sampling_rate = sampling_rate_choices[0]
		batch_size_choices = []
		batch_size_INT = fh.get_int()
		batch_size_choices.append(batch_size_INT)
		batch_size = batch_size_choices[0]
		arg_class = tf.keras.preprocessing.timeseries_dataset_from_array(parameter_0,parameter_1,sequence_length=sequence_length,sampling_rate=sampling_rate,batch_size=batch_size)
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
