from inspect import getgeneratorstate


class DemoException(Exception):
    """ Exception for the demo """


def demo_exc_handling():
    print('-> coroutine started')
    while True:
        try:
            x = yield
        except DemoException:
            print(f'*** {DemoException.__name__} handled. Continuing...')
        else:
            print(f'-> coroutine received: {x}')
    raise RuntimeError('this will never run')


exc_coro = demo_exc_handling()
next(exc_coro)
exc_coro.send(11)
exc_coro.send(22)
exc_coro.close()
print(getgeneratorstate(exc_coro))

exc_coro = demo_exc_handling()
next(exc_coro)
exc_coro.send(11)
exc_coro.throw(DemoException)
print(getgeneratorstate(exc_coro))
exc_coro.send(33)
