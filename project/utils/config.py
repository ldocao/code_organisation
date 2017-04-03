import os
import configparser

class Config:
    def __new__(self, file):
        config = configparser.ConfigParser()

        if not os.path.exists(file):
            raise IOError("File {} does not exist".format(file))
        
        config.read(file)
        return config
