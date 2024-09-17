import argparse
import json

if __name__ == "__main__":
    # 读取默认的配置
    file = open("./config.json", "r", encoding="utf-8")
    config = json.load(file)
    file.close()
    # 从命令行加载配置
    parser = argparse.ArgumentParser()
    parser.add_argument("--first-arg", default=config["argparser"]["first_arg"])
    parser.add_argument("--secend-arg", default=config["argparser"]["secend_arg"])
    # 将parser解析成一个namespaces对象
    args = parser.parse_args()
    # print(args)
    # 这个可以吧args变成一个字典然后遍历它的键值对
    # for key, arg in vars(args).items():
    #     print(key)
    #     print(arg)
    # 用这种方法可以获取对应的参数的值
    print(args.first_arg)
    print(args.secend_arg)