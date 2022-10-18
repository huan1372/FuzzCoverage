#This is a Python API fuzzer for tf.data.experimental.dense_to_ragged_batch
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.data.experimental.dense_to_ragged_batch_exception.txt","a")
	try:
		batch_size_choices = []
		batch_size_INT = fh.get_int()
		batch_size_choices.append(batch_size_INT)
		batch_size = batch_size_choices[0]
		arg_class = tf.data.experimental.dense_to_ragged_batch(batch_size=batch_size)
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
