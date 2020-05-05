import re
import reprlib


RE_WORD = re.compile(r'\w+')


class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __getitem__(self, index):  # this tells python to create __iter__ and attempt indexing, starting at 0
        return self.words[index]

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return f'Sentence ({reprlib.repr(self.text)})'  # reprlib.repr truncates the output string with elipses


if __name__ == '__main__':
    s = Sentence('"The time has come," the Walrus said,')
    print(s)
    for word in s:
        print(word)


