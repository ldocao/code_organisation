from project.infrastructure.technical_cleaning import IrisCleaner


class Iris(object):
    def __init__(self, config_file):
        self.config = config_file

    def infere_missing_values(self):
        """Replace missing values by 0"""
        iris = IrisCleaner(self.config).read_csv()
        iris.fillna(0., inplace=True)
        return iris



