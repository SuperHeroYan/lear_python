import os, shutil

folder = '/home/yanchez/Музыка'

for foldername, subfolders, filenames in os.walk(folder):
	counter = 1

	for filename in filenames:
		counter += 1
		if filename.endswith('.jpg'):
			filenamePath = os.path.join(foldername, filename)
			shutil.copy(filenamePath, '/home/yanchez/Музыка/fffffffffffffffff')
			
		elif filename.endswith('.png'):
			filenamePath = os.path.join(foldername, filename)
			shutil.copy(filenamePath, '/home/yanchez/Музыка/fffffffffffffffff')
