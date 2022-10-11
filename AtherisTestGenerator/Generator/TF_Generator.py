from operator import imod
from re import A
from symbol import parameters
import sys
import pymongo

sys.path.insert(1, '/home/usr/FreeFuzz/FuzzCoverage/AtherisTestGenerator/')
from DataProcess.Data_Process import find_api_info
from utils.writer import Write_Code
from utils.run_Atheris import run_Atheris
from Generator.ArgTF import Argument
from Generator.ArgCode import ArgType

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
            self.code += "\t\t" + parameter + "_DTYPES = ["
            for i in _DTYPES:
                self.code += i
                self.code += ","
            self.code +="]\n"
            self.code += "\t\tint_list = fh.get_int_list(min_length=2,max_length=2)\n"
            self.code += "\t\tmin_Val = min(int_list)\n"
            self.code += "\t\tmax_Val = max(int_list)\n"
            self.code += "\t\tif min_Val % 2 == 0:\n"
            self.code += "\t\t\t" + parameter + "_tensor = fh.get_random_numeric_tensor(dtype=fh.get_tf_dtype(allowed_set="+ parameter +"_DTYPES))\n"
            self.code += "\t\telse:\n"
            self.code += "\t\t\t" + parameter + "_tensor = fh.get_random_numeric_tensor(min_val = min_Val, max_val = max_Val, dtype=fh.get_tf_dtype(allowed_set="+ parameter +"_DTYPES))\n"
            self.code += "\t\t" + parameter + "_tensor = tf.saturate_cast(" + parameter + "_tensor,dtype=fh.get_tf_dtype(allowed_set="+ parameter +"_DTYPES))\n"
            self.code += "\t\t" + parameter + "_choices" + ".append(" + parameter + "_tensor)\n"
            Fuzzer_Generator.number_choices +=1
        return

    def generate_argument_code(self):
        """This function generate argument code based on type information processed in Data_process
        """
        for key,value in self.argument.items():
            _DTYPES = []
            Fuzzer_Generator.number_choices = 0
            parameter = key.replace(":","_")
            self.code += "\t\t" + parameter +"_choices"+ " = []\n"
            for argument in value:
                if argument.get_type() == ArgType.TF_TENSOR:
                    _DTYPES.append(argument.get_dtype())
                elif argument.get_type() in [ArgType.INT,ArgType.FLOAT,ArgType.BOOL,ArgType.STR]:
                    var_name = parameter + "_" + str(argument)
                    self.code += "\t\t" + argument.to_code(var_name=var_name)
                    self.code += "\t\t" + parameter + "_choices" + ".append(" + var_name + ")\n"
                    Fuzzer_Generator.number_choices +=1
                else:
                    raise Exception("Code generation not implemented for {}".format(argument.get_type()))
            self.generate_tensor_code(_DTYPES,parameter)
            self.code += "\t\t" + parameter + " = " + parameter + "_choices[fh.get_int()%" + str(Fuzzer_Generator.number_choices) + "]\n"
        return
    def generate_api_call_code(self):
        self.code += "\t\t_ = " + self.func_name + "("
        for key in self.argument.keys():
            parameter = key.replace(":","_")
            self.code += parameter
            self.code += ","
        self.code += ")\n"
        return
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
        self.code += "\t\tf.write(e)\n"
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
        if code == "":
            raise Exception("Please generate fuzzer code first")
        else:
            file_path = Fuzzer_Generator.output_folder + "/Tests/"
            coverage_path = Fuzzer_Generator.output_folder + "/CovReport/"
            run_Atheris(func_name=self.func_name,file_path=file_path,coverage_path=coverage_path)

if __name__ == "__main__":
    # database configuration
    host = "127.0.0.1"
    port = 27017
    api_name = "tf.abs"
    DB = pymongo.MongoClient(host, port)["freefuzz-tf"]
    API_Info = {}
    # find_api_list(DB)
    argument = find_api_info(DB,api_name)
    fuzzer_generator = Fuzzer_Generator(argument=argument,func_name=api_name)
    code = fuzzer_generator.generate_code()
    fuzzer_generator.write_fuzzer()
    fuzzer_generator.run_code()