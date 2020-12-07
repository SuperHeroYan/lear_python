
import PyPDF2
import os

for folderName, subFolder, fileNames in os.walk('.'):
	for fileName in fileNames:
		if fileName.endswith('.pdf'):
			pdfReader = PyPDF2.PdfFileReader(open(fileName, 'rb'))
			pdfWriter = PyPDF2.PdfFileWriter()

			if pdfReader.isEncrypted:
				print('Ошибка!! Документ ',pdfReader,' уже зашифрован')
				break

			for pageNum in range(pdfReader.numPages):
				pdfWriter.addPage(pdfReader.getPage(pageNum))

			pdfWriter.encrypt('swordfish')
			resultPdf = open(f'{fileName}__encrypted.pdf', 'wb')
			pdfWriter.write(resultPdf)
			resultPdf.close()
			print('Шифрование ',pdfReader,' прошло успешно')
