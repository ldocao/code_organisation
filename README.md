# code_organisation
An example of general code organisation for data science projects. 

# Usage
1. Clone the repository and change the `project_name` directory name
2. Modify the `config/pythonpath.sh`, and source it to add `project_name` to your PYTHONPATH
3. You can now access your functions by importing:

```python
from project_name.domain.subdir.file_name import function_name
```

# Versioning policy
The basic Version control follows the *code*, and not the data. Thus, `.gitignore` exclude all temporary emacs/python files, and data (eg: `.csv`). In order to version data files (even small ones), you should use git lfs.
1. Follow the [instructions to install git-lfs](https://git-lfs.github.com/)
2. `bash$ git lfs track "*.csv"` (kind of opposite of `.gitignore`)
3. Use regular git commands (eg: `bash$ git commit file.csv`) to version your data.

