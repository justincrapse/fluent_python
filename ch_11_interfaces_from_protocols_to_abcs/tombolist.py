from random import randrange

from ch_11_interfaces_from_protocols_to_abcs.tombola import Tombola


@Tombola.register
class TomboList(list):
    def pick(self):
        if self:
            position = randrange(len(self))
            return self.pop(position)
        else:
            raise LookupError('pop from empty TomboList')

    load = list.extend

    def loaded(self):
        return bool(self)

    def inspect(self):
        return tuple(sorted(self))


if __name__ == '__main__':
    t = TomboList(range(100))
    print(isinstance(t, Tombola))  # this resolves to true, even though no inheritance is taking place
    print(TomboList.__mro__)  # mro is Method Resolution Order. this only lists the real (not virtual) superclasses.
