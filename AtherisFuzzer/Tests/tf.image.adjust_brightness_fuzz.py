#This is a Python API fuzzer for tf.image.adjust_brightness
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.image.adjust_brightness_exception.txt","a")
	try:
		parameter_0_choices = []
		parameter_0 = parameter_0_choices[fh.get_int()%0]
		delta_choices = []
		delta_FLOAT = fh.get_float()
		delta_choices.append(delta_FLOAT)
		delta = delta_choices[fh.get_int()%1]
		_ = tf.image.adjust_brightness(parameter_0,delta=delta)
	except Exception as e:
		f.write(str(e) + "\n")
	f.close()
def main():
	atheris.Setup(sys.argv, TestOneInput, enable_python_coverage=True)
	atheris.Fuzz()

if __name__ == "__main__":
	main()
