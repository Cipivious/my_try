def counter(start_num):
    while True:
        yield start_num
        start_num += 1


new_counter = counter(10)

for i in range(100):
    print(next(new_counter))
