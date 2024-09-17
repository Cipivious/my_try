from collections import deque
import pickle
import random
import os

def get_result(real_num, guess_num):
    if real_num > guess_num:
        print(f"{guess_num}比要猜测的数字小")
        return False
    elif real_num < guess_num:
        print(f"{guess_num}比要猜测的数字大")
        return False
    else:
        print(f"恭喜你，你猜对了，{guess_num}就是最终的答案")
        return True
        
if __name__ == "__main__":
    print("欢迎你进入这个猜谜游戏")
    if os.path.exists("./history.pkl"):
        data = pickle.load(open("./history.pkl", "rb"))
        locals().update(data)
        result = input("已有存档，是否进入新游戏：Y/N ")
        if result == "Y":
            real_num = None
    else:
        hq = deque([], 5)
        real_num = None 
        
    while True:
        if not real_num:
            real_num = random.randint(0, 100)       
        guess_num = input("请输入一个你猜测的数字： ")

        if guess_num == "history":
            print("历史记录是", hq)
            continue
        hq.append(guess_num)
        if get_result(real_num, int(guess_num)):
            result = input("是否要开始新游戏？N/Y  ")
            if result == "Y":
                real_num = None
                continue
            else:
                break
            
    pickle.dump({"real_num": real_num, "hq": hq}, open("history.pkl", "wb"))    
    print("history 已经保存")  
        
                
    
    