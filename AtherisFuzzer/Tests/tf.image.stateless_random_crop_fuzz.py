#This is a Python API fuzzer for tf.image.stateless_random_crop
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.image.stateless_random_crop_exception.txt","a")
	try:
		value_choices = []
		value = value_choices[fh.get_int()%0]
		size_choices = []
		size = size_choices[fh.get_int()%0]
		seed_choices = []
		seed = seed_choices[fh.get_int()%0]
		_ = tf.image.stateless_random_crop(value=value,size=size,seed=seed)
	except Exception as e:
		f.write(str(e) + "\n")
	f.close()
def main():
	atheris.Setup(sys.argv, TestOneInput, enable_python_coverage=True)
	atheris.Fuzz()

if __name__ == "__main__":
	main()
