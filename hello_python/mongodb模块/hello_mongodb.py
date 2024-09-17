from pymongo import MongoClient
import random
import faker
fake = faker.Faker(locale="zh_CN")

# 连接到 MongoDB
client = MongoClient('mongodb://localhost:27017/')  # 修改为你的 MongoDB 连接字符串
db = client.run  # 替换为你的数据库名称
collection = db.fakeData  # 替换为你的集合名称

# 每次读十个直至读完所有的内容
# 每次读取的文档数
batch_size = 10
skip_count = 0

while True:
    # 查询当前批次的文档
    cursor = collection.find().skip(skip_count).limit(batch_size).sort({"age":1})
    
    # 将游标转换为列表
    docs = list(cursor)
    
    # 如果没有更多文档了，退出循环
    if not docs:
        break
    
    # 处理当前批次的文档
    for doc in docs:
        print(doc)
    print("*"*90)
    # 更新跳过的文档数
    skip_count += batch_size



# 删除选定的文档
# collection.delete_many({"age": {"$gte": 50}})

# for doc in collection.find({"age": {"$gt": 40}}).sort({"age":1}):
#     print(doc)




###############################################这个可以用来生成随机的文档来填充数据库###############################################
# for _ in range(10):
#     data = {
#         "name": fake.name(),
#         "age": random.randint(12, 60),
#         "description": fake.text()
#     }
#     collection.insert_one(data)


# for doc in collection.find({"age": {"$gt": 50}}):
#     print(doc)
############################################### 获取文档总数 #####################################################################
# 示例用法# 使用aggregate方法统计文档总数
# pipeline = [
#     {"$count": "total_count"}
# ]
# result = list(collection.aggregate(pipeline))
# print(result)
# # 打印结果
# if result:
#     print(f"总文档数: {result[0]['total_count']}")
# else:
#     print("集合中没有文档")


############################################### 查找所有文档并更新 ###############################################################
# # 定义一个函数来生成随机的性别
# def get_random_gender():
#     return 'female' if random.random() < 0.5 else 'male'
# for doc in collection.find():
#     collection.update_one(
#         {'_id': doc['_id']},
#         {'$set': {'gender': get_random_gender()}}
#     )
# print("更新完成")

