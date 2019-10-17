from tree import *

def divisor(n):
    for i in range(2, n):
        if n % i == 0:
            yield i

def a_path(t, x):
    if label(t) == x:
        return (x)
    for b in branches(t):
        rest_of_path = a_path(b, x)
        if rest_of_path:
            return [label(t)] + rest_of_path
