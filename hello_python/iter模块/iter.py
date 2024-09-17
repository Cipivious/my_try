from collections.abc import Iterator, Iterable  # 修改导入语句，适应新版本的Python

class WeatherIterator(Iterator):
    def __init__(self, cities):
        self.cities = cities
        self.index = 0
        import faker
        self.fake = faker.Faker("zh_CN")
        
    def __next__(self):
        if self.index == len(self.cities):
            raise StopIteration
        city = self.cities[self.index]
        self.index += 1
        return self.get_city_information(city)
    
    def get_city_information(self, city):
        return f"{city}: {self.fake.text()}"

class WeatherIterable(Iterable):
    def __init__(self, cities):
        self.cities = cities
        
    def __iter__(self):
        return WeatherIterator(self.cities)
        
def show(items):
    for item in items:
        print(item)
        
        
show(WeatherIterable(["北京", "天津", "上海"] * 10))
