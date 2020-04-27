import time
from ch_7_function_decorators_and_closures.clockdeco2 import clock


@clock
def snooze(seconds):
    time.sleep(seconds)


@clock
def factorial(n):
    return 1 if n < 2 else n*factorial(n-1)


if __name__ == '__main__':
    print('*' * 40, 'Calling snooze (.123)')
    snooze(0.123)
    print(snooze.__code__.co_freevars)  # this will appear as "func," but it is really snooze or clock wrapped up.
    print(factorial.__name__)  # this will now return "factorial" because of @functools.wraps(func) over "clocked"
    print(snooze.__name__)  # will now also return its own name.
    print('*' * 40, 'calling factorial(6)')
    print('6! =', factorial(6))
