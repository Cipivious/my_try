class Test:
    def __init__(self, name):
        self.name = name
        
    def __enter__(self):
        print("enter")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print(self.name, exc_type, exc_val, exc_tb)
        print("exit")
        return True
  
list = ["1", 1]
for item in list: 
    with Test("test_object") as obj:
        print(item + 1)