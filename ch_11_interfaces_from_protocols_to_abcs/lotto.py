import random

from ch_11_interfaces_from_protocols_to_abcs.tombola import Tombola


class LotteryBlower(Tombola):
    def __init__(self, iterable):
        self._balls = list(iterable)  # good practice to take any iterable and make your own list out of it since
        # iterable being passed may not be designed to be changed (passed by reference and mutable!)

    def load(self, iterable):
        self._balls.extend(iterable)

    def pick(self):
        try:
            position = random.randrange(len(self._balls))
        except ValueError:
            raise LookupError('pick from empty BingoCage')
        return self._balls.pop(position)

    def loaded(self):
        return bool(self._balls)

    def inspect(self):
        return tuple(sorted(self._balls))


lotto = LotteryBlower(range(10))
print(lotto.inspect())
