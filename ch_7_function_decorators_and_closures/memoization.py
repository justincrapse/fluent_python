from ch_7_function_decorators_and_closures.clockdeco2 import clock
import functools


@functools.lru_cache()
@clock
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)


@clock
def fibonacci_slow(n):
    if n < 2:
        return n
    return fibonacci_slow(n-2) + fibonacci_slow(n-1)


print(fibonacci_slow(25), '\n')
print(fibonacci(25))