from functools import singledispatch


@singledispatch
def process_name(name):
    print('my name is ' + name)


@process_name.register(int)
def _(int_name):
    name = str(int_name)
    print('my name is ' + name)


@process_name.register(tuple)
def _(tuple_name):
    name = ''.join(str(i) for i in tuple_name)
    print('my name is ' + name)


process_name('Mickey')
process_name(7777)
process_name((3, 4, 2))
