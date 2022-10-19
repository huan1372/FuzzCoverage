#This is a Python API fuzzer for tf.train.experimental.DynamicLossScale
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.train.experimental.DynamicLossScale_exception.txt","a")
	try:
		initial_loss_scale_choices = []
		initial_loss_scale_INT = fh.get_int()
		initial_loss_scale_choices.append(initial_loss_scale_INT)
		initial_loss_scale = initial_loss_scale_choices[0]
		increment_period_choices = []
		increment_period_INT = fh.get_int()
		increment_period_choices.append(increment_period_INT)
		increment_period = increment_period_choices[0]
		multiplier_choices = []
		multiplier_INT = fh.get_int()
		multiplier_choices.append(multiplier_INT)
		multiplier = multiplier_choices[0]
		parameter_0_choices = []
		parameter_0_INT = fh.get_int()
		parameter_0_choices.append(parameter_0_INT)
		parameter_0 = parameter_0_choices[0]
		arg_class = tf.train.experimental.DynamicLossScale(initial_loss_scale=initial_loss_scale,increment_period=increment_period,multiplier=multiplier,parameter_0)
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
