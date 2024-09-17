import os
import pandas as pd


def list_files_in_directory(directory):
    # 列出文件夹下的所有文件
    files = {
        f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))
    }
    return files


# 示例使用

directory_path = r"D:\bilibili"
files_set = list_files_in_directory(directory_path)

base_file_set = set(pd.read_csv("./name.csv")["file_name"])
difference = base_file_set - files_set
print(difference)

df = pd.DataFrame(difference)
df.columns = ["file_name"]
df.to_csv("./new_name.csv", index=False)
