import pandas as pd
import numpy as np
import re
import os


class DataReader(object):
    def __init__(self):
        pass

    @classmethod
    def read(cls, file_path):
        file_type = re.split(re.compile('\.'), file_path)[-1]
        if file_type == 'csv':
            return cls.readCsv(file_path)
        elif file_type == 'xls' or file_type == 'xlsx':
            return cls.readXls(file_path)
        else:
            return None

    @classmethod
    def readCsv(cls, file_path):
        df = pd.read_csv(file_path)
        data = np.array(df)
        return data

    @classmethod
    def readXls(cls, file_path):
        df = pd.read_excel(file_path)
        data = np.array(df)
        return data
