#This is a Python API fuzzer for tf.keras.utils.get_file
import atheris
with atheris.instrument_imports():
	import sys
	from python_fuzzing import FuzzingHelper
	import tensorflow as tf
def TestOneInput(data):
	fh = FuzzingHelper(data)
	f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Exceptions/tf.keras.utils.get_file_exception.txt","a")
	try:
		fname_choices = []
		fname_STR_strlist = ['image2.jpg', 'image1.jpg', 'centernet_hg104_1024x1024_coco17_tpu-32', 'mscoco_label_map.pbtxt', 'jena_climate_2009_2016.csv.zip'] 
		fname_STR = fname_STR_strlist[fh.get_int(min_int=0, max_int=len(fname_STR_strlist)-1)]
		fname_choices.append(fname_STR)
		fname = fname_choices[0]
		origin_choices = []
		origin_STR_strlist = ['https://raw.githubusercontent.com/tensorflow/models/master/research/object_detection/test_images/image2.jpg', 'http://download.tensorflow.org/models/object_detection/tf2/20200711/centernet_hg104_1024x1024_coco17_tpu-32.tar.gz', 'https://raw.githubusercontent.com/tensorflow/models/master/research/object_detection/test_images/image1.jpg', 'https://storage.googleapis.com/tensorflow/tf-keras-datasets/jena_climate_2009_2016.csv.zip', 'https://raw.githubusercontent.com/tensorflow/models/master/research/object_detection/data/mscoco_label_map.pbtxt'] 
		origin_STR = origin_STR_strlist[fh.get_int(min_int=0, max_int=len(origin_STR_strlist)-1)]
		origin_choices.append(origin_STR)
		origin = origin_choices[0]
		untar_choices = []
		untar_BOOL = fh.get_bool()
		untar_choices.append(untar_BOOL)
		untar = untar_choices[0]
		parameter_0_choices = []
		parameter_0_STR_strlist = ['starry_night.jpg', 'paris.jpg', 'YellowLabradorLooking_new.jpg'] 
		parameter_0_STR = parameter_0_STR_strlist[fh.get_int(min_int=0, max_int=len(parameter_0_STR_strlist)-1)]
		parameter_0_choices.append(parameter_0_STR)
		parameter_0 = parameter_0_choices[0]
		parameter_1_choices = []
		parameter_1_STR_strlist = ['https://i.imgur.com/F28w3Ac.jpg', 'https://i.imgur.com/9ooB60I.jpg', 'https://storage.googleapis.com/download.tensorflow.org/example_images/YellowLabradorLooking_new.jpg'] 
		parameter_1_STR = parameter_1_STR_strlist[fh.get_int(min_int=0, max_int=len(parameter_1_STR_strlist)-1)]
		parameter_1_choices.append(parameter_1_STR)
		parameter_1 = parameter_1_choices[0]
		arg_class = tf.keras.utils.get_file(fname=fname,origin=origin,untar=untar,parameter_0,parameter_1)
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
