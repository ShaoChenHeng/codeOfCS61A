def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n-2) + fib(n-1)

def fac(n):
    if n == 1:
        return 1
    return fac(n-1) * n

def count(f):
    def counted(*args):
        counted.call_count += 1
        return f(*args)
    counted.call_count = 0
    return counted

def memo(f):
    cache = {}
    def memoized(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return memoized

def factors(n):
    total = 0
    for k in range(1, n + 1):
        if divides(k, n):
            total += 1
    return total

@count  
def divides(k, n):
    return n % k == 0

from math import sqrt
def factors_fast(n):
    total = 0
    sqrt_n = sqrt(n)
    k = 1
    while k < sqrt_n:
        if divides(k,n):
            total += 2
        k += 1
    if k * k == n:
        total += 1
    return total

