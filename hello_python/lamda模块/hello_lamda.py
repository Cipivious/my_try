
def quadratic(a, b, c):
    def constructer(x):
        return a*x**2 + b*x + c
    return constructer

result = quadratic(1, 2, 3)(3)
print(result)

f = lambda a,b,c: lambda x: a*x**2 + b*x + c
print(f(1, 2, 3)(3))