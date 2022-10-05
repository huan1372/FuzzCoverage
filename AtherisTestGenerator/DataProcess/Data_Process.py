import pymongo
import textdistance
import re
import numpy as np
import configparser
import sys
from os.path import join
if __name__ == "__main__":
    # database configuration
    host = "127.0.0.1"
    port = 27017
    DB = pymongo.MongoClient(host, port)["freefuzz-tf"]