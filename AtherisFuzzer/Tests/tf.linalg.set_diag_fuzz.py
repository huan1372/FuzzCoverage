#This is a Python API fuzzer for tf.linalg.set_diag
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.linalg.set_diag_exception.txt","a")
	try:
		parameter_0_choices = []
		# Tensor generation for parameter_0
		parameter_0_DTYPES = [tf.float32]
		int_list = fh.get_int_list(min_length=2,max_length=2)
		min_Val = min(int_list) - 1
		max_Val = max(int_list)
		if min_Val % 2 == 0:
			parameter_0_tensor = fh.get_random_numeric_tensor(dtype=fh.get_tf_dtype(allowed_set=parameter_0_DTYPES))
		else:
			parameter_0_tensor = fh.get_random_numeric_tensor(min_val = min_Val, max_val = max_Val, dtype=fh.get_tf_dtype(allowed_set=parameter_0_DTYPES))
		parameter_0_tensor = tf.identity(parameter_0_tensor)
		parameter_0_choices.append(parameter_0_tensor)
		parameter_0 = parameter_0_choices[0]
		parameter_1_choices = []
		parameter_1_LIST = fh.get_int_list(min_length=2, max_length=2)
		parameter_1_choices.append(parameter_1_LIST)
		parameter_1 = parameter_1_choices[0]
		align_choices = []
		align_STR_strlist = ['LEFT_RIGHT'] 
		align_STR = align_STR_strlist[fh.get_int(min_int=0, max_int=len(align_STR_strlist)-1)]
		align_choices.append(align_STR)
		align = align_choices[0]
		k_choices = []
		k_LIST = fh.get_int_list(min_length=2, max_length=2)
		k_choices.append(k_LIST)
		k = k_choices[0]
		arg_class = tf.linalg.set_diag(parameter_0,parameter_1,align=align,k=k)
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
