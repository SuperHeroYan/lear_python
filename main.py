birthdays = {'olga': '7 june', 'petr': '21 june'}

while True :
    name = input('Enter a name: (blank to quit)')
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday information for ' + name)
        bday = input('You wanna do add birthday in base of birthdays? ' +
                    '(blank to quit) ')
        if bday == '':
            break
        else:
            birthdays[name] = bday
            print('Greate, base update!')
