def find_fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return find_fibonacci(n - 1) + find_fibonacci(n - 2)