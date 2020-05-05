import re
import reprlib


RE_WORD = re.compile(r'\w+')


class Sentence:
    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return f'Sentence ({reprlib.repr(self.text)})'

    def __iter__(self):
        for match in RE_WORD.finditer(self.text):
            yield match.group()


if __name__ == '__main__':
    s = Sentence('"The time has come," the Walrus said,')
    print(s.__iter__())
    print(s)
    for word in s:
        print(word)
