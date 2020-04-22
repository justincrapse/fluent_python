# good alternative to bisect is sortedcollections recipe by Raymond Hettinger

from sc_33 import SortedCollection

s = SortedCollection([3, 252, 23, 66])
print(s)
s.insert(55)
print(s)

found = s.index(66)
print(found)