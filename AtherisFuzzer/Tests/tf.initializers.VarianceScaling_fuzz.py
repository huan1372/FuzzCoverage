#This is a Python API fuzzer for tf.initializers.VarianceScaling
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.initializers.VarianceScaling_exception.txt","a")
	try:
		scale_choices = []
		scale_FLOAT = fh.get_float()
		scale_choices.append(scale_FLOAT)
		scale_INT = fh.get_int()
		scale_choices.append(scale_INT)
		scale = scale_choices[fh.get_int()%2]
		mode_choices = []
		mode_STR_strlist = ['fan_out'] 
		mode_STR = mode_STR_strlist[fh.get_int(min_int=0, max_int=len(mode_STR_strlist)-1)]
		mode_choices.append(mode_STR)
		mode = mode_choices[0]
		distribution_choices = []
		distribution_STR_strlist = ['uniform', 'truncated_normal'] 
		distribution_STR = distribution_STR_strlist[fh.get_int(min_int=0, max_int=len(distribution_STR_strlist)-1)]
		distribution_choices.append(distribution_STR)
		distribution = distribution_choices[0]
		arg_class = tf.initializers.VarianceScaling(scale=scale,mode=mode,distribution=distribution)
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
