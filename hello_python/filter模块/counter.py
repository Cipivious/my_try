from collections import Counter
import re

base_word_list = open("./text.txt", "r", encoding="utf-8").read()
word_list = re.split(r"\W+", base_word_list)
countered_word_list = Counter(word_list)
print(countered_word_list.most_common(10))
