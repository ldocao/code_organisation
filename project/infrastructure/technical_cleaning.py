import pandas as pd

from project.utils.config import Config



class IrisCleaner(object):
    FILENAME = "iris.csv"
    
    def __init__(self, config_file):
        self.config = config_file

    def read_csv(self):
        config = Config(self.config)
        directory = config["data"]["location"]
        path_to_file = directory + self.__class__.FILENAME
        iris = pd.read_csv(path_to_file)
        return self.upper_case_header(iris)


    def upper_case_header(self, df):
        df.columns = [header.upper() for header in df.columns]        
        return df
