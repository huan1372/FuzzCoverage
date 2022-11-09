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
		initial_learning_rate_FLOAT_floatlist = [0.01] 
		initial_learning_rate_FLOAT_floatlist_random = fh.get_float(min_float=-255,max_float=255)

		initial_learning_rate_FLOAT_floatlist.append(initial_learning_rate_FLOAT_floatlist_random)
		initial_learning_rate_FLOAT = initial_learning_rate_FLOAT_floatlist[fh.get_int(min_int=0, max_int=len(initial_learning_rate_FLOAT_floatlist)-1)]
		initial_learning_rate_choices.append(initial_learning_rate_FLOAT)
		initial_learning_rate_INT_intlist = [100] 
		initial_learning_rate_INT_intlist_random = fh.get_int(min_int=-255,max_int=255)

		initial_learning_rate_INT_intlist.append(initial_learning_rate_INT_intlist_random)
		initial_learning_rate_INT = initial_learning_rate_INT_intlist[fh.get_int(min_int=0, max_int=len(initial_learning_rate_INT_intlist)-1)]
		initial_learning_rate_choices.append(initial_learning_rate_INT)
		initial_learning_rate = initial_learning_rate_choices[fh.get_int()%2]
		decay_steps_choices = []
		decay_steps_INT_intlist = [100, 20] 
		decay_steps_INT_intlist_random = fh.get_int(min_int=-255,max_int=255)

		decay_steps_INT_intlist.append(decay_steps_INT_intlist_random)
		decay_steps_INT = decay_steps_INT_intlist[fh.get_int(min_int=0, max_int=len(decay_steps_INT_intlist)-1)]
		decay_steps_choices.append(decay_steps_INT)
		decay_steps = decay_steps_choices[0]
		decay_rate_choices = []
		decay_rate_FLOAT_floatlist = [0.1, 0.96] 
		decay_rate_FLOAT_floatlist_random = fh.get_float(min_float=-255,max_float=255)

		decay_rate_FLOAT_floatlist.append(decay_rate_FLOAT_floatlist_random)
		decay_rate_FLOAT = decay_rate_FLOAT_floatlist[fh.get_int(min_int=0, max_int=len(decay_rate_FLOAT_floatlist)-1)]
		decay_rate_choices.append(decay_rate_FLOAT)
		decay_rate = decay_rate_choices[0]
		input_signature_choices = []
		# Tensor generation for input_signature
		input_signature_DTYPES = [tf.bfloat16, tf.bool, tf.complex128, tf.complex64, tf.float64, tf.float16, tf.float32, tf.float64, tf.float16, tf.int16, tf.int32, tf.int64, tf.int8, tf.uint8, tf.uint16, tf.uint32, tf.uint64]
		int_list = fh.get_int_list(min_length=2,max_length=2)
		min_Val = min(int_list) - 1
		max_Val = max(int_list)
		if min_Val % 2 == 0:
			input_signature_tensor = fh.get_random_numeric_tensor(dtype=fh.get_tf_dtype(allowed_set=input_signature_DTYPES))
		else:
			input_signature_tensor = fh.get_random_numeric_tensor(min_val = min_Val, max_val = max_Val, dtype=fh.get_tf_dtype(allowed_set=input_signature_DTYPES))
		input_signature_tensor = tf.identity(input_signature_tensor)
		input_signature_choices.append(input_signature_tensor)
		input_signature = input_signature_choices[0]
		arg_class = tf.keras.optimizers.schedules.ExponentialDecay(initial_learning_rate=initial_learning_rate,decay_steps=decay_steps,decay_rate=decay_rate,)
		arg_input = [input_signature,]
		final_output = arg_class(*arg_input)
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
