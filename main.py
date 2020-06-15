my_pets = ['bicha', 'zoee', 'chybasi', 'serun']
name = input('Enter a pet name: ')
if name not in my_pets:
    print(name,'Does not exit!')
else:
    print(name, ' is my pet')