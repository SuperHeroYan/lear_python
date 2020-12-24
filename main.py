
# removeCsvHeader - удаляте заголовки из файлов
import os, csv

os.makedirs('headerRemoved', exist_ok=True)

for csvFileName in os.listdir('.'):
	if not csvFileName.endswith('.csv'):
		continue # Пропускает файла без расширения csv
	print('Удаление заголовка из файла ' + csvFileName + '.....')
	# прочитать csv файл с пропускаом первой строки
	csvRows = []
	csvFileObj = open(csvFileName)
	readerObj = csv.reader(csvFileObj)
	for row in readerObj:
		if readerObj.line_num == 1:
			continue
		csvRows.append(row)
	csvFileObj.close()
	# ЗАпись файла
	csvFileObj = open(os.path.join('headerRemoved', csvFileName), 'w', newline='')
	csvWriter = csv.writer(csvFileObj)
	for row in csvRows:
		csvWriter.writerow(row)
	csvFileObj.close()
