# backupTozip - Делает резервные копии папки в архиве

import os, zipfile

def backupToZip(folder):
	# Создание копии всего содержимого папки "folder" в зипе
	folder = os.path.abspath(folder)
	print(os.path.basename(folder))
	# Определить какое имя файла должен использовать этот код
	# исходя из имен уже существующих файлов
	num = 1
	while True:
		zipFileName = os.path.basename(folder) + '_' + str(num) + '.zip'
		if not os.path.exists(zipFileName):
			break
		num += 1

	print('Создается файл %s...' % (zipFileName) )
	# Указывай путь куда будут зипа сохраняться перед zipFileName
	backupZip = zipfile.ZipFile(zipFileName, 'w')

	for foldername, subfolders, filenames in os.walk(folder):
		print('Добавление файлов из папки %s...' % (foldername)) 
		# Добавление теккущей папкеи в зип
		backupZip.write(foldername)
		

		# Добавить в зип все файлы из данной папки
		for filename in filenames:
			# Не дает закидывать в зип уже готовые зипы которые находятся в папке
			newBase = os.path.basename(folder) + '_'
			if filename.startswith(newBase) and filename.endswith('.zip'):
				continue

			backupZip.write(os.path.join(foldername, filename))

	backupZip.close()
	print('Готово.')

backupToZip('/home/yanchez/Музыка/moddbord')