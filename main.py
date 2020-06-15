cat_names = []

while True:
    print('Enter name of cat' + str( len(cat_names) + 1 ) +
        'or press enter to stop')
    name = input()
    if name == '':
        break
    cat_names += [name]

print('the cats names are:')
for name in cat_names:
    print(' ' + name)