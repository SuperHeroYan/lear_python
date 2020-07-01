# pw.py - Программа для незащищенного хранения паролей
import sys, pyperclip

PASSWORDS = {
            'email': 'goper@gmail.com',
            'blog': 'valmort_228',
            'luggage': '12343'}

code_access = '228'

while True:
    user_access = input('Введите пароль!\n')
    if user_access == code_access:
        break
   
    print('Пароль не верен!')

if len(sys.argv) < 2:
    print('Использоование: python pw.py [имя учетной записи] - \
        копирование пароля учетной записи')
    sys.exit()

account = sys.argv[1] # Первый аргумент командной строки это имя учет.записи

if account in PASSWORDS:
    # Копирует в буфер обмена 
    pyperclip.copy(PASSWORDS[account])
    print('Пароль для ' + account + ' скопирован в буфер')
else:
    print('Учетная запись ' + account + ' отсутствует в списке')
