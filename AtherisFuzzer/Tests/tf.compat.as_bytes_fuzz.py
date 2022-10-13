#This is a Python API fuzzer for tf.compat.as_bytes
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.compat.as_bytes_exception.txt","a")
	try:
		parameter_0_choices = []
		parameter_0_STR_strlist = ['tfhub_module.pb', '/tmp/tfhub_modules/f591ba671b05004f8d321dc431aa264a1ed374cc'] 
		parameter_0_STR = parameter_0_STR_strlist[fh.get_int(min_int=0, max_int=len(parameter_0_STR_strlist)]
		parameter_0_choices.append(parameter_0_STR)
		parameter_0 = parameter_0_choices[fh.get_int()%1]
		_ = tf.compat.as_bytes(parameter_0)
	except Exception as e:
		f.write(str(e) + "\n")
	f.close()
def main():
	atheris.Setup(sys.argv, TestOneInput, enable_python_coverage=True)
	atheris.Fuzz()

if __name__ == "__main__":
	main()