class LookingGlass:
    def __enter__(self):
        import sys
        self.original_write = sys.stdout.write
        sys.stdout.write = self.reverse_write
        return 'JABBERWOCKY'

    def reverse_write(self, text):
        self.original_write(text[::-1])

    def __exit__(self, exc_type, exc_val, exc_tb):
        import sys
        sys.stdout.write = self.original_write
        if exc_type is ZeroDivisionError:
            print('Please Do Not divide by zero')
            return True


if __name__ == '__main__':
    with LookingGlass() as what:
        print('Alice, Kitty and Snowdrop')
        print(what)
    print(what)
    print('back to normal')

    # without with:
    print('\nWithout With:')
    manager = LookingGlass()
    print(manager)
    monster = manager.__enter__()
    print(monster == 'JABBERWOCKY')
    print(manager)
    manager.__exit__(None, None, None)
    print(monster)
