import tensorflow as tf
from enum import IntEnum
import re
import sys
import io

#* Type for testcase
class ArgType(IntEnum):
    INT = 1
    STR = 2
    FLOAT = 3
    BOOL = 4
    TUPLE = 5
    LIST = 6
    NULL = 7
    DICT = 8
    TF_TENSOR = 9
    TF_DTYPE = 10
    KERAS_TENSOR = 11
    TF_VARIABLE = 12
    TF_OBJECT = 13
    OTHER = 24

#* Modes to parse different part of comments
#* IDLE: No Info to parse
#* EXAMPLE: Curent line is example code
#* ARGS: Curent line is in argument definition
class ParseMode(IntEnum):
    IDLE = 0
    EXAMPLE = 1
    ARGS = 2    

class Testcase:
    def __init__(self):
        self.record = {}
    
    def add_argument(self,argname:str,argtype:ArgType,argvalue=None):
        self.record[argname] = (argtype,argvalue)

    def get_arg(self,argname:str):
        if argname not in self.record.keys():
            raise Exception(f"%s is not an argument"%(argname))
        return self.record[argname]
class Tensor:
    def __init__(self,dtype,shape=[]):
        self.dtype = dtype
        self.shape = shape
        
class TFAPI:
    def __init__(self,api_name,default=False):
        self.default = default
        self.default_val = {}
        self.api_name = api_name
        self.Testcase = []
        self.mode = ParseMode.IDLE

    def add_testcase(self,testcase:Testcase):
        self.Testcase.append(testcase)
    
    def parse_args(self,arglist:list):
        for item in arglist:
            if "=" in item:
                argname,default_v = item.split("=")
                default = True
                self.default = True
                default_v = self.parse_default_type(default_v)
            else:
                argname,default_v = item,None
                default = False
            self.default_val[argname] = (default,default_v)
            

    def set_mode(self,mode:ParseMode):
        self.mode = mode   

    def parse_default_type(self,type_info):
        if type_info == "None":
            return (ArgType.NULL,"None")
        else:
            print(type_info)
        
    def parse_line(self,line:str):
        if self.mode == ParseMode.IDLE:
            return
        elif self.mode == ParseMode.EXAMPLE:
            if line.startswith(">>>"):
                line_l = line.lstrip(">>> ")
                if line_l.startswith("#"):
                    return
                else:
                    return
    def get_default_value(self,argname:str):
        if self.default:
            if self.default_val[argname][0]:
                return self.default_val[argname][1]
            else:
                return None
        else:
            raise Exception("No default value for %s "%(self.argname))


API_DOC_DIR = "/Users/sh69/Documents/FreeFuzz/FuzzCoverage/DataBaseFetch/API_Doc/"

# func for parse information could be used by Atheris
# def process_type(argname,type_info,record,api_name):
#     # Raw type
#     if argname not in record.keys():
#         record[argname] = set()

#     #? There is Data with list/int not string when parsing
#     if isinstance(type_info,list):
#         record[argname].add((ArgType.LIST,"raw"))
#         return record
#     if isinstance(type_info,int):
#         record[argname].add((ArgType.INT,"raw"))
#         return record
#     if isinstance(type_info,float):
#         record[argname].add((ArgType.FLOAT,"raw"))
#         return record
#     if isinstance(type_info,str):
#         if type_info == "none":
#             record[argname].add((ArgType.NULL,"raw"))
#         else:
#             record[argname].add((ArgType.STR,"raw"))
#         return record
#     if isinstance(type_info,dict):
#         if "dtype" in type_info.keys() and "type" in type_info.keys() and type_info["type"] == "tensor":
#             record[argname].add((ArgType.TF_TENSOR,type_info["dtype"]))
#         return record
#     if type_info is None:
#         record[argname].add((ArgType.NULL,"raw"))
#         return record
#     print(argname,type(type_info),api_name)  
#     return

# func to parse information used by FreeFuzz
def parse_FreeFuzz_type(tf_api,testcase,argname,type_info):
    # Raw type
    if argname in testcase.record.keys():
        raise Exception("Two input definition in ONE testcase")

    #? There is Data with list/int not string when parsing
    if isinstance(type_info,list):
        testcase.add_argument(argname,ArgType.LIST,type_info)
        return 
    if isinstance(type_info,int):
        testcase.add_argument(argname,ArgType.INT,type_info)
        return 
    if isinstance(type_info,float):
        testcase.add_argument(argname,ArgType.FLOAT,type_info)
        return
    if isinstance(type_info,str):
        if type_info == "none":
            testcase.add_argument(argname,ArgType.NULL,"None")
        else:
            testcase.add_argument(argname,ArgType.STR,type_info)
        return 
    if isinstance(type_info,dict):
        if "dtype" in type_info.keys() and "type" in type_info.keys() and (type_info["type"] == "tensor" or type_info["type"]=="KerasTensor"):
            testcase.add_argument(argname,ArgType.TF_TENSOR,Tensor(type_info["dtype"],type_info["shape"]))
        return 
    if type_info is None:
        testcase.add_argument(argname,ArgType.NULL,"None")
        return 
    print(argname,type(type_info),tf_api.api_name)  
    return
def FreeFuzz_Data_Collection():
    import pymongo
    host = "127.0.0.1"
    port = 27017
    database_name = "freefuzz-tf"
    results = {}
    DB = pymongo.MongoClient(host=host,port=port)[database_name]
    with open("/Users/sh69/Documents/FreeFuzz/FuzzCoverage/DataBaseFetch/random_api_list_50.txt") as f:
        for line in f.readlines():
            api_name = line.rstrip()
            records = DB[api_name].find({}, {"_id": 0})
            tf_api = TFAPI(api_name=api_name)
            for doc in records:
                testcase = Testcase()
                for key,value in doc.items():
                    value_r = value
                    #print(api_name,key,value_r)
                    if key=="output_signature":
                        continue
                    if key=="input_signature":
                        try:
                            if len(value) == 0:
                                value_r = "none"
                            else:
                                value_r = value[0]
                        except KeyError:
                            print(value)
                            continue
                    parse_FreeFuzz_type(tf_api,testcase,key,value_r)
                    #process_type(key,value_r,api_name)
                tf_api.add_testcase(testcase)
            results[api_name] = tf_api
    return results

def capture_string(api_name):
    # Temporarily redirect stdout to a StringIO.
    stdout = sys.stdout
    s = io.StringIO()
    sys.stdout = s
    help(eval(api_name))

    # Don't forget to reset stdout!
    sys.stdout = stdout

    # Read the StringIO for the help message.
    s.seek(0)
    help_string = s.read()
    return help_string

def Filter_Info(help_msg:str):
    SentenceList = re.split(r"\n+",help_msg)
    SentenceList = list(filter(str.strip, SentenceList))
    SentenceList = [i.strip() for i in SentenceList]
    return SentenceList

def Write_API_Doc(api_name,DocList,Doc_DIR=API_DOC_DIR):
    out_f = open(Doc_DIR+api_name,"w")
    for line in DocList:
        out_f.write(line+"\n")
    out_f.close()
    return

def TF_doc_Collection():
    Api_Doc = {}
    with open("/Users/sh69/Documents/FreeFuzz/FuzzCoverage/DataBaseFetch/api_full_list.txt") as f:
        for line in f.readlines():
            api_name = line.rstrip()
            helper_msg = capture_string(api_name)
            Api_Doc[api_name] = Filter_Info(helper_msg)
            Write_API_Doc(api_name,Api_Doc[api_name])
    return Api_Doc

def Fetch_func_module(helpdefinestr):
    found = re.search("Help on function (\w+) in module ([\w|.]+):",helpdefinestr)
    return found.group(1),found.group(2)

def Fetch_argsname(func_name,apidefstr):
    if not apidefstr.startswith(func_name):
        raise Exception(f"There is no func definition for %s",api_name)
    arglist = re.search(func_name+"\((.+)\)",apidefstr).group(1).split(", ")
    return arglist

def Fetch_API_Info(api_name,api_doc_dir=API_DOC_DIR):
    api_doc_f = open(api_doc_dir + api_name)
    
    #? Fetch func name 
    func_name, module_name = Fetch_func_module(api_doc_f.readline().rstrip())
    
    #? Fetch and store func definition 
    #? Added argument information to TFAPI class
    args = Fetch_argsname(func_name,api_doc_f.readline().rstrip())
    tf_api = TFAPI(api_name)
    tf_api.parse_args(args)

    #! Main part of Analysis
    #! Currently neglect anything besides For example code + Args comments
    # for line in api_doc_f.readlines():
    #     if line.strip() == "For example:":
    #         tf_api.set_mode(ParseMode.EXAMPLE)
    #         continue
    #     elif line.strip() == "Args:":
    #         tf_api.set_mode(ParseMode.ARGS)
    #         continue
    #     tf_api.parse_line(line)
    
    api_doc_f.close()
    
    return tf_api

if __name__ == "__main__": 
    FreeFuzzresults = FreeFuzz_Data_Collection()
    #HelperDoc = TF_doc_Collection()
    api_name = "tf.abs"
    Fetch_API_Info(api_name)
    print("a")