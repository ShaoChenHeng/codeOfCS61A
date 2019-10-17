from operator import add, mul,truediv

def divide_all(n, ds):
    try:
        return reduce(truediv, ds, n)
    except ZeroDivisionError:
        return float('inf')

def reduce(f, s, initial):
    for x in s:
        initial = f( initial, x  )
    return initial

def reduce(f, s, initial):
    if not s:
        return initial
    else:
        first, rest = s[0], s[1:]
    return reduce(f, rest, f(initial, first))

