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
		parameter_0_STR_strlist = ['ij,jk', '...ij,...jk->...ik', 'ii', 'ibnd,jbnd->ijbn', 'i,d->id', 'ii->i', 'bcxd,bcyd->bcxy', 'blhd,bshd->blhs', 'lbnd,mlb->mbnd', 'blhs,bshd->blhd', 'bij,bjk->bik', 'bnqd,bnkd->bnqk', 'bcwd,bcdh->bcwh', 'ij->ji', 'ij,jk->ik', 'mbnd,mlb->lbnd', 'i,i->', 'vki,ki->vk', 'i,j->ij', 'ibnd,hnd->ibh', 'ibh,hnd->ibnd', 'ijbn,jbnd->ibnd'] 
		parameter_0_STR = parameter_0_STR_strlist[fh.get_int(min_int=0, max_int=len(parameter_0_STR_strlist)]
		parameter_0_choices.append(parameter_0_STR)
		parameter_0 = parameter_0_choices[fh.get_int()%1]
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
		parameter_1 = parameter_1_choices[fh.get_int()%1]
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
		parameter_2 = parameter_2_choices[fh.get_int()%1]
		_ = tf.einsum(parameter_0,parameter_1,parameter_2)
	except Exception as e:
		f.write(str(e) + "\n")
	f.close()
def main():
	atheris.Setup(sys.argv, TestOneInput, enable_python_coverage=True)
	atheris.Fuzz()

if __name__ == "__main__":
	main()
