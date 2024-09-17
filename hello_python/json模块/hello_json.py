import json

dog = {"name": "xiaohuang", "age": "1", "gender": "famale"}

dog_info = json.dumps(dog)
print(dog_info)

dog_info = dog_info[:-1] + ', "hobby": "eat"}'
print(dog_info)

dog = json.loads(dog_info)
print(dog)

with open("./dog.json", "w", encoding="utf-8") as f:
    json.dump(dog, f)

with open("./dog.json", "r", encoding="utf-8") as f:
    dog = json.load(f)

print(dog)
