import random
import faker
import functools

fake = faker.Faker(locale="zh_CN")

name_list = [fake.name() for _ in range(5)]
print(name_list)
score_list = [{name: random.randint(1, 5) for name in random.choices(name_list, k=5)} for _ in range(5)]
print(list(score_list[1].keys()))
# 使用reduce和set的交集操作

common_keys = functools.reduce(lambda prev, item: prev & item, (set(d.keys()) for d in score_list))

print(common_keys)
