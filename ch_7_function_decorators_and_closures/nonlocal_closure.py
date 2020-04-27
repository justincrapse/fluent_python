def make_averager():
    count = 0
    total = 0

    def averager(new_value):
        nonlocal count, total
        count += 1  # now we can do this without it being counted as a local variable that doesn't exist yet
        total += new_value
        return total / count

    return averager


avg = make_averager()
avg(10)
avg(11)
avg(12)

print(avg.__code__.co_varnames)
print(avg.__code__.co_freevars)
print(avg.__closure__)
print(list(cell.cell_contents for cell in avg.__closure__))
