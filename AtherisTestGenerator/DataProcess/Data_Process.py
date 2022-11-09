from ast import arg
from logging import raiseExceptions
from unittest import case
import pymongo
import numpy as np

#mport configparser

import sys
import re
sys.path.insert(1, '/home/usr/FreeFuzz/FuzzCoverage/AtherisTestGenerator/')
from DataProcess.DataBase import Database as DB
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
    if x.startswith("{"):
        #print(x)
        return re.search("^{\"class_name\": \"(\w+)\"",x).group(1)
    else:
        return x
def isdictionary(x):
    import ast
    if x.startswith("{") and "class_name" not in x:
        #print(x)
        return ast.literal_eval(x)
    else:
        return False
def find_api_list(DB):
    f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisTestgenerator/api_list.txt","w")
    for name in sorted(DB.list_collection_names()):
        if name == "similarity" or name == "signature":
            continue
        f.write(name + "\n")
    f.close()
def check_tf(name):
    check_list = ["tensorflow.python.ops.init_ops","tensorflow.python.keras.mixed_precision.policy.","tensorflow.python.ops.ragged.ragged_tensor"]
    f = open("tf_object_miss_API.txt","a")
    for check in check_list:
        if name.startswith(check):
            f.write(name + "\n")
            f.close()
            return True
    f.close()
    return False

def add_STR(record,current_type,argname,str_val):
    try:
        index = current_type.index(str(TFArgument(ArgType.STR)))
        record[argname][index].add_str_value(str_val)
    except ValueError:
        new_STR = TFArgument(ArgType.STR)
        new_STR.add_str_value(str_val)
        record[argname].append(new_STR)
    return record

def add_int_value_to_record(type_info:int,current_type,argname,record):
    value = int(float(type_info))
    if str(TFArgument(ArgType.INT)) not in current_type:
        new_INT_TYPE = TFArgument(ArgType.INT)
        new_INT_TYPE.add_list_value(value,possible_list=None)
        record[argname].append(new_INT_TYPE)
    else:
        index = current_type.index(str(TFArgument(ArgType.INT)))
        record[argname][index].add_list_value(value,possible_list=None)
    return record

def add_float_value_to_record(type_info:float,current_type,argname,record):
    if str(TFArgument(ArgType.FLOAT)) not in current_type:
        new_FLOAT_TYPE = TFArgument(ArgType.FLOAT)
        new_FLOAT_TYPE.add_list_value(float(type_info),possible_list=None)
        record[argname].append(new_FLOAT_TYPE)
    else:
        index = current_type.index(str(TFArgument(ArgType.FLOAT)))
        record[argname][index].add_list_value(float(type_info),possible_list=None)
    return record

def add_int_list_to_record(type_info:list,current_type,argname,record):
    try:
        index = current_type.index(str(TFArgument(ArgType.LIST)))
        record[argname][index].add_list_value(len(type_info),type_info)
    except ValueError:
        new_LIST = TFArgument(ArgType.LIST)
        new_LIST.add_list_value(len(type_info),type_info)
        record[argname].append(new_LIST)
    return record

def process_type(argname,type_info,record):
    # Raw type
    if argname.startswith("parameter") and argname != "parameter:0":
        return record
    if argname not in record.keys():
        record[argname] = []
    current_type = [str(i) for i in record[argname]]
    #print(argname,type_info)
    if isinstance(type_info,list):
        record = add_int_list_to_record(type_info=type_info,current_type=current_type,argname=argname,record=record)
        return record
    if isint(type_info):
        record = add_int_value_to_record(type_info=type_info,current_type=current_type,argname=argname,record=record)
        return record
    if type_info["Label"] == "raw":
        if isint(type_info["value"]):
            record = add_int_value_to_record(type_info=type_info["value"],current_type=current_type,argname=argname,record=record)
        elif isfloat(type_info["value"]):
            record = add_float_value_to_record(type_info=type_info["value"],current_type=current_type,argname=argname,record=record)
        elif isinstance(type_info["value"],list):
            record = add_int_list_to_record(type_info=type_info["value"],current_type=current_type,argname=argname,record=record)
        elif type_info["value"] == "true" or type_info["value"] == "false":
            if str(TFArgument(ArgType.BOOL)) not in current_type:
                record[argname].append(TFArgument(ArgType.BOOL))
        elif isdictionary(type_info["value"]):
            #print(type_info["value"])
            if str(TFArgument(ArgType.DICT)) not in current_type:
                record[argname].append(TFArgument(ArgType.DICT,tf_class=type_info["value"]))
        else:
            type_info["value"] = isdict(type_info["value"])
            str_val = type_info["value"]
            add_STR(record,current_type,argname,str_val)
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
            lista = re.search("ListWrapper\(\[([,a-zA-Z0-9_\s-]+)\]\)",type_info["to_str"]).group(1)
            if length == 1:
                lista = [int(float(lista))]
            else:
                lista = [int(float(i)) for i in lista.split(",")]
            record = add_int_list_to_record(type_info=lista,current_type=current_type,argname=argname,record=record)
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
        elif type_info["class_name"].startswith("tensorflow.python.keras.initializers.initializer"):
            class_val = "tf.keras.initializers."
            #print(type_info["class_name"])
            str_val = re.search("tensorflow.python.keras.initializers.initializers_v\w.(\w+)",type_info["class_name"]).group(1)
            #print(str_val)
            try:
                index = current_type.index(str(TFArgument(ArgType.TF_OBJECT)))
                if class_val !=  record[argname][index].tf_class:
                    raise Exception("Not same class")
                record[argname][index].add_str_value(str_val)
            except ValueError:
                new_STR = TFArgument(ArgType.TF_OBJECT,tf_class=class_val)
                new_STR.add_str_value(str_val)
                record[argname].append(new_STR)
        elif type_info["class_name"].startswith("tensorflow.python.keras.regularizers"):
            str_val = re.search("tensorflow.python.keras.regularizers.(\w+)",type_info["class_name"]).group(1)
            if str_val == "L1":
                str_val = "l1"
            elif str_val == "L2":
                str_val = "l2"
            else:
                raise Exception("Not implement option for tensorflow.python.keras.regularizers")
            add_STR(record,current_type,argname,str_val)
        elif check_tf(type_info["class_name"]):
            #str_val = re.search("tensorflow.python.ops.init_ops_v2.(\w+)",type_info["class_name"]).group(1)
            print(type_info["class_name"])
            # [Constant]
        else:
            print(argname,type_info)
            raise Exception("Not implemented!")
    elif type_info["Label"] == "other":
        if type_info["type"] == "<class 'NoneType'>":
            if str(TFArgument(type=ArgType.NULL)) not in current_type:
                record[argname].append(TFArgument(type=ArgType.NULL))
        else:
            if str(TFArgument(type=ArgType.NULL)) not in current_type:
                record[argname].append(TFArgument(type=ArgType.NULL))
    return record

def find_api_info(DB,api_name):
    if api_name not in DB.DB.list_collection_names():
        raise Exception("{} is not found in database.".format(api_name))
    records = DB.DB[api_name].find({}, {"_id": 0})
    results = {}
    for doc in records:
        #print("=============================")
        for key,value in doc.items():
            value_r = value
            print(api_name,key,value_r)
            if key=="output_signature":
                continue
            if key=="input_signature":
                DB.input = True
                try:
                    value_r = value[0]
                except KeyError:
                    continue
            results = process_type(key,value_r,results)
    return results

if __name__ == "__main__":
    # database configuration
    host = "127.0.0.1"
    port = 27017
    api_name = "tf.abs"
    database_name = "freefuzz-tf"
    #DB = pymongo.MongoClient(host, port)["freefuzz-tf"]
    DB = DB()
    DB.database_config( host, port, database_name)
    API_Info = {}
    # find_api_list(DB)
    record = find_api_info(DB,api_name)
    for i in record["parameter:0"]:
        print(i)