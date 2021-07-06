def fib(n):
    if n > 1:
        return fib(n - 1) + fib(n - 2)
    else:
        return n

    i = 0
    while i < n:
        fib(i)
        i += 1
    return fib(i)

print(fib(4))
