import pandas as pd

dog = {"name": "xiaohuang", "age": "1", "gender": "famale"}
data = pd.Series(dog)
print(data)
print(data.index)
print(data.values)
print(dog["age"])
