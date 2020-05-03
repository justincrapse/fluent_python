entries = [
    'string, with, commas',
    ['list', 'of', 'strings'],
    ('tuple', 'of', 'strings'),
    {'set', 'of', 'strings'},  # set won't keep in order FYI
]
for words in entries:
    try:
        words = words.replace(',', ' ').split()
    except AttributeError:
        pass
    words = tuple(words)  # this makes sure it is an iterable
    print(words)
