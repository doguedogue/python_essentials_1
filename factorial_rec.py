def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * factorial_function(n - 1)


for n in range(1, 6): # testing
    print(n, factorial_function(n))