#This is a Python API fuzzer for tf.keras.layers.experimental.EinsumDense
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.keras.layers.experimental.EinsumDense_exception.txt","a")
	try:
		parameter_0_choices = []
		parameter_0_STR_strlist = ['abcdef,efg->abcdg', 'abcde,def->abcf', 'abcd,cde->abe', 'ab,bc->ac', 'abc,cd->abd', '...x,xy->...y'] 
		parameter_0_STR = parameter_0_STR_strlist[fh.get_int(min_int=0, max_int=len(parameter_0_STR_strlist)-1)]
		parameter_0_choices.append(parameter_0_STR)
		parameter_0 = parameter_0_choices[0]
		output_shape_choices = []
		output_shape_LIST = fh.get_int_list(min_length=0, max_length=4)
		output_shape_choices.append(output_shape_LIST)
		output_shape_INT = fh.get_int()
		output_shape_choices.append(output_shape_INT)
		output_shape = output_shape_choices[fh.get_int()%2]
		bias_axes_choices = []
		bias_axes_STR_strlist = ['f', 'be', 'c', 'e', 'g', 'd', 'y', 'de'] 
		bias_axes_STR = bias_axes_STR_strlist[fh.get_int(min_int=0, max_int=len(bias_axes_STR_strlist)-1)]
		bias_axes_choices.append(bias_axes_STR)
		bias_axes_None = None
		bias_axes_choices.append(bias_axes_None)
		bias_axes = bias_axes_choices[fh.get_int()%2]
		name_choices = []
		name_STR_strlist = ['attention_output'] 
		name_STR = name_STR_strlist[fh.get_int(min_int=0, max_int=len(name_STR_strlist)-1)]
		name_choices.append(name_STR)
		name = name_choices[0]
		kernel_initializer_choices = []
		kernel_initializer_TF_OBJECT_tfobjlist = ['TruncatedNormal', 'GlorotUniform'] 
		kernel_initializer_TF_OBJECT = eval("tf.keras.initializers." + {strListName}[fh.get_int(min_int=0, max_int=len({strListName})-1)])
		kernel_initializer_choices.append(kernel_initializer_TF_OBJECT)
		kernel_initializer = kernel_initializer_choices[0]
		bias_initializer_choices = []
		bias_initializer_TF_OBJECT_tfobjlist = ['Zeros'] 
		bias_initializer_TF_OBJECT = eval("tf.keras.initializers." + {strListName}[fh.get_int(min_int=0, max_int=len({strListName})-1)])
		bias_initializer_choices.append(bias_initializer_TF_OBJECT)
		bias_initializer = bias_initializer_choices[0]
		kernel_regularizer_choices = []
		kernel_regularizer_None = None
		kernel_regularizer_choices.append(kernel_regularizer_None)
		kernel_regularizer = kernel_regularizer_choices[0]
		bias_regularizer_choices = []
		bias_regularizer_None = None
		bias_regularizer_choices.append(bias_regularizer_None)
		bias_regularizer = bias_regularizer_choices[0]
		activity_regularizer_choices = []
		activity_regularizer_None = None
		activity_regularizer_choices.append(activity_regularizer_None)
		activity_regularizer = activity_regularizer_choices[0]
		kernel_constraint_choices = []
		kernel_constraint_None = None
		kernel_constraint_choices.append(kernel_constraint_None)
		kernel_constraint = kernel_constraint_choices[0]
		bias_constraint_choices = []
		bias_constraint_None = None
		bias_constraint_choices.append(bias_constraint_None)
		bias_constraint = bias_constraint_choices[0]
		equation_choices = []
		equation_STR_strlist = ['bc...,cd->bd...', 'abc,cde->abde', '...b,bc->...c', 'i,d->id', 'ab,bc->ac', 'BFNH,NHD->BFD', '...c,cde->...de', 'ab,b->a', 'abc,cd->abd', 'ibd,nd->ibn', 'bc...,cde->bde...'] 
		equation_STR = equation_STR_strlist[fh.get_int(min_int=0, max_int=len(equation_STR_strlist)-1)]
		equation_choices.append(equation_STR)
		equation = equation_choices[0]
		dtype_choices = []
		dtype = dtype_choices[fh.get_int()%0]
		arg_class = tf.keras.layers.experimental.EinsumDense(parameter_0,output_shape=output_shape,bias_axes=bias_axes,name=name,kernel_initializer=kernel_initializer,bias_initializer=bias_initializer,kernel_regularizer=kernel_regularizer,bias_regularizer=bias_regularizer,activity_regularizer=activity_regularizer,kernel_constraint=kernel_constraint,bias_constraint=bias_constraint,equation=equation,dtype=dtype)
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
