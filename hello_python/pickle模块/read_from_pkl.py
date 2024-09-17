import pickle

q = pickle.load(open("./dp.pkl", "rb"))
print(q)

for i in q:
    print(i)