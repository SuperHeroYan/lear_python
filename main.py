# mcb.pyw - Сохраняет и загружает фрагменты текста в буфер
# Использование: py.exe mcb.pyw save <ключение_слово> -
# 				Сохраняет буфер обмена в ключевом словое.
#				py.exe mcb.pyw <ключение_слово>
#					Загружает ключ.слово в буфер обмена 
#					py.exe mcb.pyw list - 
#					Загружает все ключевые слов в буфер

import shelve, pyperclip, sys
mcbShelf = shelve.open('mcb')

# Сохранение в буфер
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
	mcbShelf[sys.argv[2]] = pyperclip.paste()
	print('Your data buffer successyfyly copy to database')
	mcbShelf.close()

# вывод всех данных и бд
elif len(sys.argv) == 2 and sys.argv[1].lower() == 'show':
	print('List of Db:')
	for key in mcbShelf:
		print('[',key,']', '-', mcbShelf[key])

# Копирует содержимое базы данаах в виде списка в буфер
elif len(sys.argv) == 2 and sys.argv[1].lower() == 'list':
	pyperclip.copy(str(list(mcbShelf.keys())))
	print('List of records successyfyly copy to bufer')
	mcbShelf.close()

#Берет значение из хранилища и помещает в буфер
elif sys.argv[1] in mcbShelf:
		pyperclip.copy(mcbShelf[sys.argv[1]])
		print('Your record successyfyly copy in bufer')
		mcbShelf.close()

# Удаление записей из бд
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
	del mcbShelf[sys.argv[2]]
	print('Record successyfyly deleted')
	mcbShelf.close()

# Удаление всех записей из бд
elif len(sys.argv) == 2 and sys.argv[1].lower() == 'clear':
	mcbShelf.clear()
	print('All record successyfyly deleted')
	mcbShelf.close()

else:
	print('Error command, try again')
	mcbShelf.close()
