import yaml

file = open("./config.yaml", "r", encoding="utf-8")
data = yaml.safe_load(file)
file.close()
print(data)