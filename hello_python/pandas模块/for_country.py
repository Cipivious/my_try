import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

df = pd.read_csv("./countries_combinations.csv")
# print(df["country"])
country_list = list(set([i for j in df["country"].str.split(",") for i in j]))
print(country_list)
country_df = pd.DataFrame(np.zeros((df.shape[0], len(country_list))))
country_df.columns = country_list
# print(country_df)
for i in range(df.shape[0]):
    for item in df["country"][i].split(","):
        country_df[item][i] = 1
print(country_df)
# all_data = df.join(country_df)
# print(all_data)
plt.figure(figsize=(20, 8))
plt.bar(range(country_df.sum().shape[0]), country_df.sum())
plt.show()
