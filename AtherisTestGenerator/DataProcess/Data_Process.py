from signal import raise_signal
from symbol import parameters
import pymongo
import textdistance
import re
import numpy as np
import configparser
import sys
from DataProcess.Types import ArgType
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

    if type_info["Label"] == "raw":
        if isint(type_info["value"]):
            record[argname].append(ArgType.INT)
        elif isfloat(type_info["value"]):
            record[argname].append(ArgType.FLOAT)
        else:
            record[argname].append(ArgType.STR)
    elif type_info["Label"] == "tensor":
        pass
    return record
def find_api_info(DB,api_name):
    if api_name not in DB.list_collection_names():
        raise Exception("{} is not found in database.".format(api_name))
    record = DB[api_name].find({}, {"_id": 0})
    for doc in record:
        for key,value in doc.items():
            if key=="output_signature":
                continue
            record = process_type(key,value,record)
if __name__ == "__main__":
    # database configuration
    host = "127.0.0.1"
    port = 27017
    api_name = "tf.abs"
    DB = pymongo.MongoClient(host, port)["freefuzz-tf"]
    API_Info = {}
    # find_api_list(DB)
    find_api_info(DB,api_name)