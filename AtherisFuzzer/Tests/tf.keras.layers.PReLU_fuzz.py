#This is a Python API fuzzer for tf.keras.layers.PReLU
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.keras.layers.PReLU_exception.txt","a")
	try:
		name_choices = []
		name_STR_strlist = ['p_re_lu'] 
		name_STR = name_STR_strlist[fh.get_int(min_int=0, max_int=len(name_STR_strlist)]
		name_choices.append(name_STR)
		name = name_choices[fh.get_int()%1]
		trainable_choices = []
		trainable_STR_strlist = ['true', 'false'] 
		trainable_STR = trainable_STR_strlist[fh.get_int(min_int=0, max_int=len(trainable_STR_strlist)]
		trainable_choices.append(trainable_STR)
		trainable = trainable_choices[fh.get_int()%1]
		batch_input_shape_choices = []
		batch_input_shape = batch_input_shape_choices[fh.get_int()%0]
		dtype_choices = []
		dtype_STR_strlist = ['float32'] 
		dtype_STR = dtype_STR_strlist[fh.get_int(min_int=0, max_int=len(dtype_STR_strlist)]
		dtype_choices.append(dtype_STR)
		dtype = dtype_choices[fh.get_int()%1]
		alpha_initializer_choices = []
		alpha_initializer_STR_strlist = ['Zeros'] 
		alpha_initializer_STR = alpha_initializer_STR_strlist[fh.get_int(min_int=0, max_int=len(alpha_initializer_STR_strlist)]
		alpha_initializer_choices.append(alpha_initializer_STR)
		alpha_initializer = alpha_initializer_choices[fh.get_int()%1]
		alpha_regularizer_choices = []
		alpha_regularizer = alpha_regularizer_choices[fh.get_int()%0]
		alpha_constraint_choices = []
		alpha_constraint = alpha_constraint_choices[fh.get_int()%0]
		shared_axes_choices = []
		shared_axes_INT = fh.get_int()
		shared_axes_choices.append(shared_axes_INT)
		shared_axes = shared_axes_choices[fh.get_int()%1]
		input_signature_choices = []
		# Tensor generation for input_signature
		input_signature_DTYPES = [tf.float32]
		int_list = fh.get_int_list(min_length=2,max_length=2)
		min_Val = min(int_list) - 1
		max_Val = max(int_list)
		if min_Val % 2 == 0:
			input_signature_tensor = fh.get_random_numeric_tensor(dtype=fh.get_tf_dtype(allowed_set=input_signature_DTYPES))
		else:
			input_signature_tensor = fh.get_random_numeric_tensor(min_val = min_Val, max_val = max_Val, dtype=fh.get_tf_dtype(allowed_set=input_signature_DTYPES))
		input_signature_tensor = tf.identity(input_signature_tensor)
		input_signature_choices.append(input_signature_tensor)
		input_signature = input_signature_choices[fh.get_int()%1]
		_ = tf.keras.layers.PReLU(name=name,trainable=trainable,batch_input_shape=batch_input_shape,dtype=dtype,alpha_initializer=alpha_initializer,alpha_regularizer=alpha_regularizer,alpha_constraint=alpha_constraint,shared_axes=shared_axes,input_signature=input_signature)
	except Exception as e:
		f.write(str(e) + "\n")
	f.close()
def main():
	atheris.Setup(sys.argv, TestOneInput, enable_python_coverage=True)
	atheris.Fuzz()

if __name__ == "__main__":
	main()
