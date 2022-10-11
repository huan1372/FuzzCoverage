#This is a Python API fuzzer for tf.histogram_fixed_width
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.histogram_fixed_width_exception.txt","a")
	try:
		parameter_0_choices = []
		parameter_0 = parameter_0_choices[fh.get_int()%0]
		parameter_1_choices = []
		parameter_1 = parameter_1_choices[fh.get_int()%0]
		nbins_choices = []
		nbins_INT = fh.get_int()
		nbins_choices.append(nbins_INT)
		nbins = nbins_choices[fh.get_int()%1]
		_ = tf.histogram_fixed_width(parameter_0,parameter_1,nbins=nbins)
	except Exception as e:
		f.write(str(e) + "\n")
	f.close()
def main():
	atheris.Setup(sys.argv, TestOneInput, enable_python_coverage=True)
	atheris.Fuzz()

if __name__ == "__main__":
	main()
