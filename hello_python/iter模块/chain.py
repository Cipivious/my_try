from itertools import chain
import random

ch1 = [random.randint(1, 99) for _ in range(10)]
ch2 = [random.randint(1, 99) for _ in range(10)]
ch3 = [random.randint(1, 99) for _ in range(10)]
ch4 = [random.randint(1, 99) for _ in range(10)]

for x1, x2, x3, x4 in zip(ch1, ch2, ch3, ch4):
    print(x1, x2, x3, x4)
    print("*"*20)
    
for index, num in enumerate(chain(ch1, ch2, ch3, ch4)):
    if index > 10:
        break
    print(num)
