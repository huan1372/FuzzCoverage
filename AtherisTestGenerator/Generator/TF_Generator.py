import sys
import pymongo

sys.path.insert(1, '/home/usr/FreeFuzz/FuzzCoverage/AtherisTestGenerator/')
from DataProcess.Data_Process import find_api_info
from utils.writer import Write_Code

class Fuzzer_Generator():
    output_folder = "/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/"
    def __init__(self,argument,func_name):
        self.argument = argument
        self.func_name = func_name
        self.code = ""
    def generate_code(self):
        
        return self.code

    def write_fuzzer(self):
        file_name = Fuzzer_Generator.output_folder + self.func_name + "_fuzz.py"
        Write_Code(content=self.code,file_name=file_name)

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
