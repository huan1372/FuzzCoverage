#This is a Python API fuzzer for tf.keras.layers.Embedding
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.keras.layers.Embedding_exception.txt","a")
	try:
		parameter_0_choices = []
		parameter_0_INT = fh.get_int()
		parameter_0_choices.append(parameter_0_INT)
		parameter_0 = parameter_0_choices[0]
		parameter_1_choices = []
		parameter_1_INT = fh.get_int()
		parameter_1_choices.append(parameter_1_INT)
		parameter_1 = parameter_1_choices[0]
		input_length_choices = []
		input_length_INT = fh.get_int()
		input_length_choices.append(input_length_INT)
		input_length_None = None
		input_length_choices.append(input_length_None)
		input_length_LIST = fh.get_int_list(min_length=2, max_length=2)
		input_length_choices.append(input_length_LIST)
		input_length = input_length_choices[fh.get_int()%3]
		output_dim_choices = []
		output_dim_INT = fh.get_int()
		output_dim_choices.append(output_dim_INT)
		output_dim = output_dim_choices[0]
		input_dim_choices = []
		input_dim_INT = fh.get_int()
		input_dim_choices.append(input_dim_INT)
		input_dim = input_dim_choices[0]
		name_choices = []
		name_STR_strlist = ['embedding_3', 'embedding_1', 'embedding_2', 'embedding'] 
		name_STR = name_STR_strlist[fh.get_int(min_int=0, max_int=len(name_STR_strlist)-1)]
		name_choices.append(name_STR)
		name = name_choices[0]
		trainable_choices = []
		trainable_BOOL = fh.get_bool()
		trainable_choices.append(trainable_BOOL)
		trainable = trainable_choices[0]
		batch_input_shape_choices = []
		batch_input_shape_LIST = fh.get_int_list(min_length=2, max_length=3)
		batch_input_shape_choices.append(batch_input_shape_LIST)
		batch_input_shape = batch_input_shape_choices[0]
		dtype_choices = []
		dtype_STR_strlist = ['float32'] 
		dtype_STR = dtype_STR_strlist[fh.get_int(min_int=0, max_int=len(dtype_STR_strlist)-1)]
		dtype_choices.append(dtype_STR)
		dtype = dtype_choices[0]
		embeddings_initializer_choices = []
		embeddings_initializer_STR_strlist = ['RandomUniform'] 
		embeddings_initializer_STR = embeddings_initializer_STR_strlist[fh.get_int(min_int=0, max_int=len(embeddings_initializer_STR_strlist)-1)]
		embeddings_initializer_choices.append(embeddings_initializer_STR)
		embeddings_initializer = embeddings_initializer_choices[0]
		embeddings_regularizer_choices = []
		embeddings_regularizer_None = None
		embeddings_regularizer_choices.append(embeddings_regularizer_None)
		embeddings_regularizer = embeddings_regularizer_choices[0]
		activity_regularizer_choices = []
		activity_regularizer_None = None
		activity_regularizer_choices.append(activity_regularizer_None)
		activity_regularizer = activity_regularizer_choices[0]
		embeddings_constraint_choices = []
		embeddings_constraint_None = None
		embeddings_constraint_choices.append(embeddings_constraint_None)
		embeddings_constraint = embeddings_constraint_choices[0]
		mask_zero_choices = []
		mask_zero_BOOL = fh.get_bool()
		mask_zero_choices.append(mask_zero_BOOL)
		mask_zero = mask_zero_choices[0]
		arg_class = tf.keras.layers.Embedding(parameter_0,parameter_1,input_length=input_length,output_dim=output_dim,input_dim=input_dim,name=name,trainable=trainable,batch_input_shape=batch_input_shape,dtype=dtype,embeddings_initializer=embeddings_initializer,embeddings_regularizer=embeddings_regularizer,activity_regularizer=activity_regularizer,embeddings_constraint=embeddings_constraint,mask_zero=mask_zero)
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
