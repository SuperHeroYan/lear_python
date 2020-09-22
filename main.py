# Madlibs prog
import re
# открываем файл для чтения и вывлда контета пользователю
textfilecontent = open('keks.txt')
content = textfilecontent.read()
print(content)

find_adj = re.compile(r'ADJECTIVE')
# Проверяем есть ли в контенте ADJECTIVE если есть то запускаеться цикл
starteradj = bool(find_adj.search(content))
counteradj = 0

while starteradj == True:
	counteradj += 1
	adjin = input(f'Введите {counteradj} прилагательное: \n')
	content = re.sub(find_adj, adjin, content, 1)
	starteradj = bool(find_adj.search(content))
	print('\n',content)

find_noun = re.compile(r'NOUN')

starternoun = bool(find_noun.search(content))
counternoun = 0

while starternoun == True:
	counternoun += 1
	nounin = input(f'Введите {counternoun} существительное: \n')
	content = re.sub(find_noun, nounin, content, 1)
	starternoun = bool(find_noun.search(content))
	print('\n',content)

find_verb = re.compile(r'VERB')

starterverb = bool(find_verb.search(content))
counterverb = 0

while starterverb == True:
	counterverb += 1
	verbin = input(f'Введите {counterverb} глагол: \n')
	content = re.sub(find_verb, verbin, content, 1)
	starterverb = bool(find_verb.search(content))
	print('\n',content)


textfilecontent = open('keks.txt', 'w')
textfilecontent.write(content)
