l = list(range(10))
print(l)
l[2:5] = [20, 30]
print(f'l[2:5] = [20, 30]: {l}')
del l[5:7]
print(f'del l[5:7]: {l}')
l[3::2] = [11, 22]
print(f'l[3::2] = [11, 22]: {l}')
