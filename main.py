
# Програма которая открывает несколько первых вкладок из google

import requests, os, webbrowser, bs4

url = 'https://xkcd.com/'

os.makedirs('xkcd', exist_ok=True)


while not url.endswith('#'):
	print('Dowload %s...' % url)
	res = requests.get(url)
	res.raise_for_status()

	soup = bs4.BeautifulSoup(res.text, 'lxml')
	comicElem = soup.select('#comic img')

	if comicElem == []:
		print('Не удалось найти изображение комикс.')
	else:
		# Получаем ссылку на картинку
		comicUrl = 'https:' + comicElem[0].get('src')
		print('Загружается изображение %s...' % (comicUrl))
		res = requests.get(comicUrl)
		res.raise_for_status()
		# Сохранение фалфа в папке
		imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')

		for chunk in res.iter_content(100000):
			imageFile.write(chunk)
		imageFile.close()

	prevLink = soup.select('a[rel="prev"]')[0]
	url = 'https://xkcd.com' + prevLink.get('href')

print('Готово')
