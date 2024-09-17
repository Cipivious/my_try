# 示例：使用 map 对列表的每个元素进行操作
nums = [1, 2, 3, 4, 5]


# 定义一个处理函数
def double(x):
    return x * 2


# 使用 map 将函数应用到列表的每个元素
result = map(double, nums)
# print(next(result))
for i in result:
    print(i)
# 将结果转换为列表
result = list(result)

print(result)  # 输出: [2, 4, 6, 8, 10]
