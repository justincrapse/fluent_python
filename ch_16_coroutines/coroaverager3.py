from collections import namedtuple

Result = namedtuple('Result', 'count average')


# the subgenerator:
def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield
        if term is None:
            break
        total += term
        count += 1
        average = total/count
    return Result(count, average)


# the delegating generator
def grouper(results, key):
    while True:
        results[key] = yield from averager()


# the client code, a.k.a. the caller
def main(data):
    results = {}
    for key, values in data.items():
        group = grouper(results, key)
        next(group)
        for value in values:
            group.send(value)
        group.send(None)  # important!

    # print (results)  # uncomment to debug
    report(results)


# output report
def report(results):
    for key, result in sorted(results.items()):
        group, unit = key.split(';')
        print(f'{result.count:2} {group:5} averaging {result.average:.2f} {unit}')
