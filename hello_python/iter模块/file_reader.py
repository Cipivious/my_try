from itertools import islice
from collections.abc import Iterator
iter_lines = islice(open("./index.html", "r", encoding="utf-8"), 20, 100)

print(isinstance(iter_lines, Iterator))

for line in iter_lines:
    print(line)
    
    
    