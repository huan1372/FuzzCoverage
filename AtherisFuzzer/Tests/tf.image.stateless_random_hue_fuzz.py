#This is a Python API fuzzer for tf.image.stateless_random_hue
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.image.stateless_random_hue_exception.txt","a")
	try:
		parameter_0_choices = []
		parameter_0 = parameter_0_choices[fh.get_int()%0]
		parameter_1_choices = []
		parameter_1_FLOAT = fh.get_float()
		parameter_1_choices.append(parameter_1_FLOAT)
		parameter_1 = parameter_1_choices[fh.get_int()%1]
		parameter_2_choices = []
		parameter_2 = parameter_2_choices[fh.get_int()%0]
		_ = tf.image.stateless_random_hue(parameter_0,parameter_1,parameter_2)
	except Exception as e:
		f.write(str(e) + "\n")
	f.close()
def main():
	atheris.Setup(sys.argv, TestOneInput, enable_python_coverage=True)
	atheris.Fuzz()

if __name__ == "__main__":
	main()
