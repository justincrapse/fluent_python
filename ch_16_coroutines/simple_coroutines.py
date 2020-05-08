from inspect import getgeneratorstate


def simple_coroutine(a):
    print('-> Started: a = ', a)
    b = yield a  # b != a. b receives what is sent in my_coro.send(), which is 28 in the code below
    print('-> Received: b =', b)
    c = yield a + b
    print('-> Received: c =', c)


my_coro = simple_coroutine(14)
print(getgeneratorstate(my_coro))
next(my_coro)  # prints first message and runs to yeild a, yielding number 14
print(getgeneratorstate(my_coro))
print(my_coro.send(28))  # assigns 28 to b, prints second message, and runs through to next yield (a + b '42')
try:
    print(my_coro.send(99))  # runs the rest of the code, then terminates with StopIteration exception
except StopIteration:
    print(getgeneratorstate(my_coro))
