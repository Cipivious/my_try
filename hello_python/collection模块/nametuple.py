import collections

Student = collections.namedtuple("Student", ["name", "age", "gender", "score"])

s1 = Student("yang", "22", "famale", "98")
print(s1.name)
