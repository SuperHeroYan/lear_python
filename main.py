import os
import re

answer_user = input('Какое слово хотите искать?\n')

for file in os.listdir('./'):
	if file.endswith('.txt'):

		claypath = os.path.join('./', file)
		opened_file = open(claypath, 'r')
		content = opened_file.read()

		regex_patter = re.compile(rf'{answer_user}')
		result = re.findall(regex_patter, content)

		if result != [] and result != '':
			print(f'------------------------\nСлово найдено в файле{claypath}\n')
			print(content,'\n------------------------\n')
		else:
			print(f'- {claypath}')
		