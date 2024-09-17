str = "abc1234xyz"

new_str = str.translate(str.maketrans("abcxyz", "XYZABC"))
print(new_str)