# Template for python project
## Purpose

## Philosophy
Based on DDD



## How to use ?
### Configuration
- Add the repo directory to your `PYTHONPATH` environment variable (eg: in your `.bashrc`)
- Change the name of `project/` directory, if necessary
- Configuration parameters (eg: location of data, API port, database configuration, etc.) should be set into a .ini file inside `project/config/`. You may copy `project/config/template.ini` into a `my_config.ini` which should **not** be committed.
- In order to access the configuration parameters, you can use :

```python
from project.config import Config
config = Config("template.ini")
print(config["database"]["password"]) #return 'password_test'
```

warning: Config returns a ConfigParser object. Please see the configparser module documentation for drawbacks (eg: an integer passed into the configuration file will be recognized as a str object)

- Import a python module using : 

```python
import project.domain.sub_directory.my_file
```

En example can be found in `project/domain/machine_learning.py`

### Tests
1. unit
2. integration
3. acceptance


### Documentation

