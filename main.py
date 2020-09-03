import re

password = input('Создайте пароль: .... \n')

regex = re.compile(r"""
	(?=.*\d)	# Проверяет есть ли хотябы одно число
	(?=.*[A-Z]) # Проверяет есть ли хотябы одна зглавная буква
	([a-zA-Z0-9]){8,}""") # Кавычки значат что до 8символов 

result = bool(regex.match(password))

if result == False:
	print('Пароль слабый')
else:
	print('Пароль сильный')
