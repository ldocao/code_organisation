# code_organisation
An example of general code organisation for data science projects. 

# Usage
1. Clone the repository and change the `project_name` directory name
2. Modify the `config/pythonpath.sh`, and source it to add `project_name` to your PYTHONPATH
3. You can now access your functions by importing:

```python
from project_name.domain.subdir.file_name import function_name
```

