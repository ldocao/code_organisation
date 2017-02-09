import os
import configparser

class Config:
    def __new__(self, file):
        current_directory = os.path.dirname(__file__)
        full_path = os.path.join(current_directory, file)
        config = configparser.ConfigParser()

        if not os.path.exists(full_path):
            raise IOError("File {} does not exist".format(full_path))
        
        config.read(full_path)
        return config
