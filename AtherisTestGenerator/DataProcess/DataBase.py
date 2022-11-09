import pymongo
import pymongo
from numpy.random import choice
"""
This file is the interfere with database
"""

class Database:
    def __init__(self) -> None:
        self.input = False

    def database_config(self, host, port, database_name):
        self.DB = pymongo.MongoClient(host=host, port=port)[database_name]
