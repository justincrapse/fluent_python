def fibonacci(iterations):
    a, b = 0, 1
    for _ in range(iterations):
        yield a
        a, b = b, a + b


print(list(fibonacci(9)))