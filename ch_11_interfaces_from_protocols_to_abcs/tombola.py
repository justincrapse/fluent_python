import abc


class Tombola(abc.ABC):  # user-defined ABCs must inherit from abc.ABC
    @abc.abstractmethod
    def load(self, iterable):
        """Add items from an iterable"""  # often the body is empty except for a docstring

    @abc.abstractmethod
    def pick(self):
        """Remove random item. This method should raise `LookupError` when the instance is empty."""

    def loaded(self):
        return bool(self.inspect())

    def inspect(self):
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
        self.load(items)
        return tuple(sorted(items))


