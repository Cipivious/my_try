import re


def match_string(input_string):
    pattern = r"(@\S+)\s?(.*)"
    match = re.match(pattern, input_string)
    if match:
        return match.groups()  # 返回匹配到的内容
    else:
        return ("", "")  # 如果没有匹配到，返回空元组


# 示例
input_string = "@username 这是后面的内容"
result = match_string(input_string)
print(result)  # 输出: ('@username', '这是后面的内容')

input_string = "hello"
result = match_string(input_string)
print(result)  # 输出: ('', '')
