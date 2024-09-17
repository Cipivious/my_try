import pickle
import collections

dq = collections.deque([_ for _ in range(10)], 5)
print(dq)

pickle.dump(dq, open("./dp.pkl", "wb"))