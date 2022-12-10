import tensorflow as tf
from enum import Enum,IntEnum
import re
import sys
import io
import copy
import os
import json
API_DOC_DIR = "/Users/sh69/Documents/FreeFuzz/FuzzCoverage/DataBaseFetch/API_Doc/"
API_DOC_ERR_DIR = "/Users/sh69/Documents/FreeFuzz/FuzzCoverage/DataBaseFetch/API_Failed_Doc/"
TENSOR_TYPE_List = ["bfloat16","half","float16","float32","float64","int8","int16","int32","int64","complex64","complex128","uint8","uint16","uint32","uint64","qint8", "quint8", "qint16", "quint16", "qint32"]
DType_List = ["tf.bfloat16", "tf.half", "tf.float32", "tf.float64", "tf.int64", "tf.int32", "tf.uint8", "tf.uint16", "tf.uint32", "tf.uint64", "tf.int8", "tf.int16", "tf.complex64", "tf.complex128", "tf.qint8", "tf.quint8", "tf.qint16", "tf.quint16", "tf.qint32"]
#* Type for testcase
class ArgType(str,Enum):
    INT = "int"
    STR = "str"
    FLOAT = "float"
    BOOL = "bool"
    TUPLE = "tuple"
    LIST = "list"
    NULL = "null"
    DICT = "dict"
    TF_TENSOR = "tf tensor"
    TF_DTYPE = "dtyoe"
    KERAS_TENSOR = "keras tensor"
    TF_VARIABLE = "variable"
    TF_OBJECT = "tf object"
    NPARRAY = "np array"
    OTHER = "other"

#* Modes to parse different part of comments
#* IDLE: No Info to parse
#* EXAMPLE: Curent line is example code
#* ARGS: Curent line is in argument definition
class ParseMode(IntEnum):
    IDLE = 0
    EXAMPLE_S = 1
    EXAMPLE_E = 2
    ARGS = 3
    RETURN = 5

def find_types(line,dtypes,TYPE_List):
    dtypes = set(dtypes)
    for type in TYPE_List:
        if type in line:
            dtypes.add(type)
    return list(dtypes)

class Testcase:
    def __init__(self):
        self.record = {}
        self.comments = ""
        self.api_call_code = ""

    def add_argument(self,argname:str,argtype:ArgType,argvalue=None):
        self.record[argname] = {"type":argtype,"value":argvalue}

    def add_comments(self,comment:str):
        self.comments += comment

    def set_api_call_code(self,code:str):
        self.api_call_code = code

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
        #self.default_val = {}
        self.ArgInfo = {}
        self.api_name = api_name
        self.Testcase = []
        self.mode = ParseMode.IDLE
        self.cur_testcase = None
        self.cur_argname = None
        self.DIR = "/Users/sh69/Documents/FreeFuzz/FuzzCoverage/DataBaseFetch/API_Json/"

    def add_testcase(self,testcase:Testcase):
        self.Testcase.append(testcase)
    
    def parse_args(self,arglist:list):
        for item in arglist:
            if "=" in item:
                argname,default_v = item.split("=",1)
                default = True
                self.default = True
                default_v3 = self.parse_default_type(default_v)
                default_v = {"type":default_v3[0],"value":default_v3[1]}
            else:
                argname,default_v = item,None
                default = False
            self.ArgInfo[argname] = {}
            self.ArgInfo[argname]["defaultInfo"] = {"default" : default,"default_value": default_v}
            

    def set_mode(self,mode:ParseMode):
        self.mode = mode   

    def parse_default_type(self,type_info):
        if type_info == "None":
            return (ArgType.NULL,"None")
        elif type_info == "False" or type_info == "True":
            return (ArgType.BOOL,type_info)
        elif isinstance(type_info,int):
            return (ArgType.INT,int(type_info))
        elif isinstance(type_info,str):
            return (ArgType.STR,type_info)
        else:
            print(type_info)
        
    def parse_line(self,line:str):
        disp = ""
        if self.mode == ParseMode.IDLE or self.mode == ParseMode.RETURN:
            return
        elif self.mode == ParseMode.EXAMPLE_S or self.mode == ParseMode.EXAMPLE_E :
            # Code 
            if line.startswith(">>>"):
                if self.mode == ParseMode.EXAMPLE_S:
                    self.cur_testcase = Testcase()
                    self.set_mode(ParseMode.EXAMPLE_E)
                line_l = line.lstrip(">>> ")
                if line_l.startswith("#"):
                    #? Comments of excute code
                    self.cur_testcase.add_comments(line_l.lstrip("# "))
                else:
                    if self.api_name in line_l:
                        self.cur_testcase.set_api_call_code(line_l.strip())
                    elif "=" in line_l:
                        code = line_l.strip().split("=",1)
                        argname = code[0].strip(" ")
                        # if argname not in self.ArgInfo.keys():
                        #     print(argname)
                        #     raise Exception("Argument not found!")
                        argval = code[1].strip(" ")
                        self.cur_testcase.add_argument(argname,ArgType.OTHER,argval)
            # OUTPUT Stage -> add testcase, set to accept next round testcase
            else:
                if self.cur_testcase == None:
                    return
                if line.startswith("Traceback") or self.cur_testcase.api_call_code == "" :
                    self.set_mode(ParseMode.EXAMPLE_S)
                    self.cur_testcase = None
                elif self.cur_testcase != None:
                    self.Testcase.append(copy.deepcopy(self.cur_testcase))
                    self.cur_testcase = None
                    self.set_mode(ParseMode.EXAMPLE_S)
            return
        elif self.mode == ParseMode.ARGS:
            if ":" in line:
                found = re.search("^(\w+):(.+)",line)
                if found != None:
                    argname = found.group(1)
                    argname = "**" + argname if argname == "kwargs" else argname
                    disp = found.group(2)
                    if argname not in self.ArgInfo.keys() :
                        if argname == "inputs" or "**kwargs" in self.ArgInfo.keys():
                            self.cur_argname = argname
                            self.ArgInfo[self.cur_argname] = {}
                        else:
                            print(argname)
                            raise Exception("Argument not found!")
                    else:
                        self.cur_argname = argname
            
            if "Tensor" in line or "SparseTensor" in line:
                dtypes = find_types(line,[],TENSOR_TYPE_List)
                self.ArgInfo[self.cur_argname]["tensor"] = dtypes
            elif "tensor" in self.ArgInfo[self.cur_argname].keys():
                dtypes = find_types(line, self.ArgInfo[self.cur_argname]["tensor"],TENSOR_TYPE_List)
                self.ArgInfo[self.cur_argname]["tensor"] = dtypes
            elif "tf.DType" in line:
                dtypes = find_types(line,[],DType_List)
                self.ArgInfo[self.cur_argname]["tf.DType"] = dtypes
            elif "tf.DType" in self.ArgInfo[self.cur_argname].keys():
                dtypes = find_types(line, self.ArgInfo[self.cur_argname]["tf.DType"],DType_List)
                self.ArgInfo[self.cur_argname]["tf.DType"] = dtypes
            elif "(optional)" in line or "(optional" in line:
                self.ArgInfo[self.cur_argname]["optional"] = "True"
            elif "string" in line:
                self.ArgInfo[self.cur_argname]["string"] = disp if disp != "" else line
            elif "`bytes`" in line:
                self.ArgInfo[self.cur_argname]["bytes"] = disp if disp != "" else line
            else:
                print(line)
            return

    def get_default_value(self,argname:str):
        if self.default:
            if self.ArgInfo[argname]["defaultInfo"]["default"]:
                return self.ArgInfo[argname]["defaultInfo"]["default_value"]
            else:
                return None
        else:
            raise Exception("No default value for %s "%(self.argname))
    
    def generate_json(self,dir=None):
        json_dir = dir if dir != None else self.DIR + api_name + "/"
        if os.path.isdir(json_dir):
            for f in os.listdir(json_dir):
                os.remove(os.path.join(json_dir, f)) 
        else:
            os.makedirs(json_dir)
        #? General Info:
        #?      Default Value
        #?      Args Type
        with open(json_dir+"General.json","w") as Genf:
            gen_obj = json.dumps(self.ArgInfo, indent=4)
            Genf.write(gen_obj)
        for i in range(len(self.Testcase)):
            filename = json_dir+"Testcase" + str(i+1) + ".json"
            testcase = self.Testcase[i]
            testcase_dict = {"api call code":testcase.api_call_code,"comments":testcase.comments,"Arguments":testcase.record}
            testcase_obj = json.dumps(testcase_dict, indent=4)
            with open(filename,"w") as testcase_f:
                testcase_f.write(testcase_obj)
        return





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
        elif "type" in type_info.keys() and type_info["type"] == "tf_object":
            testcase.add_argument(argname,ArgType.TF_OBJECT,type_info["value"])
        elif "type" in type_info.keys() and type_info["type"] == "nparray":
            testcase.add_argument(argname,ArgType.NPARRAY,Tensor(type_info["dtype"],type_info["shape"]))
        elif "type" in type_info.keys() and type_info["type"] == "DType":
            testcase.add_argument(argname,ArgType.TF_DTYPE,type_info["value"])
        elif "dtype" in type_info.keys() and "type" in type_info.keys() and type_info["type"] == "variable" :
            testcase.add_argument(argname,ArgType.TF_VARIABLE,Tensor(type_info["dtype"],type_info["shape"]))
        elif "type" in type_info.keys() and type_info["type"] == "other":
            testcase.add_argument(argname,ArgType.OTHER,type_info["value"])
        else:
            testcase.add_argument(argname,ArgType.OTHER,type_info)
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
    with open("/Users/sh69/Documents/FreeFuzz/FuzzCoverage/DataBaseFetch/api_full_list.txt") as f:
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
    if found == None:
        found = re.search("Help on class (\w+) in module ([\w|.]+):",helpdefinestr)
        return found.group(1),found.group(2),False
    else:
        return found.group(1),found.group(2),True

def Fetch_argsname(func_name,apidefstr):
    if not apidefstr.startswith(func_name):
        raise Exception(f"There is no func definition for %s",api_name)
    found = re.search(func_name+"\((.+)\)",apidefstr)
    if found != None:
        arglist = found.group(1).split(", ")
        return arglist
    else:
        found = re.search(func_name+"\(\)",apidefstr)
        if found != None:
            return []
        else:
            raise Exception("No definition of inputs")

def Fetch_API_Info(api_name,api_doc_dir=API_DOC_DIR):
    api_doc_f = open(api_doc_dir + api_name)
    
    #? Fetch func name 
    func_name, module_name, flag = Fetch_func_module(api_doc_f.readline().rstrip())
    
    #? Fetch and store func definition 
    #? Added argument information to TFAPI class
    if flag:
        args = Fetch_argsname(func_name,api_doc_f.readline().rstrip())
    else:
        args = Fetch_argsname("class "+func_name,api_doc_f.readline().rstrip())
    tf_api = TFAPI(api_name)
    tf_api.parse_args(args)
    #print(tf_api.ArgInfo)
    #! Main part of Analysis
    #! Currently neglect anything besides For example code + Args comments
    for line in api_doc_f.readlines():
        if "For example" in line or "Example" in line or "Code example:" in line or "The following example" in line:
            tf_api.set_mode(ParseMode.EXAMPLE_S)
            continue
        elif line.strip() == "Args:" or line.strip() == "Call arguments:":
            tf_api.set_mode(ParseMode.ARGS)
            continue
        elif line.strip() == "Returns:":
            tf_api.set_mode(ParseMode.RETURN)
            continue
        elif line.strip() == "Raises:":
            tf_api.set_mode(ParseMode.RETURN)
            continue
        tf_api.parse_line(line)
    tf_api.generate_json()
    api_doc_f.close()
    
    return tf_api

if __name__ == "__main__": 
    #FreeFuzzresults = FreeFuzz_Data_Collection()
    #HelperDoc = TF_doc_Collection()

   
    for api_name in sorted(os.listdir(API_DOC_DIR)):
        #print(filename)
        
        try:
            Fetch_API_Info(api_name)
           
        except Exception as e:
            import shutil
            shutil.move( API_DOC_DIR + api_name,API_DOC_ERR_DIR+api_name)
            print(api_name)
            print(e)