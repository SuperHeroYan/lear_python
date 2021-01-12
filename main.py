
import io
import json
from zipfile import ZipFile

buf = io.BytesIO()

with ZipFile(buf, 'w') as file:
	with io.BytesIO() as json_buf:

		"""Превращаем данные в json"""
		obj = {'sex':'pleauser', 'death':'suffer'}
		data = json.dumps(obj)
		"""записываем данные в буфер """
		json_buf.write(data.encode())
		json_buf.seek(0) # При записи в буфер, байт смещаеться, и мы его возвразаем 

		file.writestr('1.json', json_buf.read())

with open('1.zip', 'wb') as file:
	buf.seek(0)
	file.write(buf.read())
