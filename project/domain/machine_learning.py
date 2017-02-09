from project.config import Config

config = Config("template.ini")
print(config["database"]["password"])

