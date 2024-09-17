import mmap
import os

# 创建一个示例文件，并写入一些数字作为字节
filename = "example_numbers.bin"
with open(filename, "wb") as f:
    f.write(bytearray(range(10)))  # 写入 0-9 的数字，每个数字占一个字节

# 打开文件并将其映射到内存中
with open(filename, "r+b") as f:
    # 获取文件大小
    size = os.path.getsize(filename)
    print(list(f.read()))
    # 将文件内容映射到内存
    mmapped_file = mmap.mmap(f.fileno(), size)
    
    # 将文件内容作为数组进行操作
    print("Original content as array:")
    print(list(mmapped_file))  # 打印原始内容
    
    # 修改数组中的某些值
    mmapped_file[0] = 100  # 将第一个字节修改为 100
    mmapped_file[1] = 101  # 将第二个字节修改为 101
    mmapped_file[9] = 109  # 将最后一个字节修改为 109
    
    # 再次读取修改后的内容
    print("\nModified content as array:")
    print(list(mmapped_file))
    
    # 关闭 mmap 对象
    mmapped_file.close()

# 验证文件内容已经被修改
with open(filename, "rb") as f:
    print("\nFinal content in the file:")
    print(list(f.read()))
