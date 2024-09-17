from collections.abc import Iterable, Iterator

class PrimeIterable(Iterable):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def __iter__(self):
        for k in range(self.a, self.b):
            if self.isprime(k):
                yield k
    
    def isprime(self, k):
        if k in [2, 3, 5, 7, 9, 11, 13, 17, 19, 23, 29]:
            return True
        else:
            return False
        

primes = PrimeIterable(1, 30)
primes_iter =  iter(primes)
print(isinstance(primes_iter, Iterator))
# for i in range(10):
#     print(next(primes_iter))
# for prime in primes:
#     print(prime)
                
        