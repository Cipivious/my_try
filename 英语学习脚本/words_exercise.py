import sqlite3
from datetime import datetime, timedelta
import os
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


# 创建数据库连接
def create_connection():
    conn = sqlite3.connect("word_database.db")  # 创建或连接一个数据库文件
    return conn


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
    
def clear_screen():
    # 判断当前操作系统
    if os.name == 'nt':
        # Windows 系统
        os.system('cls')
    elif os.name == 'posix':
        # Linux 或 MacOS 系统
        os.system('clear')

def get_exe_dir():
    if getattr(sys, 'frozen', False):
        # 如果被 PyInstaller 打包了，返回 .exe 的所在目录
        return os.path.dirname(sys.executable)
    else:
        # 未被打包时，返回脚本所在的目录
        return os.path.dirname(os.path.abspath(__file__))
def main():
    guess_word_list = get_words_by_date_and_proficiency()
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
            clear_screen()
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
            threading.Thread(target=update_word_review, args=(
                word[0], datetime.now().strftime("%Y-%m-%d %H:%M:%S"), correct_count
            )).start()
        print(r"你真棒，所有的单词都已经学习完成了，要继续努力啊！")


if __name__ == "__main__":
    if not os.path.exists("word_database.db"):
        print("请先运行另一个程序创建数据库并向其中添加单词！")
        sys.exit()
    main()