import time


def clock(granularity=3):
    def decorate(func):
        def clocked(*_args):
            t0 = time.time()
            _result = func(*_args)
            elapsed = time.time() - t0
            name = func.__name__
            args = ', '.join(repr(arg) for arg in _args)
            result = repr(_result)
            print(str(locals()['elapsed'])[:granularity])
            return _result
        return clocked
    return decorate


if __name__ == '__main__':
    @clock(granularity=7)
    def snooze(seconds):
        time.sleep(seconds)

    for i in range(3):
        snooze(.123)

