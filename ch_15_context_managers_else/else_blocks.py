
def else_example(item_list):
    for item in item_list:
        if item == 'banana':
            return 'Banana found'
    else:
        print(ValueError('No banana flavor found!'))


my_list_1 = ['apple', 'banana', 'peach']
my_list_2 = ['apple', 'peach', 'blueberry']
print('my_list_1:')
print(else_example(my_list_1))
print('my_list_2:')
print(else_example(my_list_2), '\n')


try:
    else_example(my_list_2)
except ValueError:
    print('no banana found')
else:
    print('banana tear-down after ValueError raised')
