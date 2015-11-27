# NAME:
# PURPOSE: define path
# COMMENTS:


from default_packages import *
import quantpy as qp

REPO_PATH = "/absolute/path/to/my/repo"




ANALYTICS_PATH = REPO_PATH + "analytics"
CLEANING_PATH = REPO_PATH + "cleaning"
SETUP_PATH = REPO_PATH + "setup"
DATA_PATH = REPO_PATH + "data"
FIGURES_PATH = REPO_PATH + "figures"
OUT_PATH = REPO_PATH + "out"


##eventually add other directories to the list below
PATH_TO_ADD = [SETUP_PATH,
               CLEANING_PATH,
               ANALYTICS_PATH] #default dir to add to PYTHONPATH



[qp.sys.path.append(directory,recursive=True) for directory in PATH_TO_ADD]
