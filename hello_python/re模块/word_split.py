import re

base_word_list = open("./index.html", "r", encoding="utf-8").read()
word_list = re.split(r"\W+", base_word_list)
print(word_list)