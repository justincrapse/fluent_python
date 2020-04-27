b = 4


# unresolved reference b/referenced before assignment
def super_fun(a=5):
    print(a)
    print(b)
    b = 99


def more_fun(a=5):
    global b
    print(a)
    print(b)
    b = 99


if __name__ == '__main__':
    print(more_fun())
    print(b)
