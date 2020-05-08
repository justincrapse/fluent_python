from ch_16_coroutines.coroutil import coroutine


def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total/count


coro_avg = averager()
next(coro_avg)
print(coro_avg.send(10))
print(coro_avg.send(30))
print(coro_avg.send(5))


@coroutine
def averager_decorated():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total/count


coro_avg = averager_decorated()
# next(coro_avg) ## this is no longer needed ##
print(coro_avg.send(10))
print(coro_avg.send(30))
print(coro_avg.send(5))
