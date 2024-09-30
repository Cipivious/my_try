import sqlite3
from datetime import datetime, timedelta
import os
import re
import sys
import random
import os
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
import threading


def get_word_exmple(word, num=5):
    api_root = "https://linguee-api.fly.dev/api/v2"
    resp = requests.get(
        f"{api_root}/external_sources",
        params={"query": word[1], "src": "en", "dst": "zh"},
    )
    example_list = []
    for index, source in enumerate(resp.json()):
        # print(source)
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


# 创建数据库连接
def create_connection():
    conn = sqlite3.connect("word_database.db")  # 创建或连接一个数据库文件
    return conn


# 创建单词表
def create_table():
    conn = create_connection()
    cursor = conn.cursor()

    # 创建单词表
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS word_database (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        word TEXT NOT NULL,
        translation TEXT NOT NULL,
        added_time TEXT,
        review_time TEXT,
        correct_count INTEGER DEFAULT 0
    )
    """
    )

    conn.commit()
    conn.close()


# 插入单词记录
def insert_word(word, translation):
    conn = create_connection()
    cursor = conn.cursor()

    added_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    review_time = None  # 初始的复习时间可以为空

    cursor.execute(
        """
    INSERT INTO word_database (word, translation, added_time, review_time, correct_count)
    VALUES (?, ?, ?, ?, ?)
    """,
        (word, translation, added_time, review_time, 0),
    )

    conn.commit()
    conn.close()


# 获取所有单词记录
def fetch_all_words():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM word_database")
    rows = cursor.fetchall()

    conn.close()
    return rows


def get_words_by_date_and_proficiency(proficiency_threshold=6):
    # Connect to the database
    conn = create_connection()
    cursor = conn.cursor()

    today = datetime.now().date()  # 获取当前日期
    selected_words = []

    # 定义日期范围
    date_ranges = {
        "today": today,
        "yesterday": today - timedelta(days=1),
        "week_ago": today - timedelta(weeks=1),
        "month_ago": today - timedelta(days=30),
    }

    # 循环遍历每个日期范围并查询记录
    for date in date_ranges.values():
        formatted_date = date.strftime("%Y-%m-%d")  # 将日期格式化为字符串
        cursor.execute(
            f"""
            SELECT * FROM word_database
            WHERE DATE(added_time) = ? AND correct_count < ?
        """,
            (formatted_date, proficiency_threshold),
        )

        words = cursor.fetchall()

        if words:
            if len(words) >= 10:
                selected_word = random.sample(words, k=10)
                selected_words.extend(selected_word)
            else:
                selected_words.extend(words)
    cursor.execute(
        f"""
        SELECT * FROM word_database
        WHERE correct_count < ?
    """,
        (3,),
    )

    words = cursor.fetchall()

    if words:
        if len(words) >= 10:
            selected_word = random.sample(words, k=10)
            selected_words.extend(selected_word)
        else:
            selected_words.extend(words)
    # Close the database connection
    conn.close()

    return selected_words


# 更新复习时间和答对次数
def update_word_review(word_id, new_review_time, correct_count):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
    UPDATE word_database
    SET review_time = ?, correct_count = ?
    WHERE id = ?
    """,
        (new_review_time, correct_count, word_id),
    )

    conn.commit()
    conn.close()


def main():
    if len(sys.argv) == 2:
        dir_path = os.path.dirname(os.path.abspath(__file__))
        file_path = sys.argv[1]
        full_file_path = os.path.join(dir_path, file_path)
        word_list = split_txt(full_file_path)
        for word, translation in word_list:
            insert_word(word=word, translation=translation)
    elif len(sys.argv) != 1:
        print("Usage: python translate_exercise.py day1.txt")
        sys.exit()

    # 创建线程池并提交任务
    guess_word_list = get_words_by_date_and_proficiency()
    # print(rows)
    # print(len(rows))
    # sys.exit()

    with ThreadPoolExecutor(max_workers=2) as executor:
        futures = [
            executor.submit(get_word_exmple, word, 3) for word in guess_word_list
        ]
        # 逐个获取已经完成任务的返回值
        word_numbers = len(guess_word_list)
        print(f"本次一共有{word_numbers}个单词，开始你的闯关之旅吧！")
        print("单词概览：")
        for word in guess_word_list:
            print(*word)
        input("准备好了吗？")
        for future in as_completed(futures):
            os.system("clear")
            word, example_list = future.result()
            print(word[1])
            answer = input("do you understand it? y/n/e\n")
            if answer == "e":
                break
            correct_count = word[5]
            if answer in ["n", "no", "No", "N", "NO"]:
                for example in example_list:
                    print(example)
                    time.sleep(4)
                print("\n\n", word[2])
                input("你学会了吗？")
            else:
                correct_count = correct_count + 1
                if example_list:
                    print(example_list[0])
                    time.sleep(3)
            threading.Thread(
                target=update_word_review,
                args=(
                    word[0],
                    datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    correct_count,
                ),
            ).start()
        print(r"你真棒，所有的单词都已经学习完成了，要继续努力啊！")


if __name__ == "__main__":

    main()
