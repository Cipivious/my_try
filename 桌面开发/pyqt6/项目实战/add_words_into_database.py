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
