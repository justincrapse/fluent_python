traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]

# the for-loop knows to unpack the tuple and assign to the two variables
for country, _ in traveler_ids:
    print(country)

# tuple unpacking for variable assignment
lax_coordinates = (33.9425, -118.409056)
latitude, longitude = lax_coordinates
print(latitude)
print(longitude)

# variable value swap without temporary variable:
b, a = (1, 99)
print(f'b = {b}')
print(f'a = {a}')
b, a = a, b
print(f'b = {b}')
print(f'a = {a}')

# Star "*" prefix for argument unpacking
t = (20, 8)
print(divmod(*t))

# assign arbitrary excess arguments:
a, b, *rest = range(5)
print(a, b, rest)
a, b, *rest = range(3)
print(a, b, rest)
a, b, *rest = range(2)
print(a, b, rest)

# this works in any position:
a, *body, c, d = range(5)
print(a, body, c, d)

# nested tuple unpacking
metro_areas = [
    (' Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    (' Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    (' Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    (' New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    (' Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
    ]

print('{:17} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
fmt = '{:17} | {:^9.4f} | {:^9.4f}'
for name, cc, pop, (latitude, longitude) in metro_areas:
    if longitude <= 0:
        print(fmt.format(name, latitude, longitude))
