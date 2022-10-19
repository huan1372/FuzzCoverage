#This is a Python API fuzzer for tf.keras.layers.MultiHeadAttention
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.keras.layers.MultiHeadAttention_exception.txt","a")
	try:
		key_dim_choices = []
		key_dim_INT = fh.get_int()
		key_dim_choices.append(key_dim_INT)
		key_dim = key_dim_choices[0]
		num_heads_choices = []
		num_heads_INT = fh.get_int()
		num_heads_choices.append(num_heads_INT)
		num_heads = num_heads_choices[0]
		dropout_choices = []
		dropout_FLOAT = fh.get_float()
		dropout_choices.append(dropout_FLOAT)
		dropout = dropout_choices[0]
		arg_class = tf.keras.layers.MultiHeadAttention(key_dim=key_dim,num_heads=num_heads,dropout=dropout)
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
