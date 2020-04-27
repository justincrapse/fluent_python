def make_averager():
    series = []
    blue = 99  # this will not be a freevar because it is not accessed in averager function

    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total/len(series)

    return averager


avg = make_averager()
avg(10)
avg(11)
avg(12)

print(avg.__code__.co_varnames)
print(avg.__code__.co_freevars)
print(avg.__closure__)
print(avg.__closure__[0].cell_contents)
