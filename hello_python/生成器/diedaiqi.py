class Empoloyee:
    def __init__(self, empoloyees):
        self.empoloyees = empoloyees

    def __getitem__(self, item):
        return self.empoloyees[item]


emps = Empoloyee(["张三", "李四", "王五"])

for emp in emps:
    print(emp)
