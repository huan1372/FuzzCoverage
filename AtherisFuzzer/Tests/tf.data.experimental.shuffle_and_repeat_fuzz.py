#This is a Python API fuzzer for tf.data.experimental.shuffle_and_repeat
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.data.experimental.shuffle_and_repeat_exception.txt","a")
	try:
		parameter_0_choices = []
		parameter_0_INT = fh.get_int()
		parameter_0_choices.append(parameter_0_INT)
		parameter_0 = parameter_0_choices[fh.get_int()%1]
		count_choices = []
		count_INT = fh.get_int()
		count_choices.append(count_INT)
		count = count_choices[fh.get_int()%1]
		_ = tf.data.experimental.shuffle_and_repeat(parameter_0,count=count)
	except Exception as e:
		f.write(str(e) + "\n")
	f.close()
def main():
	atheris.Setup(sys.argv, TestOneInput, enable_python_coverage=True)
	atheris.Fuzz()

if __name__ == "__main__":
	main()
