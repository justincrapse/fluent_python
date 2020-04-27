import time
import functools


def clock(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.perf_counter()
        result = func(*args)  # this func function is available as a free variable
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_lst = []
        if args:
            arg_lst.append(', '.join(repr(arg) for arg in args))
        if kwargs:
            pairs = [f'{k}={w}' for k, w in sorted(kwargs.items())]
            arg_lst.append(', '.join(pairs))
        arg_str = '. '.join(arg_lst)
        print(f'[{elapsed} {name}({arg_str}) -> {result}')
        return result
    return clocked
