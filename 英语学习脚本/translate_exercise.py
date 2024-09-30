import re
import sys
import random
import os
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

def get_word_exmple(word, num=5):
    api_root = "https://linguee-api.fly.dev/api/v2"
    resp = requests.get(
        f"{api_root}/external_sources",
        params={"query": word[0], "src": "en", "dst": "zh"},
    )
    example_list = []
    for index, source in enumerate(resp.json()):
        if index >= num or source == "message":
            break
        example_list.append(
            f"{source['src']} \n\n {source['dst']} \n\n ************************************************************ \n"
        )
    return word, example_list


def split_string(string):
    result = re.search(r"[\u4e00-\u9fa5]", string)
    index = result.regs[0][0]
    word_part = string[0:index].strip()
    translate_part = string[index:].strip()
    return word_part, translate_part


def split_txt(file_path):
    word_list = []
    with open(file_path, "r", encoding="utf-8") as f:
        line = f.readline()
        while line:
            word_list.append(split_string(line))
            line = f.readline()
    return word_list


if __name__ == "__main__":
    if len(sys.argv) == 2:
        dir_path = os.path.dirname(os.path.abspath(__file__))
        file_path = sys.argv[1]
        full_file_path = os.path.join(dir_path, file_path)
        word_list = split_txt(full_file_path)
        guess_word_list = random.sample(word_list, k=10)
        # 创建线程池并提交任务
        with ThreadPoolExecutor(max_workers=5) as executor:
            futures = [
                executor.submit(get_word_exmple, word, 3) for word in guess_word_list
            ]
            # 逐个获取已经完成任务的返回值
            for future in as_completed(futures):
                word, example_list = future.result()
                print(word[0])
                answer = input("do you understand it? y/n\n")
                if answer in ["n", "no", "No", "N", "NO"]:
                    for example in example_list:
                        print(example)
                    print("\n\n", word[1])
                else:
                    print(example_list[0])

    else:
        print("Usage: python translate_exercise.py day1.txt")
