import pymongo
import numpy as np
#mport configparser

import sys
import re
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

def isdict(x):
    import ast
    if x.startswith("{"):
        return ast.literal_eval(x)["class_name"]
    else:
        return x
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
    #print(argname,type_info)
    if isinstance(type_info,list):
        try:
            index = current_type.index(str(TFArgument(ArgType.LIST)))
            record[argname][index].add_list_value(len(type_info))
        except ValueError:
            new_LIST = TFArgument(ArgType.LIST)
            new_LIST.add_list_value(len(type_info))
            record[argname].append(new_LIST)
        return record
    if type_info["Label"] == "raw":
        if isint(type_info["value"]):
            if str(TFArgument(ArgType.INT)) not in current_type:
                record[argname].append(TFArgument(ArgType.INT))
        elif isfloat(type_info["value"]):
            if str(TFArgument(ArgType.FLOAT)) not in current_type:
                record[argname].append(TFArgument(ArgType.FLOAT))
        elif isinstance(type_info["value"],list):
            try:
                index = current_type.index(str(TFArgument(ArgType.LIST)))
                record[argname][index].add_list_value(len(type_info["value"]))
            except ValueError:
                new_LIST = TFArgument(ArgType.LIST)
                new_LIST.add_list_value(len(type_info["value"]))
                record[argname].append(new_LIST)
        elif type_info["value"] == "true" or type_info["value"] == "false":
            if str(TFArgument(ArgType.BOOL)) not in current_type:
                record[argname].append(TFArgument(ArgType.BOOL))
        else:
            type_info["value"] = isdict(type_info["value"])
            str_val = type_info["value"]
            try:
                index = current_type.index(str(TFArgument(ArgType.STR)))
                record[argname][index].add_str_value(str_val)
            except ValueError:
                new_STR = TFArgument(ArgType.STR)
                new_STR.add_str_value(str_val)
                record[argname].append(new_STR)
    elif type_info["Label"] == "tensor":
        if str(TFArgument(type=ArgType.TF_TENSOR,dtype=type_info["dtype"])) not in current_type:
            record[argname].append(TFArgument(type=ArgType.TF_TENSOR,dtype=type_info["dtype"]))
    elif type_info["Label"] == "tf_object":
        #TODO: Add support for tf_object
        if type_info["class_name"] == "tensorflow.python.keras.engine.keras_tensor.KerasTensor":
            if str(TFArgument(type=ArgType.TF_TENSOR,dtype=type_info["dtype"])) not in current_type:
                record[argname].append(TFArgument(type=ArgType.TF_TENSOR,dtype=type_info["dtype"]))
        elif type_info["class_name"] == "tensorflow.python.training.tracking.data_structures.ListWrapper":
            length = type_info["to_str"].count(",") + 1
            try:
                index = current_type.index(str(TFArgument(ArgType.LIST)))
                record[argname][index].add_list_value(length)
            except ValueError:
                new_LIST = TFArgument(ArgType.LIST)
                new_LIST.add_list_value(length)
                record[argname].append(new_LIST)
        elif type_info["class_name"] == "tensorflow.python.framework.dtypes.DType":
            str_dtypes = type_info["to_str"]
            #print(str_dtypes)
            str_val = re.search("<dtype: '(\w+)'>",str_dtypes).group(1)
            str_val = "tf." + str_val
            try:
                index = current_type.index(str(TFArgument(ArgType.TF_DTYPE)))
                record[argname][index].add_str_value(str_val)
            except ValueError:
                new_STR = TFArgument(ArgType.TF_DTYPE)
                new_STR.add_str_value(str_val)
                record[argname].append(new_STR)
        else:
            print(argname,type_info)
    elif type_info["Label"] == "other":
        if type_info["type"] == "<class 'NoneType'>":
            if str(TFArgument(type=ArgType.NULL)) not in current_type:
                record[argname].append(TFArgument(type=ArgType.NULL))
    return record

def find_api_info(DB,api_name):
    if api_name not in DB.list_collection_names():
        raise Exception("{} is not found in database.".format(api_name))
    records = DB[api_name].find({}, {"_id": 0})
    results = {}
    for doc in records:
        #print("=============================")
        for key,value in doc.items():
            value_r = value
            if key=="output_signature":
                continue
            if key=="input_signature":
                continue
                # print(value)
                #value_r = value[0]

            #print(key,value_r)
            results = process_type(key,value_r,results)
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