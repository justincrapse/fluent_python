

from collections import namedtuple

City = namedtuple('City', 'name country population coordinates')  # space-delimited or an iterable of strings
tokyo = City('Tokyo', 'JP', 36.933, (35.933, 139.691667))  # must be a an iterable here
print(tokyo)
print(tokyo.population)
print(tokyo.coordinates)
print(tokyo[1])
print(f'Fields: {City._fields}')

LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
delhi = City._make(delhi_data)  # City(*delhi_data) would do the same.
print(f'As Dict: {delhi._asdict()}')
for key, value in delhi._asdict().items():
    print(key + ':', value)


