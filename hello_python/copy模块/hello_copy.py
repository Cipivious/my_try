import copy



dog = {
    "name": "yang",
    "age": 18,
    "gender": "female",
    "hobby": [
        "pingpang",
        "basketball"
    ]
}

normal_dog = copy.copy(dog)
deep_dog = copy.deepcopy(dog)

dog["hobby"][1] = "football"

print(normal_dog)
print(deep_dog)


