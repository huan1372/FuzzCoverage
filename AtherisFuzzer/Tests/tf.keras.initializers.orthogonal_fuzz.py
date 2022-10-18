#This is a Python API fuzzer for tf.keras.initializers.orthogonal
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.keras.initializers.orthogonal_exception.txt","a")
	try:
		gain_choices = []
		gain_INT = fh.get_int()
		gain_choices.append(gain_INT)
		gain = gain_choices[0]
		seed_choices = []
		seed_None = None
		seed_choices.append(seed_None)
		seed = seed_choices[0]
		arg_class = tf.keras.initializers.orthogonal(gain=gain,seed=seed)
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
