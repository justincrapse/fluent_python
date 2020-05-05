import re
import reprlib


RE_WORD = re.compile(r'\w+')


class Sentence:
    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return f'Sentence ({reprlib.repr(self.text)})'

    def __iter__(self):
        return (match.group() for match in RE_WORD.finditer(self.text))


if __name__ == '__main__':
    s = Sentence('"The time has come," the Walrus said,')
    print(s.__iter__())  # this returns a generator object, same as yield would do for a generator method.
    for word in s:
        print(word)
