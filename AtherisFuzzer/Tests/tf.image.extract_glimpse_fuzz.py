#This is a Python API fuzzer for tf.image.extract_glimpse
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.image.extract_glimpse_exception.txt","a")
	try:
		parameter_0_choices = []
		parameter_0 = parameter_0_choices[fh.get_int()%0]
		size_choices = []
		size = size_choices[fh.get_int()%0]
		offsets_choices = []
		offsets = offsets_choices[fh.get_int()%0]
		centered_choices = []
		centered_STR_strlist = ['false'] 
		centered_STR = centered_STR_strlist[fh.get_int(min_int=0, max_int=len(centered_STR_strlist)]
		centered_choices.append(centered_STR)
		centered = centered_choices[fh.get_int()%1]
		normalized_choices = []
		normalized_STR_strlist = ['false'] 
		normalized_STR = normalized_STR_strlist[fh.get_int(min_int=0, max_int=len(normalized_STR_strlist)]
		normalized_choices.append(normalized_STR)
		normalized = normalized_choices[fh.get_int()%1]
		_ = tf.image.extract_glimpse(parameter_0,size=size,offsets=offsets,centered=centered,normalized=normalized)
	except Exception as e:
		f.write(str(e) + "\n")
	f.close()
def main():
	atheris.Setup(sys.argv, TestOneInput, enable_python_coverage=True)
	atheris.Fuzz()

if __name__ == "__main__":
	main()
