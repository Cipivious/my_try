import sqlite3
from datetime import datetime
import os
import re
import sys


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


def check_txt_file(path):
    if path[-4:] == ".txt":
        return True
    else:
        return False


def get_exe_dir():
    if getattr(sys, "frozen", False):
        # 如果被 PyInstaller 打包了，返回 .exe 的所在目录
        return os.path.dirname(sys.executable)
    else:
        # 未被打包时，返回脚本所在的目录
        return os.path.dirname(os.path.abspath(__file__))


def main():
    dir_path = get_exe_dir()
    print("当前文件夹的路径是：", dir_path)
    full_file_list = os.listdir()
    txt_file_list = list(filter(check_txt_file, full_file_list))
    print("下面是当前文件夹的txt文件")
    for index, txt_file in enumerate(txt_file_list):
        print(str(index) + ". " + txt_file)
    file_path = input(
        "请输入你想要添加的文件的名称或者其对应的序号（例如：day1.txt 或者 0) "
    )
    while True:
        if file_path in txt_file_list:
            break
        if int(file_path) >= 0 and int(file_path) < len(txt_file_list):
            file_path = txt_file_list[int(file_path)]
            break
        file_path = input(
            "输入有误，请重新输入你想要添加的文件的名称或者其对应的序号（例如：day1.txt 或者 0) "
        )
    full_file_path = os.path.join(dir_path, file_path)
    word_list = split_txt(full_file_path)
    for word, translation in word_list:
        insert_word(word=word, translation=translation)


if __name__ == "__main__":
    if not os.path.exists("word_database.db"):
        create_table()
    while True:
        main()
        answer = input("是否还想要添加其它的文件？y/n？ ")
        if answer == "n":
            break
        print("好的，下面我们来添加其它文件吧")
