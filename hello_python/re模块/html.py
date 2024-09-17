import re

# content = r"<title>this is a title</title>"


# res = re.match(r"<(?P<tag>\w+)>([\w\W]+)</(?P=tag)>", content)

# # for i in range(3):
# #     print(res.group(i))

# for item in res.groups():
#     print(item)

# res = re.compile(
#     r"<(?P<tag>\w+)([^>]*)>(.*?)</(?P=tag)>|<(?P<tag_self_closing>\w+)([^>]*)/?>"
# )
res = re.compile(r"<(?P<tag>\w+)([^>]*)>(.*?)</?(?P=tag)>")

with open("./index.html", "r", encoding="utf-8") as f:
    content = f.read()


# results = res.split(content)

# for result in results:
#     print(result)
# # print(result)

# results = res.sub("我是一个大傻瓜", content)

# print(results)


# # 要替换的匹配项的序号（从1开始）
# target_match = 1

# # 计数器
# match_count = 0


# # 回调函数，用于替换指定的匹配项
# def replace_match(match):
#     global match_count
#     match_count += 1
#     if match_count == target_match:
#         return "我是一个大傻瓜"  # 只替换第 target_match 个匹配项
#     else:
#         return match.group(0)  # 返回原始匹配项，保持不变


# # 使用回调函数执行替换
# replaced_content = res.sub(replace_match, content)

# print(replaced_content)


for result in res.finditer(content):
    print(result.group(1))
