
# CombinePdfs.py - Обьединяет все PDF документы находящиуся в текущем рабочем
import PyPDF2 as pdf, os

# Получение списка имен всех PDF-файлов
pdfFiles = []

for filename in os.listdir('.'):
	if filename.endswith('.pdf'):
		pdfFiles.append(filename)

# Огранизация цикла по всем файлам
pdfFiles.sort(key=str.lower)
pdfWriter = pdf.PdfFileWriter()

for filename in pdfFiles:
	pdffileObj = open(filename, 'rb')
	pdfReader = pdf.PdfFileReader(pdffileObj)
	# Проход цикла по всем станицам без первой
	for pageNum in range(1, pdfReader.numPages):
		pageObj = pdfReader.getPage(pageNum)
		pdfWriter.addPage(pageObj)

# Сохранение результат
pdfOutput = open('allminutes.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()
