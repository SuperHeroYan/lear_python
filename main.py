while True:
    print('Entert your age:')
    age = input()
    # Проверяет что бы были только цифры
    if age.isdecimal():
        break
    print('Please enter a number for you age')

while True:
    print('Select a new password (letters and numbers only)')
    password = input()
    # Что бы были только числа и буквы
    if password.isalnum():
        break
    print('Password can only have letters and numbers.')
