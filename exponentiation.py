def exp(b,n):
    if n == 0:
        return 1
    return b * exp( b, n - 1  )

def square(x):
    return x * x

def fast_exp(b, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return square(fast_exp(b, n // 2))
    else:
        return b * fast_exp(b, n - 1)
