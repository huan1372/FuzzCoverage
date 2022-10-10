import pymongo
import numpy as np
#mport configparser

import sys
sys.path.insert(1, '/home/usr/FreeFuzz/FuzzCoverage/AtherisTestGenerator/')

from Generator.Types import ArgType
from Generator.ArgTF import TFArgument

from os.path import join
def isfloat(x):
    try:
        a = float(x)
    except (TypeError, ValueError):
        return False
    else:
        return True

def isint(x):
    try:
        a = float(x)
        b = int(a)
    except (TypeError, ValueError):
        return False
    else:
        return a == b

def find_api_list(DB):
    f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisTestgenerator/api_list.txt","w")
    for name in sorted(DB.list_collection_names()):
        if name == "similarity" or name == "signature":
            continue
        f.write(name + "\n")
    f.close()

def process_type(argname,type_info,record):
    # Raw type
    if argname not in record.keys():
        record[argname] = []
    current_type = [str(i) for i in record[argname]]
    if type_info["Label"] == "raw":
        if isint(type_info["value"]):
            if str(TFArgument(ArgType.INT)) not in current_type:
                record[argname].append(TFArgument(ArgType.INT))
        elif isfloat(type_info["value"]):
            if str(TFArgument(ArgType.FLOAT)) not in current_type:
                record[argname].append(TFArgument(ArgType.FLOAT))
        else:
            if str(TFArgument(ArgType.STR)) not in current_type:
                record[argname].append(TFArgument(ArgType.STR))
    elif type_info["Label"] == "tensor":
        if str(TFArgument(type=ArgType.TF_TENSOR,dtype=type_info["dtype"])) not in current_type:
            record[argname].append(TFArgument(type=ArgType.TF_TENSOR,dtype=type_info["dtype"]))
    elif type_info["Label"] == "tf_object":
        pass
    return record

def find_api_info(DB,api_name):
    if api_name not in DB.list_collection_names():
        raise Exception("{} is not found in database.".format(api_name))
    records = DB[api_name].find({}, {"_id": 0})
    results = {}
    for doc in records:
        for key,value in doc.items():
            if key=="output_signature":
                continue
            #print("=============================")
            #print(key,value)
            results = process_type(key,value,results)
    return results

if __name__ == "__main__":
    # database configuration
    host = "127.0.0.1"
    port = 27017
    api_name = "tf.abs"
    DB = pymongo.MongoClient(host, port)["freefuzz-tf"]
    API_Info = {}
    # find_api_list(DB)
    record = find_api_info(DB,api_name)
    for i in record["parameter:0"]:
        print(i)