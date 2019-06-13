import pandas as pd
import re


class DataSaver(object):
    def __init__(self):
        pass

    @classmethod
    def save(cls, file_path, data):
        file_type = re.split(re.compile(r'\.'), file_path)[-1]
        if file_type == 'csv':
            return cls.saveCsv(file_path, data)
        elif file_type == 'xls' or file_type == 'xlsx':
            return cls.saveXls(file_path, data)
        else:
            return None

    @classmethod
    def saveCsv(cls, file_path, data):
        df = pd.DataFrame(data)
        df.to_csv(file_path)
        return True

    @classmethod
    def saveXls(cls, file_path, data):
        df = pd.DataFrame(data)
        df.to_excel(file_path)
        return True
