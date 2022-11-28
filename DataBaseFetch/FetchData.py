import tensorflow as tf
from enum import IntEnum
import re
import sys
import io

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

API_DOC_DIR = "/Users/sh69/Documents/FreeFuzz/FuzzCoverage/DataBaseFetch/API_Doc/"

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

def process_type(argname,type_info,record,api_name):
    # Raw type
    if argname not in record.keys():
        record[argname] = set()

    #? There is Data with list/int not string when parsing
    if isinstance(type_info,list):
        record[argname].add((ArgType.LIST,"raw"))
        return record
    if isinstance(type_info,int):
        record[argname].add((ArgType.INT,"raw"))
        return record
    if isinstance(type_info,float):
        record[argname].add((ArgType.FLOAT,"raw"))
        return record
    if isinstance(type_info,str):
        if type_info == "none":
            record[argname].add((ArgType.NULL,"raw"))
        else:
            record[argname].add((ArgType.STR,"raw"))
        return record
    if isinstance(type_info,dict):
        if "dtype" in type_info.keys() and "type" in type_info.keys() and type_info["type"] == "tensor":
            record[argname].add((ArgType.TF_TENSOR,type_info["dtype"]))
        return record
    if type_info is None:
        record[argname].add((ArgType.NULL,"raw"))
        return record
    print(argname,type(type_info),api_name)  
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
            result = dict()
            for doc in records:
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
                    result = process_type(key,value_r,result,api_name)
            results[api_name] = result
    return results

if __name__ == "__main__": 
    #FreeFuzzresults = FreeFuzz_Data_Collection()
    HelperDoc = TF_doc_Collection()
    print("a")