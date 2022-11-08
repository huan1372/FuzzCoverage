import sys
import pymongo
import tensorflow as tf

sys.path.insert(1, '/home/usr/FreeFuzz/FuzzCoverage/AtherisTestGenerator/')
from DataProcess.Data_Process import find_api_info
from utils.writer import Write_Code
from utils.run_Atheris import run_Atheris
from Generator.ArgTF import Argument
from Generator.ArgCode import ArgType
from utils.Results_Compare import compare_api,Filter_Exception

class Fuzzer_Generator():
    output_folder = "/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/"
    number_choices = 0
    def __init__(self,argument,func_name):
        self.argument = argument
        self.func_name = func_name
        self.code = ""

    def instrumentation_code(self):
        """This is the function to generate the instrumentation of the Fuzzer
        """
        # Comments line
        self.code += "#This is a Python API fuzzer for " + self.func_name + "\n"
        self.code += "import atheris\n"
        # instrumentation
        self.code += "with atheris.instrument_imports():\n"
        self.code += "\timport sys\n"
        self.code += "\tfrom python_fuzzing import FuzzingHelper\n"
        self.code += "\timport tensorflow as tf\n"

        return self.code

    def main_code(self):
        """Add Code for the setup part of fuzzer
        """
        self.code += "def main():\n"
        self.code += "\tatheris.Setup(sys.argv, TestOneInput, enable_python_coverage=True)\n"
        self.code += "\tatheris.Fuzz()\n"
        self.code += "\nif __name__ == \"__main__\":\n"
        self.code += "\tmain()\n"

        return self.code

    def generate_tensor_code(self,_DTYPES,parameter):
        """Generate code for a random tensor with _DTYPES type

        Args:
            _DTYPES (List): List of accepted type for the tensor
            parameter (Str): Name of the parameter
        """
        if len(_DTYPES)!=0:
            self.code += "\t\t# Tensor generation for " + parameter +"\n"
            self.code += "\t\t" + parameter + "_DTYPES = " + str(_DTYPES) + "\n"
            self.code += "\t\tint_list = fh.get_int_list(min_length=2,max_length=2)\n"
            self.code += "\t\tmin_Val = min(int_list) - 1\n"
            self.code += "\t\tmax_Val = max(int_list)\n"
            self.code += "\t\tif min_Val % 2 == 0:\n"
            self.code += "\t\t\t" + parameter + "_tensor = fh.get_random_numeric_tensor(dtype=fh.get_tf_dtype(allowed_set="+ parameter +"_DTYPES))\n"
            self.code += "\t\telse:\n"
            self.code += "\t\t\t" + parameter + "_tensor = fh.get_random_numeric_tensor(min_val = min_Val, max_val = max_Val, dtype=fh.get_tf_dtype(allowed_set="+ parameter +"_DTYPES))\n"
            self.code += "\t\t" + parameter + "_tensor = tf.identity(" + parameter + "_tensor)\n"
            self.code += "\t\t" + parameter + "_choices" + ".append(" + parameter + "_tensor)\n"
            Fuzzer_Generator.number_choices +=1
        return

    def generate_argument_code(self):
        """This function generate argument code based on type information processed in Data_process
        """
        #! FUZZING WITHOUT RESTRICT
        _TF_ACCEPT_DTYPES = [tf.bfloat16, tf.bool, tf.complex128, tf.complex64, tf.double, tf.float16, tf.float32, tf.float64, tf.half,tf.int16, tf.int32, tf.int64, tf.int8,tf.uint8, tf.uint16, tf.uint32, tf.uint64]
        if len(self.argument.keys()) == 1:
            for key,value in self.argument.items():
                parameter = key.replace(":","_")
                if parameter == "parameter_0":
                    if len(value) == 1:
                        for argument in value:
                            argument_type = argument.get_type()
                            if argument_type == ArgType.NULL:
                                self.code += "\t\t" + parameter +"_choices"+ " = []\n"
                                Fuzzer_Generator.number_choices = 0
                                var_name = parameter + "_" + str(argument)
                                self.code += "\t\t" + argument.to_code(var_name=var_name)
                                self.code += "\t\t" + parameter + "_choices" + ".append(" + var_name + ")\n"
                                Fuzzer_Generator.number_choices +=1
                                self.generate_tensor_code(_TF_ACCEPT_DTYPES,parameter)
                                self.code += "\t\t" + parameter + " = " + parameter + "_choices[fh.get_int()%" + str(Fuzzer_Generator.number_choices) + "]\n"
                                return
        for key,value in self.argument.items():
            _DTYPES = []
            # _DTYPES_2 = ["tf.bfloat16", "tf.float32", "tf.float64", "tf.int32", "tf.int64", "tf.complex64", "tf.complex128"]
            Fuzzer_Generator.number_choices = 0
            parameter = key.replace(":","_")
            self.code += "\t\t" + parameter +"_choices"+ " = []\n"
            for argument in value:
                argument_type = argument.get_type() 
                if argument_type == ArgType.TF_TENSOR:
                    _DTYPES.append(argument.get_dtype())
                elif argument_type  in [ArgType.INT,ArgType.FLOAT,ArgType.BOOL,ArgType.STR,ArgType.LIST,ArgType.NULL,ArgType.TF_DTYPE,ArgType.TF_OBJECT,ArgType.DICT]:
                    var_name = parameter + "_" + str(argument)
                    self.code += "\t\t" + argument.to_code(var_name=var_name)
                    self.code += "\t\t" + parameter + "_choices" + ".append(" + var_name + ")\n"
                    Fuzzer_Generator.number_choices +=1
                else:
                    raise Exception("Code generation not implemented for {}".format(argument.get_type()))
            if len(_DTYPES) != 0:
                self.generate_tensor_code(_TF_ACCEPT_DTYPES,parameter)
            #self.generate_tensor_code(_DTYPES,parameter)
            if  Fuzzer_Generator.number_choices == 1:
                self.code += "\t\t" + parameter + " = " + parameter + "_choices[0]\n"
            else:
                self.code += "\t\t" + parameter + " = " + parameter + "_choices[fh.get_int()%" + str(Fuzzer_Generator.number_choices) + "]\n"
        return
    def generate_api_call_code(self):
        self.code += "\t\targ_class = " + self.func_name + "("
        i= 0
        length = len(self.argument.keys()) - 1
        if "parameter:0" in self.argument.keys():
            self.code += "parameter_0,"
        for key in self.argument.keys():
            parameter = key.replace(":","_")
            if parameter=="input_signature" or parameter.startswith("parameter"):
                i+=1
                continue
            self.code += parameter + "="
            self.code += parameter
            if i!=length:
                self.code += ","
            i+=1
        self.code += ")\n"
        '''
        if "input_signature" in self.argument.keys():
            self.generate_api_input_code()
        '''
        return
    def generate_api_input_code(self):
        self.code += "\t\targ_input = [input_signature,]\n"
        self.code += "\t\t_ = arg_class(*arg_input)\n"

    def fuzz_target_code(self):
        """Function to generate TestOneInput
        """
        self.code += "def TestOneInput(data):\n"
        self.code += "\tfh = FuzzingHelper(data)\n"
        self.code += "\tf = open(" + "\"" + Fuzzer_Generator.output_folder + "Exceptions/"+ self.func_name + "_exception.txt" + "\",\"a\")\n"
        self.code += "\ttry:\n"
        self.generate_argument_code()
        self.generate_api_call_code()
        # self.code += "\t\t\n"
        self.code += "\texcept Exception as e:\n"
        self.code += "\t\texception_type, exception_object, exception_traceback = sys.exc_info()\n"
        self.code += "\t\tline_number = str(exception_traceback.tb_lineno)\n"
        self.code += "\t\tf.write(str(e) + line_number + \"\\n\")\n"
        self.code += "\tf.close()\n"

        return

    def generate_code(self):
        self.instrumentation_code()
        self.fuzz_target_code()
        self.main_code()
        return

    def write_fuzzer(self):
        file_name = Fuzzer_Generator.output_folder + "/Tests/"+ self.func_name + "_fuzz.py"
        Write_Code(content=self.code,file_name=file_name)

    def run_code(self):
        if self.code == "":
            raise Exception("Please generate fuzzer code first")
        else:
            file_path = Fuzzer_Generator.output_folder + "Tests/"
            coverage_path = Fuzzer_Generator.output_folder + "CovReport/"
            run_Atheris(func_name=self.func_name,file_path=file_path,coverage_path=coverage_path)

    def compare_difference(self):
        import os
        file_name = self.func_name+"_1000.coverage"
        Auto_folder =  Fuzzer_Generator.output_folder + "CovReport/"
        Manual_folder = "/home/usr/FreeFuzz/FuzzCoverage/Atheris/Results/"
        os.system("diff " + Auto_folder+file_name + " " + Manual_folder + file_name)


def run_all(DB):
    with open('/home/usr/FreeFuzz/FuzzCoverage/AtherisTestGenerator/random_api_list_50.txt') as f:
        for i in f.readlines():
            api_name = i.rstrip()
            print(api_name)
            argument = find_api_info(DB,api_name)
            fuzzer_generator = Fuzzer_Generator(argument=argument,func_name=api_name)
            code = fuzzer_generator.generate_code()
            fuzzer_generator.write_fuzzer()
            fuzzer_generator.run_code()
            compare_api(api_name)
            Filter_Exception(api_name)

def print_dict(x):
    for key,value in x.items():
        print("====================================================")
        print(key)
        for i in value:
            print(i,end="  ")
        print()
def run_single(api_name,DB):
    argument = find_api_info(DB,api_name)
    #print_dict(argument)
    fuzzer_generator = Fuzzer_Generator(argument=argument,func_name=api_name)
    code = fuzzer_generator.generate_code()
    fuzzer_generator.write_fuzzer()
    fuzzer_generator.run_code()
    compare_api(api_name)
    Filter_Exception(api_name)

if __name__ == "__main__":
    # database configuration
    host = "127.0.0.1"
    port = 27017
    api_name = "tf.custom_gradient"
    #api_name = "tf.custom_gradient"
    #api_name = "tf.keras.layers.PReLU"
    #api_name = "tf.dtypes.cast"
    #api_name = "tf.keras.layers.Conv1D"
    #api_name = "tf.nest.flatten"
    #api_name = "tf.keras.layers.Dense"
    DB = pymongo.MongoClient(host, port)["freefuzz-tf"]
    API_Info = {}
    #run_all(DB)
    run_single(api_name=api_name,DB=DB)
    # find_api_list(DB)print(argument)
    # fuzzer_generator.run_code()
    #fuzzer_generator.compare_difference()
