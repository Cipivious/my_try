with open("./hello_with.py", "r", encoding="utf-8") as from_file, open("./hello_with_copy.py", "w", encoding="utf-8") as to_file:
    to_file.write(from_file.read())