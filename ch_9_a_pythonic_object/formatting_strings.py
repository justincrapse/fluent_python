blue = 0.2342523532432
green = f'Formatted Number: {blue:0.2f}'
red = f'Percent Format: {blue:0.2%}'
print(green)
print(red)


class Iiumizer:
    def __init__(self, word):
        self.word = word

    def __format__(self, format_spec):
        if format_spec == 'i':
            return self.word + 'ium'

    def __str__(self):
        return self.word


lumar = Iiumizer('Lumar')
print(lumar)
print(f'{lumar:i}')  # Lumar becomes Lumarium