import pandas as pd

# 假设这是你的 DataFrame
df = pd.DataFrame({"A": [1, 2, 3, 4, 5], "B": [10, 20, 30, 40, 50]})


# 定义处理函数
def process_value(x):
    return x * x  # 示例：将每个值乘以2


# 使用 apply 方法对 DataFrame 的某一列进行操作
df["A"] = df["A"].apply(process_value)

print(df)
