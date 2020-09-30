# renameDates.py - переименовывает файлы, имена которых включат в себя даты амерк.типа
# в евпорейский формат 
import os, re, shutil

# Создание регулярки которое будут узнать имена файлов
datePattern = re.compile(r"""^(.*?) # весь текст перед датой
	( (0|1)? \d)- # одна или две цифры месяца
	( (0|1|2|3)? \d)- # одна или две цифры числа
	( (19|20) \d\d) # четыре цифры года
	(.*?)$ # весь текст после даты
	""", re.VERBOSE) 

for amerFilename in os.listdir('.'):
	mo = datePattern.search(amerFilename)

	if mo == None:
		continue

	beforePart = mo.group(1)
	monthPart = mo.group(2)
	dayPart = mo.group(4)
	yearPart = mo.group(6)
	afterPart = mo.group(8)

	# Формировние имени файла, по европейски
	euroFilename = beforePart + dayPart + '-' + monthPart + \
			'-' + yearPart + afterPart

	# Получение полных абсолютеых путей к файлам
	asbWorkDir = os.path.abspath('.')
	amerFilename = os.path.join(asbWorkDir, amerFilename)
	euroFilename = os.path.join(asbWorkDir, euroFilename)

	# Переимнование файлов
	print('Заменяем имя "%s" \nИменем "%s"'
			% (amerFilename, euroFilename))

	shutil.move(amerFilename, euroFilename)

