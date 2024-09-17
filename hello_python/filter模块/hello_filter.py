import random

ran_num = [j for j in [random.random() for i in range(20)] if j > 0.5]
print(ran_num)
result = filter(lambda x: x > 0.5, ran_num)
print(list(result))

