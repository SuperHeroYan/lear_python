
import PyPDF2

pdf = PyPDF2.PdfFileReader(open('encryptedminutes.pdf', 'rb'))

dictonary = open('dictionary.txt')
dictonary_text = dictonary.readlines()
dictonary.close()

for passwords in range(0, len(dictonary_text)):
	password = dictonary_text[passwords]
	result = pdf.decrypt(password.replace('\n',''))
	if result == 1 :
		break
	else:
		print('Пароль ', password,' не подошел')

print('Пароль подобран:', password)