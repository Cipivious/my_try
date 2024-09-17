import time

time_struct = time.localtime()
time_str = time.strftime(r"%Y-%m-%d", time_struct)
print(time_str)
new_time_struct = time.strptime(time_str, r"%Y-%m-%d")
new_time_str = time.strftime(r"%m/%d/%Y" ,new_time_struct)
print(new_time_str)