import numpy as np
from numpy import ndarray

us_data = np.loadtxt("./us_data.csv", dtype="int", delimiter=",")
uk_data = np.loadtxt("./uk_data.csv", dtype="int", delimiter=",")

zeros = np.zeros((us_data.shape[0], 1), dtype="float")
ones = np.ones((uk_data.shape[0], 1), dtype="float")

us_data = np.hstack((us_data, zeros))
uk_data = np.hstack((uk_data, ones))

data = np.vstack((us_data, uk_data))
# print(np.asarray(data.mean(axis=0), dtype="int"))
data[1, 2:] = np.nan
print(data)


def fill_ndarray(data: ndarray):
    for i in range(data.shape[1]):
        temp = data[:, i]
        nan_num = np.count_nonzero(temp != temp)
        if nan_num != 0:
            temp_not_non_col = temp[temp == temp]
            temp[np.isnan(temp)] = temp_not_non_col.mean()
    return data


data = fill_ndarray(data)
print(data)
