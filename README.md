# code_organisation
An example of general code organisation for data science projects

# usage
- clone the repo
- rename your project and set the path in setup/setup.py
- change the default packages you would like to be always loaded in every script
- delete the __init__.py files that are here only for git.
- in every subfolder you will create later, copy setup_dir.py (in analytics/setup_dir.py)
- change the relative path to setup.py
- add at the top of each script : from setup_dir import *
