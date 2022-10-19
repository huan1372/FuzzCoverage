#This is a Python API fuzzer for tf.keras.optimizers.schedules.ExponentialDecay
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.keras.optimizers.schedules.ExponentialDecay_exception.txt","a")
	try:
		initial_learning_rate_choices = []
		initial_learning_rate_FLOAT = fh.get_float()
		initial_learning_rate_choices.append(initial_learning_rate_FLOAT)
		initial_learning_rate_INT = fh.get_int()
		initial_learning_rate_choices.append(initial_learning_rate_INT)
		initial_learning_rate = initial_learning_rate_choices[fh.get_int()%2]
		decay_steps_choices = []
		decay_steps_INT = fh.get_int()
		decay_steps_choices.append(decay_steps_INT)
		decay_steps = decay_steps_choices[0]
		decay_rate_choices = []
		decay_rate_FLOAT = fh.get_float()
		decay_rate_choices.append(decay_rate_FLOAT)
		decay_rate = decay_rate_choices[0]
		arg_class = tf.keras.optimizers.schedules.ExponentialDecay(initial_learning_rate=initial_learning_rate,decay_steps=decay_steps,decay_rate=decay_rate)
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
