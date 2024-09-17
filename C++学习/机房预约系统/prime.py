import multiprocessing
from multiprocessing import Queue, Event
import time

gap = 5000

def is_prime(num):
    for i in range(2, num-1):
        if num % i == 0:
            return False
    return True

def worker(num, result_queue):
    for i in range(num, num + gap):
        if is_prime(i):
            result_queue.put(i)

def work_manager(stop_event, result_queue):
    num = 5
    while True:
        if stop_event.is_set():
            break
        progresses = []
        for _ in range(4):
            progresses.append(multiprocessing.Process(target=worker, args=(num, result_queue)))            
            num = num + gap 
        
        for i in range(4):
            progresses[i].start()
            
        for i in range(4):
            progresses[i].join()
        

def check_final(stop_event, result_queue):
    global tag
    result_list = []
    while True:
        prime_number = result_queue.get()
        result_list.append(prime_number)
        if len(result_list) > 30000:
            stop_event.set()
            break
    result_list.sort()
    print(result_list[-1])

if __name__ == "__main__":
    start_time = time.time()
    result_queue = Queue()
    stop_event = Event()  # 事件对象，用于控制进程的停止
    work_manager_process = multiprocessing.Process(target=work_manager, args=(stop_event, result_queue))
    check_final_process = multiprocessing.Process(target=check_final, args=(stop_event, result_queue))
    work_manager_process.start()
    check_final_process.start()
    
    work_manager_process.join()
    check_final_process.join()
    end_time = time.time()
    print(f"一共耗时{end_time-start_time}秒")
    

