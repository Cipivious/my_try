import psutil

def get_disk_usage():
    # 获取所有磁盘分区的信息
    partitions = psutil.disk_partitions()
    
    try:
        for partition in partitions:
            # 获取分区的使用情况
            usage = psutil.disk_usage(partition.mountpoint)
            print(f"Disk: {partition.device}")
            print(f"  Mountpoint: {partition.mountpoint}")
            print(f"  File system type: {partition.fstype}")
            print(f"  Total Size: {usage.total / (1024**3):.2f} GB")
            print(f"  Used: {usage.used / (1024**3):.2f} GB")
            print(f"  Free: {usage.free / (1024**3):.2f} GB")
            print(f"  Percentage: {usage.percent}%\n")
    except:
        pass

if __name__ == "__main__":
    get_disk_usage()
