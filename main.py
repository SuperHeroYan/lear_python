import os, shutil

folder = '/home/yanchez/Музыка'

for foldername, subfolders, filenames in os.walk(folder):
	counter = 1

	for filename in filenames:
		filenamePath = os.path.join(foldername, filename)
		# вычисляте размер мегабайта, то есть возводит 2 в 20 степеньи уможнает на1с
		# то есть 1*2**20
		sizefile = os.path.getsize(filenamePath)/float(1<<20)

		if sizefile > 3:
			print(filenamePath)
			print('Размер: ',sizefile,'мб')
			print('---------------------------')
