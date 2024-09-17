my_dict = {'b': 2, 'a': 1, 'c': 3}

# 按值排序
sorted_by_values = dict(sorted(my_dict.items(), key=lambda item: item[1]))

print(sorted_by_values)  # 输出 {'a': 1, 'b': 2, 'c': 3}
