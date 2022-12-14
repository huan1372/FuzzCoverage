#This is a Python API fuzzer for tf.losses.CategoricalCrossentropy
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.losses.CategoricalCrossentropy_exception.txt","a")
	try:
		reduction_choices = []
		reduction_STR_strlist = ['sum', 'none'] 
		reduction_STR = reduction_STR_strlist[fh.get_int(min_int=0, max_int=len(reduction_STR_strlist)-1)]
		reduction_choices.append(reduction_STR)
		reduction = reduction_choices[0]
		from_logits_choices = []
		from_logits_BOOL = fh.get_bool()
		from_logits_choices.append(from_logits_BOOL)
		from_logits = from_logits_choices[0]
		arg_class = tf.losses.CategoricalCrossentropy(reduction=reduction,from_logits=from_logits)
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
