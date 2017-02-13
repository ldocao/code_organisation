# Template for python project
## Purpose
This repository is a template for a python data science project. 

## Main structure
The root should contain at least the following elements:

- `project/`: a folder named after the project containing the code. Inside, you should follow the code organisation described in [coding.md](https://gitlab.com/quantmetry/guidelines/blob/master/coding.md#folder-structure)
- `README.md`: a markdown file describing very shortly the objective, methods, main results, and how to use the repo
- `doc/`: folder containing all additional and detailed documentation of your repository.
- `.gitignore`: list of git ignored files

Optionnally, you may find a `sonar-project.properties` which is a configuration file for the [sonarqube software](https://www.sonarqube.org/), a code quality evaluator. 


## Code organisation
Inside `project/`, the code should be organised according to Domain Driven Design:

-	`infrastructure/`: data collection and technical cleaning, connector to the database-	`domain/`: domain-related cleaning, feature engineering, machine learning algorithm, domain specific knowledge-	`application/`: application orchestrator or API, you may define here the order in which the cleaning processes must be run
-	`interface/`: user interface (eg: javascript front-end)In addition, you will find two folders:
-	`tests/`: unit (functions test), integration (pipeline test), acceptance (expected domain values test), scalability (workload test)
- `config/`: folder containing all configuration files if you need to deploy your code to another machine




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

warning: `Config` returns a `ConfigParser` object. Please see the [configparser](https://docs.python.org/3/library/configparser.html) module documentation for drawbacks (eg: an integer passed into the configuration file will be recognized as a str object)

- Import a python module using : 

```python
import project.domain.sub_directory.my_file
```

En example can be found in `project/domain/machine_learning.py`


## Side effects
Support for python3.x only


