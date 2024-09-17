from configparser import ConfigParser

config = ConfigParser()
config.read("./config.ini")
print(config["production"]["port"])
print(dict(config))
