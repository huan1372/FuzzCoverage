#This is a Python API fuzzer for tf.einsum
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.einsum_exception.txt","a")
	try:
		parameter_0_choices = []
		parameter_0_STR_strlist = ['bnqd,bnkd->bnqk', 'ii', 'ijbn,jbnd->ibnd', '...ij,...jk->...ik', 'ij,jk->ik', 'ij->ji', 'ibh,hnd->ibnd', 'ii->i', 'i,i->', 'mbnd,mlb->lbnd', 'i,d->id', 'vki,ki->vk', 'blhd,bshd->blhs', 'ibnd,jbnd->ijbn', 'ibnd,hnd->ibh', 'blhs,bshd->blhd', 'i,j->ij', 'bij,bjk->bik', 'bcwd,bcdh->bcwh', 'ij,jk', 'lbnd,mlb->mbnd', 'bcxd,bcyd->bcxy'] 
		parameter_0_STR = parameter_0_STR_strlist[fh.get_int(min_int=0, max_int=len(parameter_0_STR_strlist)-1)]
		parameter_0_choices.append(parameter_0_STR)
		parameter_0 = parameter_0_choices[0]
		parameter_1_choices = []
		# Tensor generation for parameter_1
		parameter_1_DTYPES = [tf.int32,tf.float32]
		int_list = fh.get_int_list(min_length=2,max_length=2)
		min_Val = min(int_list) - 1
		max_Val = max(int_list)
		if min_Val % 2 == 0:
			parameter_1_tensor = fh.get_random_numeric_tensor(dtype=fh.get_tf_dtype(allowed_set=parameter_1_DTYPES))
		else:
			parameter_1_tensor = fh.get_random_numeric_tensor(min_val = min_Val, max_val = max_Val, dtype=fh.get_tf_dtype(allowed_set=parameter_1_DTYPES))
		parameter_1_tensor = tf.identity(parameter_1_tensor)
		parameter_1_choices.append(parameter_1_tensor)
		parameter_1 = parameter_1_choices[0]
		parameter_2_choices = []
		# Tensor generation for parameter_2
		parameter_2_DTYPES = [tf.float32]
		int_list = fh.get_int_list(min_length=2,max_length=2)
		min_Val = min(int_list) - 1
		max_Val = max(int_list)
		if min_Val % 2 == 0:
			parameter_2_tensor = fh.get_random_numeric_tensor(dtype=fh.get_tf_dtype(allowed_set=parameter_2_DTYPES))
		else:
			parameter_2_tensor = fh.get_random_numeric_tensor(min_val = min_Val, max_val = max_Val, dtype=fh.get_tf_dtype(allowed_set=parameter_2_DTYPES))
		parameter_2_tensor = tf.identity(parameter_2_tensor)
		parameter_2_choices.append(parameter_2_tensor)
		parameter_2 = parameter_2_choices[0]
		arg_class = tf.einsum(parameter_0,parameter_1,parameter_2)
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
