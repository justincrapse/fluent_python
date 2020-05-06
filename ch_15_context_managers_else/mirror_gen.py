import contextlib


@contextlib.contextmanager  # wrapper for implementing __enter__ and __exit__
def looking_glass():
    import sys
    original_write = sys.stdout.write

    def reverse_write(text):
        original_write(text[::-1])

    sys.stdout.write = reverse_write
    msg = ''
    # when using the contextmanager, you must use try, except, finally to catch errors that can occur within
    # the with block that the users will implement.
    try:
        yield 'JABBERWOCKY'  # everything before the yield is like __enter__, everything after is like __exit__
    except ZeroDivisionError:
        msg = 'Please Do Not divide by zero'
    finally:
        sys.stdout.write = original_write
        if msg:
            print(msg)


if __name__ == '__main__':
    with looking_glass() as what:
        print('Alice, Kitty and Snowdrop')
        print(what)
    print(what)
    print('back to normal')
